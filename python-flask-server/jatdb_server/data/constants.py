""" Constants for application data
"""
import os.path

# TODO: Respect XDG_DATA_HOME and XDG_CONFIG_HOME
CONFIG_HOME = os.path.expanduser("~/.config/jatdb")
DATA_HOME = os.path.expanduser("~/.local/share/jatdb")

TINYDB_FILE = os.path.join(DATA_HOME, 'db.json')
