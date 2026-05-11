# test_wiretools.py
"""
Tests for WireTools module.
"""

import unittest
from wiretools import WireTools

class TestWireTools(unittest.TestCase):
    """Test cases for WireTools class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WireTools()
        self.assertIsInstance(instance, WireTools)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WireTools()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
