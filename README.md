# DEPRECATED

Use the new, spiffy, official [https://github.com/jupyter/widget-cookiecutter](widget-cookiecutter) instead!

# cookiecutter-ipython-widget
Cookiecutter template for an IPython 2.x (stable) widget.

> For IPython (master) 3.x, see the [v3.0 branch](https://github.com/bollwyvl/cookiecutter-ipython-widget/tree/v3.0)!

See the [repo](https://github.com/bollwyvl/cookiecutter-ipython-widget) and the official [IPython Notebook](http://nbviewer.ipython.org/github/ipython/ipython/blob/2.x/examples/Interactive%20Widgets/Custom%20Widgets.ipynb) this is based on.

- Free software: BSD license
- Vanilla testing setup with `unittest` and `python setup.py test`
- [Travis-CI][]: Ready for Travis Continuous Integration testing
- [Tox][] testing: Setup to easily test for Python 2.6, 2.7, 3.3
- [Sphinx][] docs: Documentation ready for generation with, for example, [ReadTheDocs][]

## Get Ready
We'll assume you have done something like this:

```shell
virtualenv ~/venv/ipython-widget-hacking
. ~/venv/ipython-widget-hacking/bin/activate
pip install ipython[all] cookiecutter 
```

## Usage
Generate a Python package project:

```shell
cookiecutter https://github.com/bollwyvl/cookiecutter-ipython-widget.git
```

## Important things to note/Gotchas

> TODO: These need to be developed in more detail!

- Copying assets
- Loading the JavaScript and CSS
- Namespacing
- Linting

## Next Steps
- Go into the generated directory and run
  ```shell
  python setup.py develop`
  ```
- Fire up the notebook
  ```shell
  ipython notebook
  ```
- Try out the `Whatever Example` Notebook! 
- Create a repo and put it there.
- Add the repo to your Travis CI account.
- Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
- Release your package the standard Python way. Here's a release checklist: https://gist.github.com/audreyr/5990987

## Not Exactly What You Want?
Don't worry, you have options:

### Similar Cookiecutter Templates
- Coming Soon: d3 widget
- Coming Soon: Bower + CoffeeScript + LESS

### Fork This / Create Your Own
If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

- Once you have your own version working, add it to the Similar Cookiecutter Templates list above with a brief description. 
- It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

### Or Submit a Pull Request
The IPython widget API is new, and will be changing, and tooling will develop.
Let's find some great patterns!

[Travis-CI]: http://travis-ci.org/
[Tox]: http://testrun.org/tox/
[Sphinx]: http://sphinx-doc.org/
[ReadTheDocs]: https://readthedocs.org/
