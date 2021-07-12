# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.builtin.thornado-mini import ThornadoMini as Unpatched
import os


class ThornadoMini(Unpatched):
    patch(
        "https://raw.githubusercontent.com/HPC-Hackathon-Clangers/Cloud-HPC-Hackathon-2021/laura/Applications/MiniApps/thornado-mini/output_dir.patch",
        when="@1.0",
        sha256="8b7c9b30f6b0a43326d24c74ff97e12ae92a89b3dc13189a506a231dc1045e6f",
    )
