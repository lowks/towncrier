# Copyright (c) Amber Brown, 2015
# See LICENSE for details.

"""
Responsible for getting the version and name from a project.
"""

from __future__ import absolute_import, division

import sys

from importlib import import_module

from incremental import Version


def get_version(package_dir, package):

    # Step 1: Try the dumbest and simplest thing that could possibly work.
    # Yes, that means importing it. Call the cops, I don't care.
    sys.path = [package_dir] + sys.path

    try:
        module = import_module(package)
    except ImportError:
        # wups that didn't work
        module = None

    sys.path.pop(0)
    del sys.modules[package]

    # Step 2: uhhhhhhh
    # TBA

    if not module:
        raise Exception("Can't find your project :(")

    version = getattr(module, "__version__", None)

    if not version:
        raise Exception("No __version__, I don't know how else to look")

    if isinstance(version, str):
        return version

    if isinstance(version, Version):
        return version.base()

    if isinstance(version, tuple):
        return ".".join(map(str, version))

    raise Exception(("I only know how to look at a __version__ that is a str, "
                     "an Increment Version, or a tuple. If you can't provide "
                     "that, use the --version argument and specify one."))


def get_project_name(package_dir, package):

    # Step 1: Try the dumbest and simplest thing that could possibly work.
    # Yes, that means importing it. Call the cops, I don't care.
    sys.path = [package_dir] + sys.path

    try:
        module = import_module(package)
    except ImportError:
        # wups that didn't work
        module = None

    sys.path.pop(0)
    del sys.modules[package]

    # Step 2: uhhhhhhh
    # TBA

    if not module:
        raise Exception("Can't find your project :(")

    version = getattr(module, "__version__", None)

    if not version:
        # welp idk
        return package.title()

    if isinstance(version, str):
        return package.title()

    if isinstance(version, Version):
        # Incremental has support for package names
        return version.package
