##
# Copyright 2012-2016 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
Support for BLACS as toolchain linear algebra library.

@author: Stijn De Weirdt (Ghent University)
@author: Kenneth Hoste (Ghent University)
"""

from easybuild.tools.toolchain.linalg import LinAlg


class Blacs(LinAlg):
    """
    Trivial class, provides BLACS support.
    """
    BLACS_MODULE_NAME = ['BLACS']
    BLACS_LIB = ["blacsCinit", "blacsF77init", "blacs"]
    BLACS_LIB_GROUP = True

    def _set_blacs_variables(self):
        """Skip setting BLACS variables if it is not required (e.g., with recent ScaLAPACK versions)."""
        if self.is_required(self.BLACS_MODULE_NAME[0]):
            super(Blacs, self)._set_blacs_variables()

