Title: Vimeo liquid tag for Pelican
Date: 2014-03-07 4:41
Category: Tech
Tags: web, python
Slug: pelican-vimeo
Summary: Extend liquid tags plugin for Pelican to include a Vimeo tag.


Testing my implementation of the `vimeo` tag for `liquid_tags`. This is based on the `youtube` tag which in turn is based on the [jekyll / octopress youtube tag](https://gist.github.com/jamieowen/2063748).

The syntax is the same as for the `youtube` tag:

<div class="highlight"><pre>
{% vimeo id [width height] %}
</pre></div>

_Update_: The code is now merged into the main pelican-plugins repository on github:
[https://github.com/getpelican/pelican-plugins](https://github.com/getpelican/pelican-plugins)


## Tests with different sizes

{% vimeo 21789576 320 180 %}
{% vimeo 21789576 480 270 %}
{% vimeo 21789576 640 360 %}

