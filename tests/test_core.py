from tests.client_base import ClientTestCase

class CoreTestCase(ClientTestCase):
    def test_core_index(self):
        resp = self.client.get('/')
        self.assertTrue('you have reached the core' in resp.get_data(as_text=True))
