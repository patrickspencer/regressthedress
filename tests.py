import unittest
import numpy

# from wombat.engine.predict_price import get_predicted_value
from wombat.engine.one_hot_funcs import one_hot_form_input
from wombat.engine import Prediction

class TestStringMethods(unittest.TestCase):

    def test_one_hot_form_input(self):
        brand = 'Tibi'
        item_type = 'dresses'
        cost = 300
        title = 'lurex evening dress'
        sample = one_hot_form_input(brand = brand, item_type = item_type, est_price = cost, title = title)
        self.assertEqual(sample['cost'], 300)
        self.assertEqual(sample['dresses'], 1)
        self.assertEqual(sample['Tibi'], 1)
        self.assertEqual(sample['lurex'], 1)

class TestPrediction(unittest.TestCase):

    def test_prediction(self):
        brand = 'Tibi'
        item_type = 'dresses'
        cost = 300
        title = 'lurex evening dress'
        prediction = Prediction(brand = brand, item_type = item_type, est_price = cost, title = title)
        self.assertEqual(prediction.brand, 'Tibi')
        self.assertEqual(prediction.item_type, 'dresses')
        self.assertEqual(prediction.est_price, 300)
        self.assertEqual(prediction.title, 'lurex evening dress')
        self.assertEqual(prediction.one_hot_array['cost'], 300)
        self.assertEqual(prediction.one_hot_array['dresses'], 1)
        self.assertEqual(prediction.one_hot_array['Tibi'], 1)
        self.assertEqual(prediction.one_hot_array['lurex'], 1)
        # this next one is important. We cannot accidentally change the length of the 
        # input array into the model
        self.assertEqual(prediction.sample_len, prediction.one_hot_array_len)
        self.assertTrue(isinstance(prediction.predicted_price,
            numpy.float64))
        self.assertTrue(prediction.predicted_price>0)

if __name__ == '__main__':
    unittest.main()
