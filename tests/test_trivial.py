import unittest


class TrivialTest(unittest.TestCase):
    """Test passes by default."""

    def test(self):
        assert True


if __name__ == "__main__":
    unittest.main()
