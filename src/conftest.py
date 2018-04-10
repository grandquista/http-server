from .server import main

import pytest

from multiprocessing import Process


@pytest.fixture(scope='session', autouse=True)
def server_setup():
    process = Process(target=main)
    yield process.start()
    process.terminate()
