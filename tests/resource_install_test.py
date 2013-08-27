import unittest
import os
import shutil

import sys
sys.path.insert(0, '../..')

import chzip # this is __init__.py


class ResourceInstallTestCase(unittest.TestCase):
    def setUp(self):
        self._download_dir = os.path.join(os.path.dirname(__file__, 'resources'))
        os.makedirs(self._download_dir)

    def tearDown(self):
        # Recursive delete
        shutil.rmtree(self._download_dir)

    def test_download_and_unpack(self):
        chzip.download_and_unpack()
