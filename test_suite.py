#!/usr/bin/env python3
# -*- coding: utf-8 -*

import unittest
import os
import shutil
import sqlite3

import chzip


class ResourceInstallTestCase(unittest.TestCase):
    def setUp(self):
        self._download_dir = os.path.join(os.path.dirname(__file__),
                                          '__tmp_res')
        os.makedirs(self._download_dir)

    def tearDown(self):
        # Recursive delete
        shutil.rmtree(self._download_dir)

    def test_download_and_unpack(self):
        chzip.download_and_unpack_all(self._download_dir)

        db_path = os.path.join(self._download_dir,
                               chzip.zipcodes.ZipCodesDatabase.DEFAULT_FILENAME)
        self.assertTrue(os.path.exists(db_path), 'Database was not created.')
        db_path_size = os.path.getsize(db_path)
        self.assertTrue(db_path_size > 100, 'Database contains no data.')

        # Test imported data
        conn = sqlite3.connect(db_path)
        try:
            cursor = conn.cursor()
            cursor.execute('select * from zipcodes where onrp = 9161')
            conn.commit()

            number_of_results = 0
            for row in cursor:
                number_of_results += 1
                self.assertEqual(row,
                                 (9161, 80, 1920, 'Martigny PF',
                                  'Martigny PostFinance', 'VS'))

            self.assertEqual(number_of_results, 1)
        finally:
            conn.close()


class FindTestCases(unittest.TestCase):
    def setUp(self):
        res_dir = os.path.join(os.path.dirname(__file__),
                               'test_resources')
        self.chzip = chzip.ChZip(res_dir)

    def __find_onrp(self, onrp, localities):
        for locality in localities:
            if locality._onrp == onrp:
                return locality

    def test_zip(self):
        results = self.chzip.find(1003)
        # Should have three results
        self.assertEqual(3, len(results))

        parking_centre = self.__find_onrp(9036, results)

        self.assertEqual(parking_centre._onrp, 9036)
        self.assertEqual(parking_centre._zip_type_number, 80)
        self.assertEqual(parking_centre.zip_type, chzip.common.ZipType.INTERNAL)
        self.assertEqual(parking_centre.zip, 1003)
        self.assertEqual(parking_centre.short_name, 'Lausanne Centre')
        self.assertEqual(parking_centre.long_name, 'Lausanne Parking du Centre')
        self.assertEqual(parking_centre.canton, 'VD')

    def test_equality(self):
        loc1 = chzip.Locality(zip=1234, short_name='this is short',
                              long_name='this is long', onrp=2525, canton='AB',
                              zip_type_number=10)
        loc2 = chzip.Locality(zip=1234, short_name='this is short',
                              long_name='this is long', onrp=2525, canton='AB',
                              zip_type_number=10)
        self.assertEqual(loc1, loc2)


unittest.defaultTestLoader.discover('chzip')
unittest.main()

