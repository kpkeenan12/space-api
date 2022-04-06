from io import TextIOWrapper
from os.path import dirname
import unittest

from app import app

class EndpointTests(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.dir = dirname(__file__)
    
    def test_can_post_cdm_file(self):
        with open("{0}/sample_files/example_cdm.txt".format(self.dir), "rb") as cdm_file:
            response = self.app.post("/cdm", data={"file": cdm_file})
            self.assertEqual(response.status_code, 202)
