import requests
import unittest

class Test2(unittest.TestCase):
    true_statement = -1

    def setUp(self):
        self.base_url = 'http://localhost:8080'
    
    def test_statements(self):
        for index in range(3):
            response = requests.get(self.base_url + '/statement/' + str(index))
            self.assertEqual(response.status_code, 200, 'A státusz kód nem 200.')
            body = response.json()
            self.assertIn('statement', body, 'Hiányzik a statement mező.')
            self.assertIn('istrue', body, 'Hiányzik az istrue mező.')
            if 'istrue' in body:
                if body['istrue']:
                    self.assertTrue(self.true_statement == -1, 'Egynél több állításra is igaz van beállítva.')
                    self.true_statement = index
        self.assertGreater(self.true_statement, -1, 'Egyik állításra sincs beállítva, hogy igaz.')
        
    
    def test_statement_not_found(self):
            response = requests.get(self.base_url + '/statement/3')
            self.assertEqual(response.status_code, 404, 'A státusz kód nem 404.')
            response = requests.get(self.base_url + '/statement/4')
            self.assertEqual(response.status_code, 404, 'A státusz kód nem 404.')
        
if __name__ == '__main__':
    unittest.main(verbosity=0)
