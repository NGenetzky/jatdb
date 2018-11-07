#!/usr/bin/env python

import connexion

from jatdb_server import encoder
from jatdb_server.data.tinydb_handler import DbApp

def setup():
    db = DbApp()
    db.initalize()

def main():
    setup()
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'jatdb'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
