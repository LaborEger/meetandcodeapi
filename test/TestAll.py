import requests
import unittest

class TestAll(unittest.TestCase):
    true_statement = -1

    def setUp(self):
        self.base_url = 'http://localhost:8080'
    
    def test_hello(self):
        response = requests.get(self.base_url + '/')
        self.assertEqual(response.status_code, 200)
        body = response.json()
        print ('Válasz kód: ' + str(response.status_code))
        print ('Válasz üzenet: ' + str(body))
        self.assertIn('name', body, 'Hiányzik a name')
        self.assertIn('statements', body, 'Hiányzik a statements')
        self.assertEqual(len(body['statements']), 3, 'A statements nem 3 elemet tartalmaz.')
    
    def test_statements(self):
        for index in range(3):
            response = requests.get(self.base_url + '/statement/' + str(index))
            self.assertEqual(response.status_code, 200)
            body = response.json()
            print ('Válasz kód: ' + str(response.status_code))
            print ('Válasz üzenet: ' + str(body))
            self.assertIn('statement', body)
            self.assertIn('istrue', body)
            if 'istrue' in body:
                if body['istrue']:
                    self.true_statement = index
        self.assertGreater(self.true_statement, -1, 'Egyik állításra sincs beállítva, hogy igaz')
    
    def test_statement_not_found(self):
            response = requests.get(self.base_url + '/statement/3')
            self.assertEqual(response.status_code, 404)
            response = requests.get(self.base_url + '/statement/4')
            self.assertEqual(response.status_code, 404)
        
    def test_guess_valid(self):
        self.test_statements()
        body = {
            'from': 'Test Bot',
            'truestatement': self.true_statement
        }
        response = requests.post(self.base_url + '/guess', None, body)
        self.assertEqual(response.status_code, 200)
        response_body = response.json()
        print ('Válasz kód: ' + str(response.status_code))
        print ('Válasz üzenet: ' + str(response_body))
        self.assertIn('message', response_body)
        self.assertEqual(response_body['message'], 'Helyes tipp, felvettelek a barátaim közé.')

    def test_guess_invalid(self):
        self.test_statements()
        for index in range(3):
            if index != self.true_statement:
                body = {
                    'from': 'Test Bot',
                    'truestatement': index
                }
                response = requests.post(self.base_url + '/guess', None, body)
                self.assertEqual(response.status_code, 400)
                response_body = response.json()
                print ('Válasz kód: ' + str(response.status_code))
                print ('Válasz üzenet: ' + str(response_body))
                self.assertIn('message', response_body)
                self.assertEqual(response_body['message'], 'Sajnálom, nem jó a tipped.')

if __name__ == '__main__':
    unittest.main(verbosity=0)
