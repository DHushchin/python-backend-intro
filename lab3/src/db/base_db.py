import sys
import path

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from config import Config

class BaseDB:
    def __init__(self):
        self.cfg = Config()

    def connect(self):
        pass

    def disconnect(self):
        pass

    def create_table(self):
        pass

