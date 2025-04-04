import os
import tempfile
import unittest
from unittest.mock import patch, MagicMock
from dbmesh.core.config import DBConfig

class TestDBConfig(unittest.TestCase):
    """Test cases for the DBConfig class."""
    
    def setUp(self):
        """Set up test environment before each test."""
        # Create a temporary directory for test config files
        self.temp_dir = tempfile.mkdtemp()
        self.config_path = os.path.join(self.temp_dir, "test_db_config.yaml")
        
        # Create a test instance with the temporary config path
        self.db_config = DBConfig(config_path=self.config_path)
    
    def tearDown(self):
        """Clean up after each test."""
        # Remove the temporary config file if it exists
        if os.path.exists(self.config_path):
            os.remove(self.config_path)
        
        # Remove the temporary directory
        os.rmdir(self.temp_dir)
    
    def test_get_credentials(self):
        """Test getting current credentials."""
        # Set up test credentials
        test_creds = {
            'host': 'localhost',
            'port': 5432,
            'username': 'test_user',
            'password': 'test_password',
            'database': 'test_db'
        }
        self.db_config.credentials = test_creds.copy()
        
        # Get credentials and verify
        result = self.db_config.get_credentials()
        self.assertEqual(result, test_creds)
        
        # Verify that the returned dict is a copy (not the same object)
        self.assertIsNot(result, self.db_config.credentials)
    
    def test_update_credentials(self):
        """Test updating credentials."""
        # Initial credentials
        initial_creds = {
            'host': 'localhost',
            'port': 5432,
            'username': 'initial_user',
            'password': 'initial_password',
            'database': 'initial_db'
        }
        self.db_config.credentials = initial_creds.copy()
        
        # New credentials to update with
        new_creds = {
            'username': 'updated_user',
            'password': 'updated_password'
        }
        
        # Update credentials
        self.db_config.update_credentials(new_creds)
        
        # Verify that only the specified fields were updated
        expected_creds = initial_creds.copy()
        expected_creds.update(new_creds)
        self.assertEqual(self.db_config.credentials, expected_creds)
    
    def test_save_and_load_credentials(self):
        """Test saving credentials to file and loading them back."""
        # Set up test credentials
        test_creds = {
            'host': 'test_host',
            'port': 5432,
            'username': 'test_user',
            'password': 'test_password',
            'database': 'test_db'
        }
        self.db_config.credentials = test_creds.copy()
        
        # Save credentials to file
        self.db_config.save_credentials()
        
        # Create a new instance to load the saved credentials
        new_db_config = DBConfig(config_path=self.config_path)
        
        # Verify that the loaded credentials match the original
        loaded_creds = new_db_config.get_credentials()
        self.assertEqual(loaded_creds, test_creds)

    
    def test_create_default_config(self):
        """Test creating a default configuration file."""
        # Remove the config file if it exists
        if os.path.exists(self.config_path):
            os.remove(self.config_path)
        
        # Create a new instance to trigger default config creation
        new_db_config = DBConfig(config_path=self.config_path)
        
        # Verify that the config file was created
        self.assertTrue(os.path.exists(self.config_path))
        
        # Verify that the credentials were loaded
        creds = new_db_config.get_credentials()
        self.assertIn('host', creds)
        self.assertIn('port', creds)
        self.assertIn('username', creds)
        self.assertIn('password', creds)
        self.assertIn('database', creds)

if __name__ == "__main__":
    unittest.main() 