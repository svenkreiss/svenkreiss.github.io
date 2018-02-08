Title: pelican-jsmath Plugin
Date: 2018-02-05
Category: Tech
Tags: blog, Pelican, math, Python
Slug: pelican-jsmath
Summary: An $\alpha\omega\epsilon s \sigma m \epsilon$ Pelican plugin to render math in JavaScript libraries like KaTeX.
Status: draft


The new plugin is $\alpha\omega\epsilon s \sigma m \epsilon$, particularly
in combination with KaTeX as on this blog. It has good support for big
equations: $$E=mc^2$$
A vector $\vec{a}$ looks beautiful. Writing
order of magnitudes with $\mathcal{O}(n)$ is pretty. There was a related
[Pelican issue](https://github.com/getpelican/pelican-plugins/issues/625)
for support.


## Packaging

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

If you are converting a plugin from pelican-plugins repository, move your files
into a folder, here `pelican_jsmath`, and add a `setup.py` file. That's it.
You can submit it to pypi if you want, but you can also tell people to install
directly from Github using
`pip install https://github.com/svenkreiss/pelican-jsmath/zipball/master`.

With packaged plugins, you can manage your dependencies in your
`requirements.txt` as usual.
