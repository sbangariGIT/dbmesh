from dbmesh.db.base import DBConfig
from typing import Dict, Any, List
from pydantic import Field

class ExampleManager(DBConfig):
    """Excel specific configuration."""

    def setup_connection(self) -> None:
        """Initialize and setup the database connection."""
        return True

    def close_connection(self) -> None:
        """Close the database connection."""
        return True
    
    # This are some example tools
    def add(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b

    def get_tools(self) -> list:
        return [
            (self.add, "add", "Add two numbers")
        ]
    
    def get_resources(self) -> List[Dict[str, Any]]:
        return []

    def get_prompts(self) -> List[Dict[str, Any]]:
        return []