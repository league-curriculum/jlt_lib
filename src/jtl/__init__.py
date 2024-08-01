import sys
import os
import inspect

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "jtl_lib"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError


def add_path():
    # Get the path of the file from which this function is called
    calling_file = inspect.stack()[1].filename
    calling_directory = os.path.dirname(os.path.abspath(calling_file))
    
    # Add the directory to sys.path if it's not already there
    if calling_directory not in sys.path:
        sys.path.append(calling_directory)

