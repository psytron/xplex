from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("alias",  ["mesh/models/alias.py"]),
    Extension("mesh",  ["mesh.py"]),
]

setup(
    name = 'Xplex',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
