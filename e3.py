import types
from pathlib import Path
def load(path):
    with open(path) as file:
        ret = types.ModuleType(Path(path).stem)
        exec(file.read(), ret.__dict__)
    return ret

