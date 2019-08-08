import unittest
import pandas as pd
import numpy as np
import lambdata_ewuerfel66

# Test check_null
class TestCheckNull(unittest.TestCase):

    # Case 1 - no null
    def test_noNull(self):
        # Initialize test DataFrame
        df = pd.DataFrame([[3, 4, 5],
                           [5, 6, 7],
                           [2, 3, 4]])

        # Assert that zero is returned
        self.assertEqual(lambdata_ewuerfel66.check_null(df), 0)

    # Case 2 - one null
    def test_oneNull(self):
        # Initialize test DataFrame
        df = pd.DataFrame([[3, 4, 5],
                           [5, np.nan, 7],
                           [2, 3, 4]])

        # Assert that zero is returned
        self.assertEqual(lambdata_ewuerfel66.check_null(df), 1)

# Test add_column
class TestAddColumn(unittest.TestCase):

    def test_add(self):
        # Initialize test DataFrame
        df = pd.DataFrame([[3, 4, 5],
                           [5, np.nan, 7],
                           [2, 3, 4]])

        # Initialize test list
        lst = [4] * len(df[0])

        # Add test list to test DataFrame
        lambdata_ewuerfel66.add_column('new', lst, df)

        # Check that the last column in the df is the proper series
        self.assertEqual(df['new'][0], pd.Series([4, 4, 4])[0])
        self.assertEqual(df['new'][1], pd.Series([4, 4, 4])[1])
        self.assertEqual(df['new'][2], pd.Series([4, 4, 4])[2])


# Initialize test
if __name__ == '__main__':
    unittest.main()