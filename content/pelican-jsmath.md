Title: pelican-jsmath Plugin
Date: 2018-02-18
Category: Tech
Tags: blog, Pelican, math, Python
Slug: pelican-jsmath
Summary: An $\alpha\omega\epsilon s \sigma m \epsilon$ Pelican plugin to render math in JavaScript libraries like KaTeX. This plugin makes sure that equations are preserved in the Markdown and Restructured Text parsers and get reproduced properly in HTML for a JavaScript renderer to process.
Status: published


The new plugin is $\alpha\omega\epsilon s \sigma m \epsilon$, particularly
in combination with KaTeX which is used here. It has good support for big
equations: $$E=mc^2$$
A vector $\vec{a}$ looks beautiful. Writing
order of magnitudes with $\mathcal{O}(n)$ is pretty. There was a related
[Pelican issue](https://github.com/getpelican/pelican-plugins/issues/625)
for support for KaTeX.

The plugin is packaged and can be installed with `pip install pelican-jsmath`
(with a dash) and then added to Pelican in `pelicanconf.py` by adding
`'pelican_jsmath'` (with an underscore) to your `PLUGINS` list. See the
[Readme](https://github.com/svenkreiss/pelican-jsmath) for more details.

## Packaging Pelican Plugins

It is great that Pelican supports plugins installed via `pip` and outside the
plugins directory. It gives the plugin author and user more control over the
plugin version. This is why I wanted to document the steps I took to make
`pelican-jsmath` a Python package.

Simplest `setup.py` file:

```python
from setuptools import setup


setup(
    name='pelican-jsmath',
    version='0.1.0',
    description='Pelican Plugin that passes math to JavaScript.',
    url='http://github.com/svenkreiss/pelican-jsmath',
    author='Sven Kreiss',
    author_email='me@svenkreiss.com',
    license='AGPL-3.0',
    packages=['pelican_jsmath'],
)
```

If you are converting a plugin from the pelican-plugins repository, move your files
into a folder, here `pelican_jsmath`, and add a `setup.py` file. That's it.
You can submit it to pypi if you want, but you can also tell people to install
directly from Github using
`pip install https://github.com/svenkreiss/pelican-jsmath/zipball/master`.

With packaged plugins, you can manage your dependencies in your
`requirements.txt` as usual.

## Testing Packaged Plugins

This Pelican plugin includes a plugin for the Python Markdown parser that
modifies the HTML output. It is good to test that this plugin produces valid HTML.
The repository includes an example Pelican site which is regenerated on every
commit and validated with
[html5validator](https://github.com/svenkreiss/html5validator).

## Sample

<img class="image-process-crisp top" alt="pelican-jsmath sample" src="/images/pelican_jsmath_sample.png" />
