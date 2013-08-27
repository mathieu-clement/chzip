#!/usr/bin/env python3
# -*- coding: utf-8 -*

import chzip # this is __init__.py

import unittest
from chzip.tests.resource_install_test import *


suite = unittest.TestLoader.loadTestsFromModule(chzip.tests)
test_result = unittest.TestResult()
suite.run(test_result)