# -*- coding: utf-8 -*-

# Import widgets, provisioners and traitlets
from IPython.html import widgets
from IPython.utils import traitlets

from .mixins import InstallerMixin


class {{cookiecutter.widget_stem}}(InstallerMixin, widgets.DOMWidget):
    '''
    A sample widget... with one "real" traitlet, and a bunch of housekeeping
    '''
    # the name of the requirejs module (no .js!)
    _view_module = traitlets.Unicode(
        'nbextensions/{{cookiecutter.pkg_name}}/js/widget_{{cookiecutter.widget_file}}',
        sync=True)

    # the name of the Backbone.View subclass to be used
    _view_name = traitlets.Unicode('{{cookiecutter.widget_stem}}View', sync=True)

    # an actual value, used in the front-end
    value = traitlets.Unicode(sync=True)

    # don't define to automagically find these
    # _view_styles = ['css/{{cookiecutter.widget_stem}}View.css']
