import os, sys; 

current_dir = os.path.dirname(os.path.realpath(__file__))

sys.path.append(current_dir)
sys.path.append(os.path.dirname(current_dir))