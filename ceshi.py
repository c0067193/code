import unittest
from my_app import app

class SystemMaintenanceScenarioTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def test_check_updates(self):
        response = self.app.get('/check_updates')
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json['status'])
        self.assertIn('updates', response.json)


    def test_monitor_resources(self):
        response = self.app.get('/monitor_resources')
        self.assertEqual(response.status_code, 200)
        self.assertIn('cpu', response.json)
        self.assertIn('memory', response.json)


    def test_handle_failure(self):
        response = self.app.get('/handle_failure')
        self.assertEqual(response.status_code, 200)
        self.assertIn('recovered', response.json['status'])

if __name__ == '__main__':
    unittest.main()
