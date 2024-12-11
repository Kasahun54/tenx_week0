import unittest
from src.eda import calculate_statistics

class TestEDA(unittest.TestCase):
    def test_calculate_statistics(self):
        test_data = {'GHI': [100, 200, 300]}
        df = pd.DataFrame(test_data)
        stats = calculate_statistics(df, 'GHI')
        self.assertEqual(stats['mean'], 200)

if __name__ == '__main__':
    unittest.main()
