import unittest
from carelib import cosine_similarity

class Test_Cosine_Similarity(unittest.TestCase):
    def test_same_vectors(self):
        """Test that identical vectors have a cosine similarity of 1.0"""
        v1 = [1, 0, 0]
        v2 = [1, 0, 0]
        self.assertAlmostEqual(cosine_similarity(v1, v2), 1.0, places=6, msg="Identical vectors should have a cosine similarity of 1.0")

    def test_orthogonal_vectors(self):
        """Test that perpendicular vectors have a cosine similarity of 0.0"""
        v1 = [1, 0]
        v2 = [0, 1]
        self.assertAlmostEqual(cosine_similarity(v1, v2), 0.0, places=6, msg="Perpendicular vectors should have a cosine similarity of 0.0")

    def test_opposite_vectors(self):
        """Test that opposite vectors have a cosine similarity of -1.0"""
        v1 = [1, 0]
        v2 = [-1, 0]
        self.assertAlmostEqual(cosine_similarity(v1, v2), -1.0, places=6, msg="Opposite vectors should have a cosine similarity of -1.0")

    def test_random_vectors(self):
        """Test cosine similarity calculation with arbitrary vectors"""
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        # Calculate expected value using the formula: (v1·v2) / (||v1|| * ||v2||)
        expected = (1*4 + 2*5 + 3*6) / (((1**2 + 2**2 + 3**2) ** 0.5) * ((4**2 + 5**2 + 6**2) ** 0.5))
        self.assertAlmostEqual(cosine_similarity(v1, v2), expected, places=6, msg="Random vectors should have a cosine similarity of 0.97463")

if __name__ == '__main__':
    unittest.main()