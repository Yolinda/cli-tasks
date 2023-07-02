"""
    APP NAME: CLI Task Manager
"""

## --- IMPORTS --- ###
import argparse
from task_manager import TaskManager
from file_manager import FileManager

## --- Defaults Values --- ##
__app_name__ = "CLI Task Manager"
__version__ = "0.0.1"
__src_list__ = "tasks.txt"
__des_list__ = "done.txt"

## --- CLI Parser --- ##
parser = argparse.ArgumentParser(
        
        ## Define CLI Name
        prog = __app_name__,

    )

## --- Argument Groups --- ##
required = parser.add_argument_group( 
        "Required Arguments" 
    )

## --- Define Arguments --- ##
required.add_argument( 
        "action",
        action = "store", 
        type = str, 
        nargs = "?",
        default = "default"
    )

## --- Get arguments passed by user --- ##
args = parser.parse_args()


## --- Validations --- ##
















# tasks = TaskManager()
# tasks.add(value="YOLINDA")
# files = FileManager()
# files.open_file("test.txt")
# print(files)