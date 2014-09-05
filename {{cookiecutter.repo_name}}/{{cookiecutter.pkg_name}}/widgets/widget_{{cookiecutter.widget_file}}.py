# -*- coding: utf-8 -*-

import os

# Import widgets, provisioners and traitlets
from IPython.html import widgets
from IPython.utils import traitlets

from .mixins import InstallerMixin

class {{cookiecutter.widget_stem}}(InstallerMixin, widgets.DOMWidget):
    '''
    A sample widget... with one "real" traitlet, and a bunch of housekeeping
    '''

    # the name of the Backbone.View subclass to be used
    _view_name = traitlets.Unicode('{{cookiecutter.widget_stem}}View', sync=True)

    # don't define to automagically find these
    # _view_module = 'js/{{cookiecutter.widget_stem}}View.js'
    # _view_styles = ['css/{{cookiecutter.widget_stem}}View.css']

    # an actual value, used in the front-end
    value = traitlets.Unicode(sync=True)

