from importlib.metadata import PackageNotFoundError, version

from .core import read_snowflake, to_snowflake

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"
