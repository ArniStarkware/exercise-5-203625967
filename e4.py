import contextlib
import sys
import os
@contextlib.contextmanager
def in_directory(path):
    original = os.getcwd()
    os.chdir(path)
    yield 
    os.chdir(original)
