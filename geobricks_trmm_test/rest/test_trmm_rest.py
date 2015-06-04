import unittest
import json
from flask import Flask
from geobricks_trmm.rest.trmm_rest import trmm


class GeobricksTrmmRestTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(trmm, url_prefix='/trmm')
        self.tester = self.app.test_client(self)

    def test_discovery(self):
        response = self.tester.get('/trmm/discovery/', content_type='application/json')
        out = json.loads(response.data)
        self.assertEquals(out['name'], 'TRMM')
        self.assertEquals(out['type'], 'DATASOURCE')

    def test_list_years(self):
        response = self.tester.get('/trmm/', content_type='application/json')
        out = json.loads(response.data)
        self.assertEquals(len(out), 18)

    def test_list_months(self):
        response = self.tester.get('/trmm/2014/', content_type='application/json')
        out = json.loads(response.data)
        self.assertEquals(len(out), 12)

    def test_list_days(self):
        response = self.tester.get('/trmm/2014/2/', content_type='application/json')
        out = json.loads(response.data)
        self.assertEquals(len(out), 28)