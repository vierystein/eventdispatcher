# test_eventdispatcher.py
"""
Tests for EventDispatcher module.
"""

import unittest
from eventdispatcher import EventDispatcher

class TestEventDispatcher(unittest.TestCase):
    """Test cases for EventDispatcher class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EventDispatcher()
        self.assertIsInstance(instance, EventDispatcher)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EventDispatcher()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
