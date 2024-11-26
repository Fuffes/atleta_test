import os
from enum import Enum



MM_EXTENSION_PATH = os.path.abspath("./MetaMask")
USER_DATA_DIR =  "/user_data"

# MM setup
MM_PASSWORD = os.getenv('METAMASK_PASSWORD')
MM_KEY = os.getenv('METAMASK_KEY').split()
