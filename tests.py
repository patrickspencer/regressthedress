import unittest

# from wombat.engine.predict_price import get_predicted_value
from wombat.engine.one_hot_funcs import one_hot_form_input

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

if __name__ == '__main__':
    unittest.main()
