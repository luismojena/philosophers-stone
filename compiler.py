"""
The purpose of this module is to be executed via `python -m philosophal-proto.compiler ...`
It has several options that can be passed in as parameters to configure the compiler output.
For a more detailed help on the use of the compiler check the documentation or type
`python -m philosophal-proto.compiler -h` on your terminal.
"""
import sys
import os
import types
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
    Base = declarative_base()

    # get the directory where the module is
    filename = sys.argv[1]
    filename_path = os.path.dirname(filename)
    sys.path.extend([filename_path])

    module_file = os.path.basename(filename)
    module = str(module_file.split('.py')[0])

    lib = None
    try:
        lib = __import__(module)
    except ImportError:
        print(sys.exc_info())
        print('se cago')
    else:
        globals()[module] = lib

    if lib is None:
        sys.exit(1)

    # get the declarative clases that come from the declarative.api module in sqlalchemy
    declarative_classes = []
    for key, value in lib.__dict__.items():
        if hasattr(value, '__module__'):
            # change by importing types and use types.FunctionType
            if value.__module__ == 'sqlalchemy.ext.declarative.api' and not isinstance(value, types.FunctionType):
                declarative_classes.append(lib.__dict__[key])

    subclasses_in_module = [subclass for klass in declarative_classes for subclass in klass.__subclasses__() if
                            subclass.__module__ == module]
    print(subclasses_in_module)