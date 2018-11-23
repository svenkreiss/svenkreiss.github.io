Title: Python at a University Lab
Date: 2018-11-23
Category: Science
Tags: Python, Machine Learning
Slug: lab-python
Summary: List of useful Python resources for starting in a university machine learning lab.
Status: published


_I am a post-doc at [VITA lab at EPFL university](https://vita.epfl.ch/)._

Good software engineering practices are important to me. They are foundational
for open and reproducible science. You -- a current or future
member of a Machine Learning lab -- are not necessarily expected to be a computer scientist
or software engineer, but the tools must be familiar.
Expert-level familiar. You will use these tools most of the day.
You should not be clumsy with or afraid of these tools.
Below is an ambitious list, so don't worry if you are not familiar with most of it yet.

__Python Core:__
The best way to get started and a great resource for advanced users is
the [tutorial on the official Python webpage](https://docs.python.org/3/tutorial/index.html).
Here are my notes more specific to ML.

* always use Python3 now, not Python2
* read Python code of great projects outside of ML (almost no ML projects are written well, see closing remarks):
  start with [`requests`](https://github.com/requests/requests)
* Python core and standard libraries (always available, so use them):
    * [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
    * [classes](https://docs.python.org/3/tutorial/classes.html):
      when your function becomes too long it might want to be a class
    * [sets](https://docs.python.org/3/tutorial/datastructures.html#sets):
      avoid testing whether an element is in a list, test whether it is in a set
    * [argparse](https://docs.python.org/3/library/argparse.html), use a standard library to parse command line arguments
    * [logging](https://docs.python.org/3/library/logging.html#module-logging)
    * [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict)
      for sparse accumulators
    * generators and `yield`, see [functional programming howto](https://docs.python.org/3/howto/functional.html)
    * all [`itertools`](https://docs.python.org/3/library/itertools.html)
      (e.g.&nbsp;[`itertools.chain.from_iterable`](https://docs.python.org/3/library/itertools.html#itertools.chain.from_iterable))
    * [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache) is a powerful tool
    * [`property` decorator](https://docs.python.org/3/library/functions.html#property) is great for adding caches
    * more advanced but useful: context managers, decorators
* understand stack traces (the basics: the line above is where the line below originated), [Wikipedia](https://en.wikipedia.org/wiki/Stack_trace)
* scientific foundational packages:
  [`numpy`](http://www.numpy.org/),
  [`scipy`](https://scipy.org/getting-started.html),
  [`scikit-learn`](https://scikit-learn.org/stable/)
  and depending on your focus [`cython`](https://cython.org/)

__Packaging:__
As soon as you need to re-use code in a second file, you will want to import
one of your own files. You should use relative imports and to use those
properly you need to package your code. Packaging in Python used to be a mess,
but much progress has been made over recent years.
When you  search for help related
to packaging, filter for results within the last year.

* `pip`, I have never used `conda`
* relative imports: see [tutorial section on Modules](https://docs.python.org/3/tutorial/modules.html)
* `setup.py`: see [`setuptools` basic use](https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use)
* [`venv`](https://docs.python.org/3/tutorial/venv.html): I never do anything outside a virtual environment
* [Jupyter notebooks](https://github.com/jupyter/notebook):
  Great for demos and log books. _Never_ to code.
* [mybinder.org](https://mybinder.org/) to make your Jupyter demos interactive

__Style / Unit Tests / Continuous Testing:__
Standard practices for software engineers are useful for ML projects, too. They help.
Beyond testing code, unit tests in combination with continuous integration give
a robust and reproducible starting point for anyone picking up your project
(including yourself in one year).

* [PEP8](https://www.python.org/dev/peps/pep-0008/) is the _Style Guide for Python_ and contains explanations. Don't skip [_A Foolish Consistency is the Hobgoblin of Little Minds_](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds). Still, I follow almost all of PEP8 to the letter. Additional:
    * no abbreviations for variables, classes, functions, etc.
    * do not iterate over indices in Python: don't do `for i in range(len(mylist))`
* [`pylint`](https://www.pylint.org/) generally provides good advice beyond checking for PEP8
* [`pytest`](https://docs.pytest.org/en/latest/) to run all your tests
* [CircleCI](https://circleci.com/) and [TravisCI](https://travis-ci.org/) can automatically run your tests on every commit to git

__Red Flags:__
When browsing open source code, this is when I get worried.

* no eval metrics/scripts for that implementation
* have to change the `PATH` or `PYTHONPATH` variables
* have to copy or symlink folders with code

__Closing:__
Infrastructures at large companies are different from a university lab and
your laptop: containers, distributed storage, build systems, custom DNS,
mono repositories. A small piece in the middle of the stack is open source and
has been duct-taped to make it work without the rest of the infrastructure.
Don't follow blindly what seems like a standard practice of the best software
engineers in the world. It might be an artifact of porting it to the
open source world.

Feedback is welcome on Twitter @svenkreiss.
