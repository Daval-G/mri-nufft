"""MRI-NUFFT.

MRI-NUFFT provides an easy to use Fourier operator for non-Cartesian
reconstruction.

Doing non-Cartesian MRI has never been so easy.
"""

from .operators import (
    get_operator,
    check_backend,
    list_backends,
)

from .trajectories import (
    initialize_2D_radial,
    initialize_2D_spiral,
    initialize_2D_cones,
    initialize_2D_sinusoide,
    initialize_2D_rosette,
    initialize_2D_rings,
    initialize_2D_polar_lissajous,
    initialize_2D_lissajous,
    initialize_2D_waves,
    initialize_3D_from_2D_expansion,
    initialize_3D_cones,
    initialize_3D_helical_shells,
    initialize_3D_annular_shells,
    display_2D_trajectory,
    display_3D_trajectory,
)

__all__ = [
    "get_operator",
    "check_backend",
    "list_backends",
    "initialize_2D_radial",
    "initialize_2D_spiral",
    "initialize_2D_cones",
    "initialize_2D_sinusoide",
    "initialize_2D_rosette",
    "initialize_2D_rings",
    "initialize_2D_polar_lissajous",
    "initialize_2D_lissajous",
    "initialize_2D_waves",
    "initialize_3D_from_2D_expansion",
    "initialize_3D_cones",
    "initialize_3D_helical_shells",
    "initialize_3D_annular_shells",
    "display_2D_trajectory",
    "display_3D_trajectory",
]


try:
    # -- Distribution mode --
    # import from _version.py generated by setuptools_scm during release
    from ._version import version as __version__
except ImportError:
    # -- Source mode --
    # use setuptools_scm to get the current version from src using git
    from setuptools_scm import get_version as _gv
    from os import path as _path

    __version__ = _gv(_path.join(_path.dirname(__file__), _path.pardir))
