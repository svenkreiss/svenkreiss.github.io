Title: Pelican 2018
Date: 2018-02-02
Category: Tech
Tags: blog
Slug: pelican-2018
Summary: Updates to Pelican.
Status: draft


Inspired by [Fred Wilson's post about owning content LINK!!!!!!!!](), revived
my Pelican blog. Reasons for Pelican:

* version control in git
* my usual editor for content creation
* owning content
* complete customizability, therefore I want Python, therefore Pelican

Cost, have to contribute some changes myself:

* customized Pure theme [repository](https://github.com/svenkreiss/pure), including print mode, less author mentions, responsive resizing for mobile
* pelican-cite: created a [PR](https://github.com/cmacmackin/pelican-cite/pull/5) so that it also works on draft pages
* using KaTeX: had to create [pelican-jsmath](https://github.com/svenkreiss/pelican-jsmath);
  There was a related [Pelican issue](https://github.com/getpelican/pelican-plugins/issues/625)
  for support. The new plugin is $\alpha\omega\epsilon s \sigma m \epsilon$.
