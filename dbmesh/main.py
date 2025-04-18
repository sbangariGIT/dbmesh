from dbmesh.server import db_mesh_server

if __name__ == "__main__":
    print("Starting DB_Mesh...")
    db_mesh_server.run(transport="sse")

