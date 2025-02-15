"""nd2: A Python library for reading and writing ND2 files."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__author__ = "Talley Lambert"
__email__ = "talley.lambert@gmail.com"
__all__ = [
    "AXIS",
    "BinaryLayer",
    "BinaryLayers",
    "imread",
    "is_supported_file",
    "is_legacy",
    "ND2File",
    "rescue_nd2",
    "structures",
    "__version__",
]


from . import structures
from ._binary import BinaryLayer, BinaryLayers
from ._parse._chunk_decode import rescue_nd2
from ._util import AXIS, is_legacy, is_supported_file
from .nd2file import ND2File, imread
