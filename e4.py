import contextlib
import sys
import os
@contextlib.contextmanager
def in_directory(path):
    original = sys.path
    sys.path = [path]
    yield 
    sys.path = original
