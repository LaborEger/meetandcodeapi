import requests
import unittest

class Test1(unittest.TestCase):
    true_statement = -1

    def setUp(self):
        self.base_url = 'http://localhost:8080'
    
    def test_hello(self):
        response = requests.get(self.base_url + '/')
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIn('name', body, 'Hiányzik a name mező')
        self.assertIn('statements', body, 'Hiányzik a statements mező')
        self.assertEqual(len(body['statements']), 3, 'A statements mező nem 3 elemet tartalmaz.')
    
if __name__ == '__main__':
    unittest.main(verbosity=0)
