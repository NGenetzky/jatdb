""" Application context for tinydb
"""
import datetime
import os.path
import tinydb
import uuid

from jatdb_server.encoder import JSONEncoder
from jatdb_server.models.universal_resource import UniversalResource  # noqa: E501
from jatdb_server.models.content_file import ContentFile  # noqa: E501

# TODO: Respect XDG_DATA_HOME and XDG_CONFIG_HOME
CONFIG_HOME = os.path.expanduser("~/.config/jatdb")
DATA_HOME = os.path.expanduser("~/.local/share/jatdb")

def touch_universal_resource(uri):
    if uri.uuid is None:
        # uri must have uuid to be valid
        uri.uuid = uuid.uuid1()
    # date is updated whenever it is touched
    uri.date = datetime.datetime.utcnow()

class DbApp(object):
    def __init__(self, configdir=CONFIG_HOME, datadir=DATA_HOME):
        self._configdir = configdir
        self._datadir = datadir
        self._db = None

    def initalize(self):
        for dir_ in [self._datadir, self._configdir]:
            if not os.path.isdir(dir_):
                os.makedirs(dir_)

    @property
    def db(self):
        """ Database

        :return: The tinydb database
        :rtype: tinydb.TinyDB
        """
        if self._db is None:
            self._db = self._create_db()
        return self._db

    def _create_db(self):
        dbpath = os.path.join(self._datadir, 'db.json')
        return tinydb.TinyDB(dbpath, cls=JSONEncoder)

    def post_uri(self, uri):
        """ POST UniversalResource
        """
        table = self.db.table('jatdb.universal_resource')

        query = tinydb.Query()
        docs = table.search(query.uri == uri.uri)

        if len(docs) is 0: # Doesn't exist yet.
            touch_universal_resource(uri)
            data = uri.to_dict()
            table.insert(data)
            docs = table.search(query.uri == uri.uri)
        elif len(docs) is not 1:
            raise Exception('There should never be more than one doc!')

        rv = UniversalResource.from_dict(docs[0])

        return rv

    def post_content(self, contentfile):
        """ POST ContentFile
        """
        table = self.db.table('jatdb.content_file')

        query = tinydb.Query()
        docs = table.search(query.path == contentfile.path)

        if len(docs) is 0: # Doesn't exist yet.
            data = contentfile.to_dict()
            table.insert(data)
            docs = table.search(query.path == contentfile.path)
        elif len(docs) is not 1:
            raise Exception('There should never be more than one doc!')

        rv = ContentFile.from_dict(docs[0])

        return rv
