import sys
from os.path import dirname, abspath

print(sys.path.insert(0, dirname(dirname(dirname(abspath(__file__))))))