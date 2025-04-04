# Loads YAML configs & environment variables
# config.py
import os
import yaml
from typing import Dict, Any, Optional

class DBConfig:
    """Manages database configuration and credentials."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the DB configuration manager.
        
        Args:
            config_path: Path to the YAML config file. If None, uses default path.
        """
        self.config_path = config_path or os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "db_config.yaml")
        self.credentials = {}
        self.load_config()
    
    def load_config(self) -> None:
        """Load database credentials from the config file."""
        try:
            # Create config directory if it doesn't exist
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            
            # Check if config file exists
            if not os.path.exists(self.config_path):
                # Create a default config file
                self._create_default_config()
            
            # Load the config file
            with open(self.config_path, 'r') as f:
                config_data = yaml.safe_load(f)
                
            # Extract database credentials
            self.credentials = config_data.get('database', {})
            
        except Exception as e:
            print(f"Error loading config: {e}")
            # Initialize with empty credentials if loading fails
            self.credentials = {}
    
    def _create_default_config(self) -> None:
        """Create a default configuration file with placeholder values."""
        default_config = {
            'database': {
                'host': 'localhost',
                'port': 5432,
                'username': 'postgres',
                'password': 'password',
                'database': 'dbmesh'
            }
        }
        
        with open(self.config_path, 'w') as f:
            yaml.dump(default_config, f, default_flow_style=False)
    
    def get_credentials(self) -> Dict[str, Any]:
        """Get the current database credentials."""
        return self.credentials.copy()
    
    def update_credentials(self, new_credentials: Dict[str, Any]) -> None:
        """
        Update database credentials in memory.
        
        Args:
            new_credentials: Dictionary containing new credential values.
        """
        self.credentials.update(new_credentials)
    
    def save_credentials(self) -> None:
        """Save the current credentials to the config file."""
        try:
            # Load the entire config file
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as f:
                    config_data = yaml.safe_load(f) or {}
            else:
                config_data = {}
            
            # Update the database section
            config_data['database'] = self.credentials
            
            # Save the updated config
            with open(self.config_path, 'w') as f:
                yaml.dump(config_data, f, default_flow_style=False)
                
        except Exception as e:
            print(f"Error saving config: {e}")
    

# Create a singleton instance for application-wide use
db_config = DBConfig()