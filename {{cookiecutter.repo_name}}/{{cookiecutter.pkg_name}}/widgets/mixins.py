import os

from IPython.html.nbextensions import install_nbextension, check_nbextension
from IPython.display import display, Javascript

pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
nbextension = os.path.basename(pkg_path)
static = os.path.join(pkg_path, 'static', nbextension)


class InstallerMixin(object):
    '''
    An opinonated mixin for handling static assets associated with IPython
    widgets
    '''

    def __init__(self, install_assets=False, *args, **kwargs):
        '''
        Each time an instance is created:
        - if the nbextension is not installed...
            - copy all assets in `static` to the current profile's nbextensions
        - automagically load any css
        '''

        if install_assets or not check_nbextension([nbextension]):
            # copy the static files to a namespaced location in `nbextensions`
            install_nbextension(static)

        # magically-named files css/SomeWidgetView.css
        magic_style = os.path.join(static, 'css', '%s.css' % self._view_name)

        styles = getattr(self, '_view_styles', [])
        if os.path.exists(magic_style):
            styles.append('css/%s.css' % self._view_name)
        styles = [
            '/nbextensions/%s/%s' % (nbextension, style)
            for style in styles
        ]

        # tell the front-end to request the assets
        display(Javascript('', css=styles))

        # always call the parent constructor!
        super(InstallerMixin, self).__init__(*args, **kwargs)
