# cookiecutter-ipython-widget
An opinionated [Cookiecutter][] template for a maintainable Jupyter/IPython 3.x
widget.

See the [repo][] and the official [IPython Notebook][nb] this is based on.

Use any or all of these features:
- Testing
  - [Travis-CI][] continuous integration: `.travis.yml`
  - [Nose][] unit testing
  - [CasperJS][] integration testing: `<pkg>/tests/test_widgets.py`
- Packaging & Configuration Management
  - [jupyter-pip][] for nbextension installation & development
  - [PyPi][] publishing
  - [Bower][] static JS and CSS (and LESS): `.bowerrc` and `bower.json`
  - [LESS][] compilation to CSS: `<pkg>/static/less`
- Automation
  All chores documented and executable in `notebooks/Automation.ipynb`
  - Generate RST `README` for Github and PyPi from a single notebook
  - Publish to PyPi
  - Run tests
  - Check Python and JS code style

## Get Ready
We'll assume you have done something like this:

```shell
virtualenv ~/venv/ipython-widget-hacking
. ~/venv/ipython-widget-hacking/bin/activate
pip install ipython[notebook] cookiecutter
```

## Usage
Generate an IPython Widget package project:

```shell
cookiecutter https://github.com/bollwyvl/cookiecutter-ipython-widget.git
```

## Next Steps
- Go into the generated directory
- Fire up the notebook
  ```shell
  ipython notebook
  ```
- Load up the `notebooks/Whatever Example` Notebook!
- Develop your great widget!

## Next, Next Steps
- Make your package a repo, push it up to GitHub.
- Add the repo to your Travis CI account.


## Not Exactly What You Want?
Don't worry, you have options:

### Fork This / Create Your Own
If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

- Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.
- It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

### Or Submit a Pull Request
The IPython widget API is new, and will be changing, and tooling will develop.
Let's find some great patterns!

[checklist]: https://gist.github.com/audreyr/5990987
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[CasperJS]: http://casperjs.org/
[jupyter-pip]: https://github.com/jdfreder/jupyter-pip
[bower]: http://bower.io
[less]: http://lesscss.org
[PyPi]: https://pypi.python.org/pypi
[nb]: http://nbviewer.ipython.org/github/ipython/ipython/blob/master/examples/Interactive%20Widgets/Custom%20Widget%20-%20Hello%20World.ipynb
[Nose]: https://nose.readthedocs.org/en/latest/
[ReadTheDocs]: https://readthedocs.org/
[repo]: https://github.com/bollwyvl/cookiecutter-ipython-widget
[Sphinx]: http://sphinx-doc.org/
[Travis-CI]: http://travis-ci.org/
