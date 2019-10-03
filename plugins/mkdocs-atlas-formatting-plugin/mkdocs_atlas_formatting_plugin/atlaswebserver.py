import os
import socket
import time
from base64 import b64encode
from contextlib import closing
from io import BytesIO
from subprocess import Popen, PIPE
from typing import Optional, Tuple

import requests
from PIL import Image

from .config import ATLAS_VERSION
from .logconfig import setup_logging

logger = setup_logging(__name__)


class NoopWebserver:
    """Used by Parser and Block, for unit testing."""

    ENCODED = 'iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlE' \
              'QVR42mNkYPhfz0AEYBxVSF+FAP5FDvcfRYWgAAAAAElFTkSuQmCC'
    WIDTH, HEIGHT = 10, 10

    def get_image(self, uri: str) -> Tuple[str, int, int]:
        return f'data:image/png;base64,{self.ENCODED}', self.WIDTH, self.HEIGHT


class AtlasWebServer:
    proc: Optional[Popen] = None

    standalone_jar: str = f'{os.getcwd()}/atlas-standalone.jar'
    standalone_url: str = f'https://github.com/Netflix/atlas/releases/download/v{ATLAS_VERSION}/atlas-standalone-{ATLAS_VERSION}.jar'

    webserver_host: str = '127.0.0.1'
    webserver_port: int = 7101

    base_url: str = f'http://{webserver_host}:{webserver_port}'

    def __new__(cls):
        """Singleton Pattern"""
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        if not self.proc:
            self.download_jar(self.standalone_jar, self.standalone_url)
            self.start_jar(self.standalone_jar, self.webserver_host, self.webserver_port)

    @staticmethod
    def download_jar(jar: str, url: str) -> None:
        """Download the specified Atlas Standalone jar from the GitHub releases page."""

        if os.path.isfile(jar):
            logger.info(f'{jar} exists, skipping download')
            return

        logger.info(f'download {url}')

        r = requests.get(url, stream=True)

        with open(jar, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        logger.info(f'saved {jar}')

    def start_jar(self, jar: str, host: str, port: int) -> None:
        """Start the Atlas Standalone jar and wait for the webserver port to become available."""

        logger.info(f'starting atlas webserver on port {port}')

        self.proc = Popen(['java', '-jar', jar], stdout=PIPE, stderr=PIPE)

        count = 0

        while True:
            with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
                if count > 10:
                    self.proc.terminate()
                    raise ChildProcessError(f'ERROR: failed to access atlas webserver on port {port} after 10s')

                if s.connect_ex((host, port)) != 0:
                    count += 1
                    time.sleep(1)
                else:
                    break

        logger.info(f'webserver startup complete in {count}s, pid={self.proc.pid}')

    def get_image(self, uri: str) -> Tuple[str, int, int]:
        """
        Given an Atlas URI, fetch a PNG image from the running Atlas Standalone server. Encode
        the image as a Base64 string suitable for embedding as a data uri in an image tag.

        :param uri: Atlas URI
        :return: image data uri, image width, image height
        """
        url = self.base_url + uri

        r = requests.get(url)

        if not r.ok:
            logger.error(f'failed to get image: code={r.status_code} text={r.text} url={url}')
            return '<pre>ERROR: failed to get image</pre>', 0, 0

        content_type = r.headers['Content-Type']
        encoded = str(b64encode(r.content), 'utf-8')
        data_uri = f'data:{content_type};base64,{encoded}'

        with BytesIO(r.content) as buffer:
            with Image.open(buffer) as image:
                width, height = image.size

        return data_uri, width, height

    def shutdown(self) -> None:
        self.proc.terminate()
        self.proc.wait()
