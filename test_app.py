import unittest
from app import app


class TestApp(unittest.TestCase):

	def setUp(self):
		print('Test working')
		self.app = app.test_client()
		self.app.testing = True 
		
	def test_endpoint(self):
		result = self.app.get('/')
		print('result', result.get_data())
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result.get_data(), b'200 OK!')



if __name__ == "__main__":
	unittest.main()