import os

from IPython.html.nbextensions import install_nbextension
from IPython.display import display, Javascript

class InstallerMixin(object):
    '''
    An opinonated mixin for handling static assets associated with IPython
    widgets
    '''

    def __init__(self, *args, **kwargs):
        '''
        This will be called each time an implementing class is instantiated
        '''

        # as a good citizen
        extension = os.path.basename(self._view_static)

        # copy the static files to a namespaced location in `nbextensions`
        install_nbextension(os.path.abspath(self._view_static))

        # this assumes your extension takes care of its own dependencies...
        script = 'IPython.load_extensions("%s/%s");' % (
            extension,
            self._view_module
        )

        # again, assume that you have put the style in the extension's folder
        styles = []
        try:
            styles = ['/nbextensions/%s/%s.css' % (extension, self._view_style)]
        except:
            pass

        # tell the front-end to request the assets
        display(Javascript(script, css=styles))

        # always call the parent constructor!
        super(InstallerMixin, self).__init__(*args, **kwargs)
