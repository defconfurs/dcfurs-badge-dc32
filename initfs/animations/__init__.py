## Dynamically import all the python files we can find.
import os
import sys

## Do something to amuse the user while we load animations.
def __loading__(step, total):
    pass

## Dynamically load/generate animation classes.
def __load_classes__():
    pathsplit = __file__.rsplit('/', 1)

    step = 0
    files = os.listdir(pathsplit[0])
    for i in range(len(files)):
        __loading__(i, len(files))

        filename = files[i]
        if filename[:2] == "__":
            continue
        
        # Files ending in .py should contain scripted animations.
        if filename[-3:] == ".py":
            classname = filename[:-3]
            try:
                print("Loading scripted animation from " + filename)
                mod = __import__("animations." + classname, globals(), locals(), (classname))
                globals()[classname] = getattr(mod, classname)
            finally:
                pass

__load_classes__()

## Return a list of all animation classes
def all():
    results = []
    module = sys.modules['animations']
    for name in dir(module):
        x = getattr(module, name)
        if isinstance(x, type) and name[:2] != "__":
            results.append(x)
    return results
