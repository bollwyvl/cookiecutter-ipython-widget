# cookiecutter-ipython-widget
Cookiecutter template for an IPython widget.

See the [repo][] and the official [IPython Notebook][nb] this is based on.

- Free software: BSD license
- [Travis-CI][]: Ready for Travis Continuous Integration testing
  - > TODO: figure out how to plug in to the IPython casper testing
- [Tox][] testing: Setup to easily test for Python 2.6, 2.7, 3.3
- [Sphinx][] docs: Documentation ready for generation with, for example,
 [ReadTheDocs][]

## Get Ready
We'll assume you have done something like this:

```shell
virtualenv ~/venv/ipython-widget-hacking
. ~/venv/ipython-widget-hacking/bin/activate
pip install ipython[all] cookiecutter 
```

## Usage
Generate an IPython Widget package project:

```shell
cookiecutter https://github.com/bollwyvl/cookiecutter-ipython-widget.git \
 -c v3.0
```
> Note: the `-c v3.0` is to ensure that you are getting the version that works 
> with the current master of IPython. Otherwise, you'll get master, which works
> with current stable (2.2)

## Next Steps
- Go into the generated directory
- Fire up the notebook
  ```shell
  ipython notebook
  ```
- Load up the `Whatever Example` Notebook!
- Develop your great widget!

## Next, Next Steps
- Make your package a repo, push it up to GitHub.
- Add the repo to your Travis CI account.
- Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
- Release your package the standard Python way. Here's a [checklist][]. 
  

## Not Exactly What You Want?
Don't worry, you have options:

### Similar Cookiecutter Templates
- Coming Soon: d3 widget
- Coming Soon: Bower + CoffeeScript + LESS

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

[repo]: https://github.com/bollwyvl/cookiecutter-ipython-widget
[nb]: http://nbviewer.ipython.org/github/ipython/ipython/blob/master/examples/Interactive%20Widgets/Custom%20Widget%20-%20Hello%20World.ipynb
[Travis-CI]: http://travis-ci.org/
[Tox]: http://testrun.org/tox/
[Sphinx]: http://sphinx-doc.org/
[ReadTheDocs]: https://readthedocs.org/
[checklist]: https://gist.github.com/audreyr/5990987
