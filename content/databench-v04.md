Title: Databench v0.4
Date: 2016-09-22
Category: Tech
Tags: JavaScript, Python, data visualization, data analysis
Slug: databench-v04
Summary: New release of Databench that switches the backend from Flask to Tornado, fully supports Python 2 and 3, transpiles ES6 to legacy JavaScript and runs unit tests and coverage on every commit.
Status: published

<img class="image-process-crisp" src="/images/databench_examples.png" alt="screenshot of index page for examples" />

Databench v0.4 is [released](https://github.com/svenkreiss/databench/releases/tag/v0.4.0).
It is a major change from the v0.3 branch. All [documentation](http://databench.trivial.io/),
[examples](https://github.com/svenkreiss/databench_examples) and
[demos](http://databench-examples.trivial.io/) are updated.
Install the new version with

```sh
pip install --upgrade databench
```

Here are the highlights:

* Migrated from **Flask to Tornado** and with that a switch from Jinja2 templates to Tornado templates.
* With that new backend, **Python 2.7, 3.4 and 3.5** are supported.
* The previous version had many dependencies and a major goal of the refactor was to reduce the number of dependencies. This version only depends on **tornado, pyyaml and pyzmq**. Markdown and docutils to support *md* and *rst* readme files are optional.
* A **Datastore** was added. This concept encourages a consistent pattern for state that works with multiple threads and languages (see the new part of the documentation on [data flow](http://databench.trivial.io/en/latest/quickstart.html#data-flow)).
* Front-end code in **ES6** that is transpiled to legacy JavaScript. Also for analysis code, there is built in support for [node_modules](http://databench.trivial.io/en/latest/frontend.html#node-modules).
* **Unit tests run automatically** on every commit. Also the **documentation is built and updated** on every commit. The test coverage of the code is also updated continuously and is currently at 95%. Unit tests always run for Python 2.7, 3.4 and 3.5.

If you want to jump right in, start with the
[documentation](http://databench.trivial.io/) and have a look at some
[examples](https://github.com/svenkreiss/databench_examples).
