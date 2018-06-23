const initialize = function(pageBase) {

  /*
   * Search Support
   *
   * Uses lunr.js to support search over the documents.
   */

  var documents = {};
  var idx = null;
  var currentQuery = null;

  function search(query) {
    if (idx !== null && query !== null && currentQuery !== query) {
      console.log("query changed from '" + currentQuery + "' to '" + query + "'");
      currentQuery = query;
      var results = idx.search(currentQuery);
      var grouped = groupByLocation(results);
      var content = '<div class="list-group">' + grouped
        .map(function(matches) {
          return matches[1]
            .map(function(match) {
              var doc = documents[match.ref];
              var text = summarize('text', doc.text, match);
              var classes = 'list-group-item list-group-item-action flex-column align-items-start';
              return '<a href="' + pageBase + doc.location + '" class="' + classes + '">'
                + '<div class="d-flex w-100 justify-content-between">'
                + '<h6 class="mb-1">' + doc.pageTitle + ' > ' + doc.title + '</h6>'
                + '</div>'
                + '<small class="mb-1">' + text + '</small>'
                + '</a>';
            })
            .join('');
        })
        .join('') + "</dl>";
      var header = (currentQuery === '')
        ? '<div>Type to start searching.</div>'
        : "<div>" + results.length + " matches for '<b>" + currentQuery + "</b>'</div>";
      $("#search-results").html(header + '<hr/>' + content);
    }
  }

  function groupByLocation(results) {
    var map = new Map();
    results.forEach(function(match) {
      var doc = documents[match.ref];
      var loc = doc.location;
      var fragmentPos = loc.indexOf("#");
      if (fragmentPos > 0) {
        loc = loc.substring(0, fragmentPos);
      }
      if (map.has(loc)) {
        map.get(loc).push(match);
      } else {
        map.set(loc, [match]);
      }
    });

    var grouped = Array
      .from(map.entries())
      .sort(function (a, b) {
        return aggregateScore(b[1]) - aggregateScore(a[1]);
      });
    return grouped;
  }

  function aggregateScore(matches) {
    var sum = 0.0;
    matches.forEach(function(m) { sum += m.score; });
    return sum;
  }

  function summarize(field, text, match) {
    // Highlight the terms that lead to it matching
    var content = '';
    var meta = match.matchData.metadata;
    for (var k in meta) {
      if (field in meta[k]) {
        var positions = meta[k][field].position;
        var p = 0;
        for (var i = 0; i < positions.length; ++i) {
          var s = positions[i][0];
          var e = s + positions[i][1];
          content += text.substring(p, s);
          content += '<b>' + text.substring(s, e) + '</b>';
          p = e;
        }
        content += text.substring(p, text.length);
      } else {
        content = text;
      }
    }

    // Extract first sample sentence with a match
    var match = '';
    content.split(/[.?!;]\s/).forEach(function(sentence) {
      if (sentence.indexOf("<b>") >= 0) {
        match += sentence + "... ";
      }
    });
    if (match.length > 200) {
      var s = match.lastIndexOf('<b>', 200);
      var e = match.lastIndexOf('</b>', 200);
      if (s > e) {
        // Boundary is inside of tag, push to end
        match = match.substring(0, e + 4);
      } else {
        // Boundary to next whitespace
        var p = match.indexOf(' ', 200);
        match = match.substring(0, p);
      }
    }
    return match;
  }

  $("#search").keyup(function() {
    search($(this).val());
  });

  $('#search-modal').on('shown.bs.modal', function () {
    $('#search').trigger('focus')
    if (idx === null) {
      $('#search-results').html('<p>Loading search index...</p>');
      fetch(pageBase + 'search.json')
        .then(function(response) {
          if (response.status !== 200) {
            var status = 'Failed to load index: ' + response.status + ' ' + response.statusText;
            $('#search-results').html('<p style="color: red;">' + status + '</p>');
          } else {
            response.text().then(function(json) {
              try {
              var docs = JSON.parse(json).docs;

              docs.forEach(function(doc) {
                documents[doc.location] = doc;
              });

              idx = lunr(function () {
                this.ref('location');
                this.field('title');
                this.field('text');
                this.metadataWhitelist = ['position'];

                docs.forEach(function(doc) {
                  this.add(doc)
                }, this)
              });

              search($('#search').val());
              } catch(err) {
                var status = 'Failed to load index: ' + err.message;
                $('#search-results').html('<p style="color: red;">' + status + '</p>');
              }
            });
          }
        })
    }
  });

  /*
   * Header Links
   *
   * Add quick link the user can click on to get to that header on the page.
   */

  $('h1, h2, h3, h4, h5, h6').each(function() {
    var href = $(this).find('a').attr('href');
    var text = $(this).text();
    $(this).html(
      '<a name="' + href.substring(1) + '" href="' + href + '" class="anchor"></a>' +
      '<a href="' + href + '">' + text + '</a>');
  });

  /*
   * Image Widths
   *
   * Set the max-width on images to ensure they do not exceed the content div.
   */
  $('img').each(function() {
    $(this).css('max-width', '100%');
  });

  /*
   * Code Snippets
   *
   * Rewrite code definition lists to divs with appropriate class.
   */

  $('dl').replaceWith(function() {
    //$(this).attr('class', 'nav nav-tabs').attr('role', 'tablist');
    var group = '';
    var content = '<div>';
    $(this).find('dt, dd').each(function() {
      if ($(this).prop('tagName') === 'DT') {
        group = $(this).text().toLowerCase();
      } else {
        content += '<div class="group-' + group + '">' + $(this).html() + '</div>';
      }
    });
    content += '</div>';
    return content;
  });

  /*
   * Group Selection
   *
   * Needs to be after the rewrites for code snippets so that the initial display setting
   * is correctly set. Initial group selection can come from 3 sources, in order of precedence
   * they are:
   *
   * 1). Url parameter, to allow for precise linking.
   * 2). Cookie, (not yet implemented), to support user default.
   * 3). First in select list, if no preference is specified.
   */

  function getParameter(name) {
    var query = window.location.search.substring(1);
    params = query.split('&');
    for (var i = 0; i < params.length; ++i) {
      var p = params[i].split('=');
      if (p[0] === name) {
        return p[1];
      }
    }
    return null;
  }

  function setInitialGroup() {
    var language = getParameter('language');
    if (language !== null) {
      $('select[name=Language]').val('group-' + language.toLowerCase());
    }
  }

  function updateGroupDisplay() {
    var select = $('select[name=Language]');
    var language = '.' + select.val();
    select.find('option').each(function() {
      var cls = '.' + $(this).attr('value');
      if (cls === language) {
        $(cls).css('display', 'initial');
      } else {
        $(cls).css('display', 'none');
      }
    });
  }

  setInitialGroup();
  updateGroupDisplay();
  $('select[name=Language]').change(updateGroupDisplay);
};