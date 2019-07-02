import unittest
import temp_tracker


class TestTempTracker(unittest.TestCase):

    def test_insert_case_good_input(self):
        t_tr = temp_tracker.TempTracker()
        t_tr.insert(99)
        self.assertEqual(99, t_tr.get_min())

    def test_insert_case_wrong_input(self):
        t_tr = temp_tracker.TempTracker()
        with self.assertRaises(ValueError) as context:
            t_tr.insert('toto')
        self.assertTrue('input should be an integer' in str(context.exception))

    def test_insert_case_out_of_range(self):
        t_tr = temp_tracker.TempTracker()
        with self.assertRaises(ValueError) as context:
            t_tr.insert(199)
        self.assertTrue(
            'out of range, input should be between ' + str(t_tr.min_temp) + ' and ' + str(t_tr.max_temp) in str(
                context.exception))

    def test_insert_case_out_of_range(self):
        t_tr = temp_tracker.TempTracker()
        with self.assertRaises(ValueError) as context:
            t_tr.insert(-2)
        self.assertTrue(
            'out of range, input should be between ' + str(t_tr.min_temp) + ' and ' + str(t_tr.max_temp) in str(
                context.exception))

    def test_get_min_without_values(self):
        t_tr = temp_tracker.TempTracker()
        self.assertEqual(0, t_tr.get_min())
        self.assertEqual(int, type(t_tr.get_min()))

    def test_get_min(self):
        t_tr = temp_tracker.TempTracker()
        t_tr.insert(99)
        t_tr.insert(2)
        self.assertEqual(2, t_tr.get_min())
        self.assertEqual(int, type(t_tr.get_min()))

    def test_get_max_without_values(self):
        t_tr = temp_tracker.TempTracker()
        self.assertEqual(0, t_tr.get_max())
        self.assertEqual(int, type(t_tr.get_max()))

    def test_get_max(self):
        t_tr = temp_tracker.TempTracker()
        t_tr.insert(99)
        t_tr.insert(2)
        self.assertEqual(99, t_tr.get_max())
        self.assertEqual(int, type(t_tr.get_max()))

    def test_get_mean_without_values(self):
        t_tr = temp_tracker.TempTracker()
        self.assertEqual(0.0, t_tr.get_mean())
        self.assertEqual(float, type(t_tr.get_mean()))

    def test_get_max(self):
        t_tr = temp_tracker.TempTracker()
        t_tr.insert(99)
        t_tr.insert(2)
        self.assertEqual(50.5, t_tr.get_mean())
        self.assertEqual(float, type(t_tr.get_mean()))


if __name__ == '__main__':
    unittest.main()
