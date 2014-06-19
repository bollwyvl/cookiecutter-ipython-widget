# -*- coding: utf-8 -*-

import os

# Import widgets, provisioners and traitlets
from IPython.html import widgets
from IPython.utils import traitlets

from .mixins import InstallerMixin

class {{cookiecutter.widget_stem}}Widget(InstallerMixin, widgets.DOMWidget):
    '''
    A sample widget... with one "real" traitlet, and a bunch of housekeeping
    '''

    # the name of the Backbone.View subclass to be used
    _view_name = traitlets.Unicode('{{cookiecutter.widget_stem}}View', sync=True)

    # an actual value, used in the front-end
    value = traitlets.Unicode(sync=True)

    # provisioning and loading JS/CSS assets
    _view_static = os.path.join(
        os.path.dirname(__file__), '..', 'static', '{{cookiecutter.pkg_name}}'
    )
    _view_module = 'js/{{cookiecutter.widget_file}}'
    _view_style = 'css/{{cookiecutter.widget_file}}'
