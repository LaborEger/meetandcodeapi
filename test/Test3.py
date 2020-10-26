import requests
import unittest

class Test3(unittest.TestCase):
    true_statement = -1

    def setUp(self):
        self.base_url = 'http://localhost:8080'
    
    def get_statements(self):
        for index in range(3):
            response = requests.get(self.base_url + '/statement/' + str(index))
            body = response.json()
            if 'istrue' in body:
                if body['istrue']:
                    self.true_statement = index

    def test_guess_valid(self):
        self.get_statements()
        body = {
            'from': 'Test Bot',
            'truestatement': self.true_statement
        }
        response = requests.post(self.base_url + '/guess', None, body)
        self.assertEqual(response.status_code, 200, 'A státusz kód nem 200.')
        response_body = response.json()
        self.assertIn('message', response_body, 'Hiányzik a message mező.')
        self.assertEqual(response_body['message'], 'Helyes tipp, felvettelek a barátaim közé.')

    def test_guess_invalid(self):
        self.get_statements()
        for index in range(3):
            if index != self.true_statement:
                body = {
                    'from': 'Test Bot',
                    'truestatement': index
                }
                response = requests.post(self.base_url + '/guess', None, body)
                self.assertEqual(response.status_code, 400, 'A státusz kód nem 400.')
                response_body = response.json()
                self.assertIn('message', response_body, 'Hiányzik a message mező.')
                self.assertEqual(response_body['message'], 'Sajnálom, nem jó a tipped.')

        
if __name__ == '__main__':
    unittest.main(verbosity=0)
