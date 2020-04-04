Title: Pelican 2018
Date: 2018-02-10
Category: Tech
Tags: blog, Pelican
Slug: pelican-2018
Summary: Updates to Pelican and this blog. This is a summary of theme changes, a list of my favorite plugins, and a summary of plugins that I updated to improve this website. It also contains a short discussion of the pelican-plugins repository and its potential consequences for the lacking popularity of individual plugins.
Status: published


<img class="image-process-crisp top" alt="screenshot of this blog" src="/images/pelican_screenshot_Feb2018.png" />

Inspired by Fred Wilson's post about [Owning Yourself](http://avc.com/2018/01/owning-yourself/),
I revived my Pelican blog.
All my website's
[configuration and source files](https://github.com/svenkreiss/svenkreiss.github.io/tree/pelican)
are public as well as
[my modifications to the pure theme](https://github.com/svenkreiss/pure).
Reasons for Pelican compared to hosted solutions:

* content under version control in git
* my usual text editor for content creation
* fully owning content and its exact presentation
* complete customizability, therefore I want Python, therefore Pelican

A cost is that I have to contribute some changes myself:

* [customized Pure theme](https://github.com/svenkreiss/pure): print mode, less author mentions, responsive resizing for mobile, using the pygments `friendly` style for code highlighting
* `pelican_jsmath`: using KaTeX: nothing existed to combine it with Pelican and so I created
  [pelican-jsmath](https://github.com/svenkreiss/pelican-jsmath).
  The new plugin is $\alpha\omega\epsilon s \sigma m \epsilon$ and described in a separate
  [blog post]({filename}/pelican-jsmath.md).
* `pelican-cite`: create a nicely formatted Bibliography from a bibtex file. I created [PR#5](https://github.com/cmacmackin/pelican-cite/pull/5) so that it also works on draft pages.
* `image_process`: Responsive images (smaller images on smaller devices) are
  especially important for the [projects](/projects.html) page and on article index page.
  The plugin works on all generated files just before they are written, so you can use it everywhere in your theme as well.
* `pelican-advance-embed-tweet`: submitted [PR#2](https://github.com/fundor333/pelican-advance-embed-tweet/pull/2) to remove align attribute from `<bockquote>` which is not HTML5, and you can instead set `TWITTER_ALIGN = 'center'` in your `pelicanconf` to center the embedded tweet.
* `gravatar`: request higher resolution Gravatar images by adding `?s=140` to the image url in the theme
* `related_posts`: newly added to this blog
* `representative_image`: automatically extract an image from an article and use it in article list with `image_process` to thumbnail
* `pelican_dynamic`: adds options to add per article custom `css` and `js`

Open and in-progress issues:

* hack of the day: make your default status `draft` (generally a good idea), but then set the default status in `publishconf.py` to `hidden`. When trying to publish, `hidden` will create an error and the file will be skipped. So the article wont exist on the web at all until its status is set to `draft`. Problem: have to split `OUTPUTDIR` in the Makefile so that two different directories are used for `make devserver` and `make publish` (filed [issue#2284](https://github.com/getpelican/pelican/issues/2284) against Pelican; see [Makefile](https://github.com/svenkreiss/svenkreiss.github.io/blob/pelican/Makefile)).
* Have to wrap Tweet embeds in `<div>` to avoid Markdown's `<p>` tag because the embedded tweet includes a `<blockquote>` which cannot appear inside a `<p>` tag.

Always validate html with [html5validator](https://github.com/svenkreiss/html5validator)
and check links with the [W3C Link Checker](https://validator.w3.org/checklink).

## Pelican Plugins

Most Pelican Plugins are distributed through the central
[pelican-plugins](https://github.com/getpelican/pelican-plugins) repository.
The contributed plugins have fairly little recognition: `render_math` has 65 stars and
`image_process` has 10 stars. Issues against individual plugins are filed
in the central repository and not against the individual plugins. Updates to
plugins have to wait for inclusion in the central repository before they become
used by others.

<!-- <div>@svenkreiss/status/960716731059785730</div> -->

Python provides its standard mechanism with `pip`, `setuptools`, `requirements.txt`, etc.
to manage dependencies. Plugins can be written to support `pip` and Pelican
does support importable plugins. This also allows unit tests and continuous
integration to ensure the quality of the plugin.
This is the method I chose for [pelican-jsmath](https://github.com/svenkreiss/pelican-jsmath).
