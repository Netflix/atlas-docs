<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
      integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4"
      crossorigin="anonymous">
    <link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css"
      integrity="sha256-eZrrJcwDc/3uDhsdt61sL2oOBY362qM3lon1gyExkL0="
      crossorigin="anonymous">
    <link rel="stylesheet" href="$page.base$css/page.css">

    <title>Atlas</title>
  </head>
  <body>
    <header class="navbar navbar-expand-lg navbar-dark" id="nav-top">
      <a class="navbar-brand" href="$page.base$index.html">
        <img src="$page.base$images/atlas_logo_small.png" width="40px" height="40px"/>
      </a>
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="$page.base$index.html">
            <span style="font-size: 1.8em;">Atlas</span>
          </a>
        </li>
      </ul>

      <button type="button" class="btn btn-outline-light" data-toggle="modal" data-target="#search-modal">
        <span class="fa fa-search"></span>
      </button>
    </header>

    <div id="search-modal" class="modal" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <form style="min-width: 100%">
              <input class="form-control form-control-sm" id="search" type="text" autocomplete="off">
            </form>
          </div>
          <div class="modal-body">
            <div id="search-results"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="row flex-xl-nowrap justify-content-md-center">
        <div class="d-none d-lg-block col-lg-2 col-xl-2" id="nav-left">
          $page.groups$
          $page.navigation$
        </div>
        <div class="col-12 col-md-9 col-xl-8 py-md-3" id="content">
          $page.content$

          $if(page.next.html)$
          <div class="nav-next">
          <p><strong>Next:</strong> $page.next.html$</p>
          </div>
          $endif$
        </div>
        <div class="d-none d-xl-block col-xl-2" id="nav-right">
          $page.toc$
        </div>
      </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"
      integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ"
      crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"
      integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm"
      crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/lunr@2.1.6/lunr.js"
      integrity="sha256-U3smMZ6uKxtHEAX38FWHzhjlVgfcm5Xvs0Gp8t3unQk="
      crossorigin="anonymous"></script>
    <script src="$page.base$js/page.js"></script>
    <script>initialize("$page.base$")</script>

    <script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js?lang=scala"></script>
    <script type="text/javascript">jQuery(function(){window.prettyPrint && prettyPrint()});</script>
  </body>
</html>
