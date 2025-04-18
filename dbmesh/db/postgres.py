from dbmesh.db.base import DBConfig
from typing import Dict, Any, List
from pydantic import Field

class PostgresManager(DBConfig):
    """PostgreSQL specific configuration."""
    
    host: str = Field(default="localhost", description="Database host")
    port: int = Field(default=5432, description="Database port") 
    username: str = Field(default="postgres", description="Database username")
    password: str = Field(default="password", description="Database password")
    database: str = Field(default="dbmesh", description="Database name")

    class Config:
        env_prefix = "POSTGRES_"
        env_file = ".env"
        case_sensitive = False

    def setup_connection(self) -> None:
        """Initialize and setup the database connection."""
        import psycopg2
        try:
            self.connection = psycopg2.connect(**self.get_connection_params())
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            raise Exception(f"Failed to connect to PostgreSQL database: {e}")

    def close_connection(self) -> None:
        """Close the database connection."""
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()

    def get_tools(self) -> List[Dict[str, Any]]:
        """Get list of available PostgreSQL tools/operations."""
        return []

    def get_resources(self) -> List[Dict[str, Any]]:
        """Get list of available PostgreSQL resources."""
        return []

    def get_prompts(self) -> List[Dict[str, Any]]:
        """Get list of available PostgreSQL prompts/templates."""
        return []

    def get_connection_url(self) -> str:
        """Get PostgreSQL connection URL."""
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

    def get_connection_params(self) -> Dict[str, Any]:
        """Get PostgreSQL connection parameters."""
        return {
            "host": self.host,
            "port": self.port,
            "user": self.username,
            "password": self.password,
            "database": self.database
        }