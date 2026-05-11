# test_bitflow.py
"""
Tests for BitFlow module.
"""

import unittest
from bitflow import BitFlow

class TestBitFlow(unittest.TestCase):
    """Test cases for BitFlow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BitFlow()
        self.assertIsInstance(instance, BitFlow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BitFlow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
