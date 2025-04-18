from db.postgres import PostgresManager
from db.example import ExampleManager

DB_CLASS_MANAGER_MAP = {
    "postgres": PostgresManager,
    "example": ExampleManager,
}
class DBManager:
    def __init__(self, server) -> None:
        self._server = server
        self.VALID_DBS = []
        self.setup()
        self.add_all_tools()

    def setup(self):
        available_dbs = ["example"]
        for db_type in available_dbs:
            self.VALID_DBS.append(DB_CLASS_MANAGER_MAP[db_type]())

    def add_all_tools(self):
        for db_config_manager in self.VALID_DBS:
            for tool_fn, name, des in db_config_manager.get_tools():
                self._server.add_tool(tool_fn, name, des)
