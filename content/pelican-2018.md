Title: Pelican 2018
Date: 2018-02-02
Category: Tech
Tags: blog
Slug: pelican-2018
Summary: Updates to Pelican and this blog.
Status: draft


Inspired by Fred Wilson's post about [Owning Yourself](http://avc.com/2018/01/owning-yourself/),
I revived my Pelican blog. Reasons for Pelican:

* version control in git
* my usual editor for content creation
* owning content
* complete customizability, therefore I want Python, therefore Pelican

Cost, have to contribute some changes myself:

* customized Pure theme [repository](https://github.com/svenkreiss/pure), including print mode, less author mentions, responsive resizing for mobile
* pelican-cite: created a [PR](https://github.com/cmacmackin/pelican-cite/pull/5) so that it also works on draft pages
* related_posts: newly added to this blog
* using KaTeX: nothing existed to combine it with Pelican and so I created
  [pelican-jsmath](https://github.com/svenkreiss/pelican-jsmath).
  The new plugin is $\alpha\omega\epsilon s \sigma m \epsilon$ and described in a separate
  [blog post]({filename}/pelican-jsmath.md).
* image_process: responsive images (smaller images on smaller devices) are
  especially important for the [projects](/projects.html) page
* Pelican plugins in a single repository or standalone? @svenkreiss/status/960716731059785730
* featured_image in article list
* pygments `friendly` style, a light theme for code highlighting shown in the [gallery](https://help.farbox.com/pygments.html)
* [pelican-advance-embed-tweet](https://pypi.python.org/pypi/pelican-advance-embed-tweet): already a package on pypi, but submitted [PR](https://github.com/fundor333/pelican-advance-embed-tweet/pull/2) to remove align attribute from `<bockquote>` which is not HTML5, and you can instead set `TWITTER_ALIGN = 'center'` in your `pelicanconf` to center the embedded tweet.

