import os
from racks.rack_starter import start_rack_with_config

os.chdir(os.path.dirname(os.path.abspath(__file__)))

start_rack_with_config(True)
