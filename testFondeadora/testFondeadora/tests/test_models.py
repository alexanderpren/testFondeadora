from django.test import TestCase

# Create your tests here.

from key.models import Record
from key.controller import get_record_by_key, get_record_by_key_and_version


class TestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        #print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Record("whateverKey", 200)
        Record("whateverKey", 500)
        Record("whateverKey", 600)
        Record("superImportantKey", 1200)
        Record("superImportantKey", 1500)
        Record("whateverKey", 550)

    def test_newest_version_value(self):
        print("Method: test_newest_version_value_equals_for_key_whateverKey_600.")
        record = get_record_by_key("whateverKey")
        self.assertEqual(record['version'], 3)
        self.assertEqual(record['value'], 600)

    def test_get_value_by_key_and_version(self):
        print("Method: test_get_key_whateverKey_and_version_2_value_equal_to_500.")
        record = get_record_by_key_and_version("whateverKey", 2)
        self.assertEqual(record['version'], 2)
        self.assertEqual(record['value'], 500)

    def test_get_value_closest_version(self):
        print("Method: test_get_closest_version.")
        record = get_record_by_key_and_version("whateverKey", 4)
        self.assertEqual(record['version'], 3)
        self.assertEqual(record['value'], 600)
        
    def test_get_superImportantKey(self):
        print("Method: test_get_closest_version.")
        record = get_record_by_key_and_version("superImportantKey", 5)
        self.assertEqual(record['value'], 1500)
        
    def test_get_superImportantKey_version_7(self):
        print("Method: test_get_superImportantKey_version_7.")
        record = get_record_by_key_and_version("superImportantKey", 7)
        self.assertEqual(record['value'], 1500)

