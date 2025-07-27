# test_nexustools.py
"""
Tests for NexusTools module.
"""

import unittest
from nexustools import NexusTools

class TestNexusTools(unittest.TestCase):
    """Test cases for NexusTools class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NexusTools()
        self.assertIsInstance(instance, NexusTools)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NexusTools()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
