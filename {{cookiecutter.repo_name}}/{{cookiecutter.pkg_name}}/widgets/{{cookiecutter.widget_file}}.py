# -*- coding: utf-8 -*-

# Impor widget and traitlets
from IPython.html import widgets
from IPython.utils import traitlets
from IPython.display import display, Javascript


class {{cookiecutter.widget_stem}}Widget(widgets.DOMWidget):
    # A sample Widget
    _view_name = traitlets.Unicode('{{cookiecutter.widget_stem}}View', sync=True)
    value = traitlets.Unicode(sync=True)

    def __init__(self, *args, **kwargs):
        # this could be moved into a common base class
        script = '''IPython.load_extensions('%(path)s/%(view)s');''' % {
            'path': '{{cookiecutter.pkg_name}}/js',
            'view': '{{cookiecutter.widget_file}}'
        }
        display(Javascript(script, css=[
            "/nbextensions/{{cookiecutter.pkg_name}}/css/{{cookiecutter.widget_file}}.css"
        ]))
        super({{cookiecutter.widget_stem}}Widget, self).__init__(*args, **kwargs)
