# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyaml(PythonPackage):
    """PyYAML-based python module to produce pretty and readable
       YAML-serialized data."""

    homepage = "https://github.com/mk-fg/pretty-yaml"
    pypi     = "pyaml/pyaml-21.8.3.tar.gz"

    version('21.8.3', sha256='a1636d63c476328a07213d0b7111bb63570f1ab8a3eddf60522630250c23d975')

    depends_on('python@3.5:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-pyyaml', type=('build', 'run'))
