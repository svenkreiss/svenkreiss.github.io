Title: Artisanal S2 Cells
Date: 2018-11-28
Category: Tech
Tags: Python, geo, data
Slug: artisanal-s2
Summary: Creating S2-cell ids by hand.
Status: published


S2 cells are a great representation for locations on earth and are the storage
format for many popular web services, including Google Maps, Foursquare and Pokemon Go.
I worked on the [s2sphere](https://s2sphere.readthedocs.io) Python implementation when I was at Sidewalk Labs. I also wrote some
background notes on the [Sidewalk blog](https://www.sidewalklabs.com/blog/s2-cells-and-space-filling-curves-keys-to-building-better-digital-map-tools-for-cities/).
Recently, I was asked to explain
how to verify manually that an S2 cell id is correct. By hand. From scratch.
Here is my answer for the simplest ids.

Get a feel for the cells and faces of the cube by using the web tools
at [s2.sidewalklabs.com](https://s2.sidewalklabs.com):

<img style="width:58.5%" src="/images/s2cell_regioncoverer.png" />
<img style="width:39.7%" src="/images/s2cell_globe.png" />

Tokens are hex format with right zeros stripped. To recover an integer, use
[`from_token()`](https://s2sphere.readthedocs.io/en/latest/api.html#s2sphere.CellId.from_token)
and print as binary. The example tokens converted to binary cell ids are:
```
token "04": 0000010000000000000000000000000000000000000000000000000000000000
token "0c": 0000110000000000000000000000000000000000000000000000000000000000
token "14": 0001010000000000000000000000000000000000000000000000000000000000
token "1c": 0001110000000000000000000000000000000000000000000000000000000000
```

The binary format from left to right: three bits for face (here face 0), two bits to encode the cell on that face, 1 bit terminating. In agreement with what is in the docstring for the
[CellId](https://s2sphere.readthedocs.io/en/latest/api.html#s2sphere.CellId) class :)

Just to compare, face 1, level 1 cell ids are:
```
0010010000000000000000000000000000000000000000000000000000000000
0010110000000000000000000000000000000000000000000000000000000000
0011010000000000000000000000000000000000000000000000000000000000
0011110000000000000000000000000000000000000000000000000000000000
```

It all makes sense. Those are eight hand-crafted S2 cell ids.
