import os
from IPython.html.nbextensions import install_nbextension

# copy the static files to a namespaced location in `nbextensions`
install_nbextension(os.path.join(
    os.path.dirname(__file__), '..', 'static', '{{cookiecutter.pkg_name}}'
))
