import argparse
import os.path
from collections import namedtuple
from glob import glob
from typing import List
from argparse import Namespace
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from .config import EXCLUDED_LINKS, MKDOCS_SITE_DIRECTORY, OLD_SITE_PREFIX
from .logconfig import setup_logging

logger = setup_logging(__name__)


LinkStatus = namedtuple('LinkStatus', ['old_site_links', 'bare_links', 'bad_links'])


def parse_args() -> Namespace:
    parser = argparse.ArgumentParser('get discovery information')
    parser.add_argument('--title', type=str, help=f'check links on matching page title')
    parser.add_argument('--fname', type=str, help=f'check links on matching file name')
    return parser.parse_args()


def html_files() -> List[str]:
    if not os.path.isdir('site'):
        raise FileNotFoundError('mkdocs site directory not found')

    files = glob(f'{MKDOCS_SITE_DIRECTORY}/**/*.html', recursive=True)
    logger.info(f'found {len(files)} html files in mkdocs site directory')

    return files


def read_file(fname: str) -> str:
    with open(fname) as f:
        return f.read()


def skip_link(link: Tag) -> bool:
    if link['href'] in EXCLUDED_LINKS:
        return True
    elif 'class' not in link.attrs:
        return False
    elif 'headerlink' in link['class']:
        return True
    elif True in [True for c in link['class'] if c.startswith('md-')]:
        return True
    else:
        return False


def html_links(soup: BeautifulSoup) -> List[Tag]:
    links: List[Tag] = []

    for link in soup.find_all('a'):
        if skip_link(link):
            continue
        links.append(link)

    return links


def old_site_link(link: Tag) -> bool:
    if link['href'].startswith(OLD_SITE_PREFIX):
        return True
    else:
        return False


def bare_link(link: Tag) -> bool:
    if link['href'].startswith('http://'):
        return False
    elif link['href'].startswith('https://'):
        return False
    else:
        return True


def bad_link(link: Tag) -> bool:
    try:
        r = requests.get(link['href'], allow_redirects=False)
    except requests.exceptions.ConnectionError:
        return True

    if r.ok:
        return False
    else:
        return True


def check_links(soup: BeautifulSoup) -> LinkStatus:
    links = html_links(soup)

    old_site_links: List[Tag] = []
    bare_links: List[Tag] = []
    bad_links: List[Tag] = []

    for link in links:
        if old_site_link(link):
            old_site_links.append(link)

        if bare_link(link):
            bare_links.append(link)
        elif bad_link(link):
            bad_links.append(link)

    return LinkStatus(old_site_links, bare_links, bad_links)


def link_report(args: Namespace, fname: str) -> None:
    if args.fname and fname != args.fname:
        return

    html = read_file(fname)
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.contents[0]

    if args.title and title != args.title:
        return

    logger.info(f'==== {title}: {fname} ====')

    link_status = check_links(soup)

    if len(link_status.bare_links) > 0:
        logger.warning('BARE LINKS:')

        for link in link_status.bare_links:
            logger.warning(f'  {link}')

    if len(link_status.old_site_links) > 0:
        logger.warning('OLD SITE LINKS:')

        for link in link_status.old_site_links:
            logger.error(f'  {link}')

    if len(link_status.bad_links) > 0:
        logger.error('BAD LINKS:')

        for link in link_status.bad_links:
            logger.error(f'  {link}')


def main():
    args = parse_args()

    if args.fname or args.title:
        logger.info(f'restricted to filename [{args.fname}] or title [{args.title}]')

    for fname in html_files():
        link_report(args, fname)


if __name__ == '__main__':
    main()
