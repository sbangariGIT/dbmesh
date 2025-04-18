from abc import ABC, abstractmethod
from typing import Dict, Any, List

class DBConfig(ABC):
    """
    Abstract base class for database configurations.
    
    This class defines the interface that all database configurations must implement.
    It provides methods for managing database connections, retrieving tools, resources,
    and prompts specific to the database type.
    """
    
    @abstractmethod
    def setup_connection(self) -> None:
        """
        Initialize and setup the database connection.
        Must be implemented by concrete classes.
        """
        raise NotImplementedError

    @abstractmethod 
    def close_connection(self) -> None:
        """
        Close the active database connection.
        Must be implemented by concrete classes.
        """
        raise NotImplementedError

    @abstractmethod
    def get_tools(self) -> List[tuple]:
        """
        Get list of available database tools/operations.
        Must be implemented by concrete classes.
        
        Returns:
            List of tool configurations
        """
        raise NotImplementedError

    @abstractmethod
    def get_resources(self) -> List[Dict[str, Any]]:
        """
        Get list of available database resources.
        Must be implemented by concrete classes.
        
        Returns:
            List of resource configurations
        """
        raise NotImplementedError

    @abstractmethod
    def get_prompts(self) -> List[Dict[str, Any]]:
        """
        Get list of available database prompts/templates.
        Must be implemented by concrete classes.
        
        Returns:
            List of prompt configurations
        """
        raise NotImplementedError