import numpy as np

# "python3.8 test_debug.py"    prints Hello
# "python3.8 -O test_debug.py" prints nothing

if __name__ == '__main__':
    if __debug__:
        print('Hello')
