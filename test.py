import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_predict_endpoint(self):
        input_data = {
            'alcohol': 13.24,
            'malic_acid': 2.59,
            'ash': 2.87,
            'alcalinity_of_ash': 21.0,
            'magnesium': 118.0,
            'total_phenols': 2.8,
            'flavanoids': 2.69,
            'nonflavanoid_phenols': 0.39,
            'proanthocyanins': 1.82,
            'color_intensity': 4.32,
            'hue': 1.04,
            'od280/od315_of_diluted_wines': 2.93,
            'proline': 735.0
        }
        response = self.app.post('/predict', json=input_data)
        data = response.get_json()
        
        print("Response status code:", response.status_code)
        print("Response data:", data)

        self.assertIn('prediction', data)
        self.assertTrue(data['prediction'] in ['Class 0', 'Class 1', 'Class 2'])

if __name__ == '__main__':
    unittest.main()
