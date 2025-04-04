# DB Mesh
![DB Mesh Architecture](assets/arch.png)

A middleware solution designed to seamlessly connect Large Language Model (LLM) applications and AI Agents with databases using the Model Context Protocol. DB Mesh acts as an intelligent intermediary layer that facilitates secure and efficient database interactions while maintaining context awareness. Key features include:

- Easy configuration through YAML files and environment variables
- Fine-grained access control and permission management
- Intellegent service that creates custom tools based on the database it connects to.

## Overview

DB Mesh provides:
- Seamless integration between LLM applications and various database systems
- Implementation of Model Context Protocol for structured data interactions
- Security and access control layer for database operations
- Context-aware query handling and optimization
- Support for multiple database types and configurations

### Installation

1. Run the docker container with path to the config.yaml file that contains DB credentials or Run the container and add credentials using the UI.




## Configuration File

The main configuration file is `db_config.yaml`, which stores database connection credentials. By default, it is located at:

```
dbmesh/config/db_config.yaml
```

## Default Configuration

When the application starts for the first time, it will create a default configuration file with the following structure:

```yaml
database:
  host: localhost
  port: 5432
  username: postgres
  password: password
  database: dbmesh
```

## Using the Configuration System

The configuration system is implemented in `dbmesh/core/config.py` and provides a singleton instance `db_config` that can be imported and used throughout the application:

```python
from dbmesh.core.config import db_config

# Get current credentials
credentials = db_config.get_credentials()

# Update credentials
new_creds = {
    'host': 'db.example.com',
    'username': 'admin',
    'password': 'secure_password',
    # ... other credentials
}
db_config.update_credentials(new_creds)

# Save changes to the config file
db_config.save_credentials()

# Get a connection string
conn_string = db_config.get_connection_string()
```

## Security Considerations

- The configuration file contains sensitive information. Make sure it is not committed to version control.
- Consider using environment variables for sensitive values in production environments.
- The default configuration is for development purposes only. Always change the default password in production. 
