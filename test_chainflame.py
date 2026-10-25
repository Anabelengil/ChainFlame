# test_chainflame.py
"""
Tests for ChainFlame module.
"""

import unittest
from chainflame import ChainFlame

class TestChainFlame(unittest.TestCase):
    """Test cases for ChainFlame class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = ChainFlame()
        self.assertIsInstance(instance, ChainFlame)

    def test_run_method(self):
        """Test the run method."""
        instance = ChainFlame()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
