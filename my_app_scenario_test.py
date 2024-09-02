import unittest
from my_app import app

class AccessControlScenarioTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def test_admin_access_to_admin_page(self):
        self.app.post('/login', data={'username': 'admin', 'password': 'admin123'})
        response = self.app.get('/admin')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to the admin page', response.data.decode())


    def test_user_access_to_admin_page(self):
        self.app.post('/login', data={'username': 'user', 'password': 'user123'})
        response = self.app.get('/admin')
        self.assertEqual(response.status_code, 403)


    def test_guest_access_to_admin_page(self):
        self.app.post('/login', data={'username': 'guest', 'password': 'guest123'})
        response = self.app.get('/admin')
        self.assertEqual(response.status_code, 403)


    def test_blacklisted_ip_access(self):
        with self.app as c:
            c.environ_base['REMOTE_ADDR'] = '192.168.1.100'
            response = c.get('/home')
            self.assertEqual(response.status_code, 403)


    def test_multiple_failed_logins(self):
        for _ in range(5):
            response = self.app.post('/login', data={'username': 'user', 'password': 'wrongpassword'})
            self.assertIn('Login Failed', response.data.decode())


if __name__ == '__main__':
    unittest.main()
