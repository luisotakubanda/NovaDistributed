# test_novadistributed.py
"""
Tests for NovaDistributed module.
"""

import unittest
from novadistributed import NovaDistributed

class TestNovaDistributed(unittest.TestCase):
    """Test cases for NovaDistributed class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaDistributed()
        self.assertIsInstance(instance, NovaDistributed)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaDistributed()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
