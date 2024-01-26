import os
import logging
from pylib import __version__

__author__ = "ckir"
__copyright__ = "ckir"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

def find_parent_folder(parent = '.venv'):
    current_dir = os.path.abspath(os.path.dirname(__file__))  # Get the absolute path of the script folder
    while True:
        if parent in os.listdir(current_dir):  # Check if the 'parent' folder exists in the current directory
            return os.path.basename(current_dir)  # Return the base name of the current directory
        if os.path.dirname(current_dir) == current_dir:  # Check if we have reached the root directory
            return None  # Return None if 'parent folder is not found
        current_dir = os.path.dirname(current_dir)  # Move up to the parent directory

