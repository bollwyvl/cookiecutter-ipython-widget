import os
import time

from IPython.html.nbextensions import install_nbextension
from IPython.display import display, Javascript

pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
nbextension = os.path.basename(pkg_path)
static = os.path.join(pkg_path, 'static', nbextension)

class InstallerMixin(object):
    '''
    An opinonated mixin for handling static assets associated with IPython
    widgets
    '''

    def __init__(self, *args, **kwargs):
        '''
        Each time an instance is created:
        - copy ALL assets in `static` to the current profile's nbextensions
        - ensure that the view module has been required
        
        It also doesn't fix the race condition that can occur from a cell
        output being displayed that uses a widget before it has been required.

        This is inefficient, but can't be better until requirejs is used
        instead of WidgetManager.
        '''

        # copy the static files to a namespaced location in `nbextensions`
        install_nbextension(static)

        # magically-named files js/SomeWidgetView.js and css/SomeWidgetView.css
        magic_module = os.path.join(static, 'js', '%s.js' % self._view_name) 
        magic_style = os.path.join(static, 'css', '%s.css' % self._view_name)

        view_module = None
        if os.path.exists(magic_module):
            view_module =  'js/%s' % self._view_name
        view_module = getattr(self, '_view_module', view_module)
        
        if view_module is None:
            raise NotImplemented('No JavaScript found for %s' % self._view_name)

        styles = getattr(self, '_view_styles', [])
        if os.path.exists(magic_style):
            styles.append('css/%s.css' % self._view_name)
        styles = [
            '/nbextensions/%s/%s' % (nbextension, style)
            for style in styles
        ]

        # tell the front-end to request the assets
        display(
            Javascript('IPython.load_extensions("%s/%s");' % (
                nbextension, view_module
            ), css=styles)
        )

        # always call the parent constructor!
        super(InstallerMixin, self).__init__(*args, **kwargs)
