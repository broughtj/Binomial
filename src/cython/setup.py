from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_modules=[Extension("binom", sources=["binom.pyx"], language="c++",)]

setup(ext_modules=cythonize(ext_modules))
