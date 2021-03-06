# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os

# BASE DIRECTORY
from gui import BASE_DIR

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings


# APP THEMES
# ///////////////////////////////////////////////////////////////

class Themes:
    """Themes is a class that contains a list of themes and a list of colors"""

    # LOAD SETTINGS
    # ///////////////////////////////////////////////////////////////
    setup_settings = Settings()
    _settings = setup_settings.items

    # APP PATH
    # ///////////////////////////////////////////////////////////////
    json_file = f"themes\\{_settings['theme_name']}.json"
    settings_path = os.path.normpath(os.path.join(BASE_DIR, json_file))
    if not os.path.isfile(settings_path):
        print(f"WARNING: \"gui/themes/{_settings['theme_name']}.json\" not found! check in the folder {settings_path}")

    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        """The function is a constructor that initializes the class Themes"""
        super(Themes, self).__init__()

        # DICTIONARY WITH SETTINGS
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
