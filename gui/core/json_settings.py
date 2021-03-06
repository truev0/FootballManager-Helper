# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os

# BASE DIRECTORY
from gui import BASE_DIR


# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class Settings:
    """The Settings class is a container for all the settings that are used in the app"""

    # APP PATH
    # ///////////////////////////////////////////////////////////////
    json_file = "core\\settings.json"
    settings_path = os.path.normpath(os.path.join(BASE_DIR, json_file))
    if not os.path.isfile(settings_path):
        print(f"WARNING: \"settings.json\" not found! check in the folder {settings_path}")

    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        """The function is a constructor that initializes the class Settings"""
        super(Settings, self).__init__()

        # DICTIONARY WITH SETTINGS
        # Just to have objects references
        self.items = {}

        # DESERIALIZE
        self.deserialize()

    # SERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def serialize(self):
        """It opens a file, writes a json file, and then closes the file"""
        # WRITE JSON FILE
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(self.items, write, indent=4)

    # DESERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def deserialize(self):
        """> Reads a JSON file and loads it into a dictionary"""
        # READ JSON FILE
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            settings = json.loads(reader.read())  # skipcq: PY-W0078
            self.items = settings
