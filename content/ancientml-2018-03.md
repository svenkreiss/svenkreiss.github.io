Title: AncientML 1
Date: 2018-03-05
Category: ML
Tags: ancientml
Summary: AncientML is a series of paper reading notes. This first edition covers the first mention of AI and the Mathematical Theory of Communication.
Status: published

<img class="img-thumbnail float-right" src="/images/ancientml-logo.png" width="300" alt="AncientML Logo" />

AncientML is a series of paper reading notes. The purpose is to review
outstanding contributions to machine learning that are valuable to the
formation as an academic field.

<div style="clear:both"></div>

## A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence, August 31, 1955 [@@mccarthy2006proposal], [PDF](https://www.aaai.org/ojs/index.php/aimagazine/article/download/1904/1802)

* The paper/event that gets credited with the foundation of the field of Artificial Intelligence research.
* The paper is three pages long and the authors include Claude Shannon.
* scale of the proposed project: 2 months, 10 men
* focused on language, abstraction and concepts
* identifies seven areas to improve: Automatic Computers, How Can a Computer be
  Programmed to Use a Language, Neuron Nets, Theory of the Size of a Calculation,
  Self-Improvement, Abstractions, Randomness and Creativity
* "the major obstacle is not lack of machine capacity, but our inability to write programs"
* There is Wikipedia article on the [Dartmouth workshop](https://en.wikipedia.org/wiki/Dartmouth_workshop).
* 102 pages of Ray Solomonoff's
  [hand written notes](http://raysolomonoff.com/dartmouth/notebook/notebook.html)
  including some doodles on page 3.


## The Mathematical Theory of Communication [@@shannon1951mathematical], [PDF](http://pubman.mpdl.mpg.de/pubman/item/escidoc:2383164/component/escidoc:2383163/Shannon_Weaver_1949_Mathematical.pdf)

* Central paper for many fields. 90 pages (skip the part by Weaver).
* _The Idea Factory_ [@@ideafactory2012gertner] is a book about Bell Labs around that time.
* [@khinchin1957mathematical] is a book that discusses this paper.
* p.49: _information_ is not attached to a particular message but to the amount of
  freedom of choice
* p.49: "decomposition of choice" is a beautiful requirement for $H$, and leads with
  the other two requirements to a unique form for $H$
* p.50: simple example to visualize the connection between probability of a message and information is shown in the figure below
* p.53: origin for terms of the form $p_i\log{}p_i$
* p.56: relative entropy, maximum possible compression, redundancy
* p.70: capacity of a noisy channel; includes a `max()` over all possible information sources
