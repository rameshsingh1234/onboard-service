#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
# use_plugin("python.unittest")
use_plugin("python.flake8")
# use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('pypi:pybuilder_pytest')
use_plugin('pypi:pybuilder_pytest_coverage')


name = "onboard-service"
default_task = "publish"


@init
def set_properties(project):
    # pass
    project.set_property_if_unset("pytest_coverage_break_build_threshold", 50)

@init
def init(project):
    project.get_property("pytest_extra_args").append("-x")

