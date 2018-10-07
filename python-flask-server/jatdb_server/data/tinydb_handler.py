import tinydb

from jatdb_server.data.constants import TINYDB_FILE

def get_db():
    return tinydb.TinyDB(TINYDB_FILE)
