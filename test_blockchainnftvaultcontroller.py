# test_blockchainnftvaultcontroller.py
"""
Tests for BlockchainNFTVaultController module.
"""

import unittest
from blockchainnftvaultcontroller import BlockchainNFTVaultController

class TestBlockchainNFTVaultController(unittest.TestCase):
    """Test cases for BlockchainNFTVaultController class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNFTVaultController()
        self.assertIsInstance(instance, BlockchainNFTVaultController)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNFTVaultController()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
