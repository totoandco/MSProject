import unittest
import flatten_array


class TestFlattenArray(unittest.TestCase):

    def test_flatten_array_case_1(self):
        self.assertEqual([1, 2, 3, 4], flatten_array.flatten_array([[1, 2, [3]], 4]))

    def test_flatten_array_case_2(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                         flatten_array.flatten_array([[1, 2, [3]], 4, [5, 6, 7, [8, [9, 10]]]]))

    def test_flatten_array_wrong_input_1(self):
        with self.assertRaises(ValueError) as context:
            flatten_array.flatten_array('toto')
        self.assertTrue('input should be a list' in str(context.exception))

    def test_flatten_array_wrong_input_2(self):
        with self.assertRaises(ValueError) as context:
            flatten_array.flatten_array([1, 'toto'])
        self.assertTrue('input should contain only integers' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
