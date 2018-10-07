""" Application context for tinydb
"""
import os.path
import tinydb

# TODO: Respect XDG_DATA_HOME and XDG_CONFIG_HOME
CONFIG_HOME = os.path.expanduser("~/.config/jatdb")
DATA_HOME = os.path.expanduser("~/.local/share/jatdb")

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
        return tinydb.TinyDB(dbpath)
