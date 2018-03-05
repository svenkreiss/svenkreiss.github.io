Title: AncientML 1
Date: 2018-03-05
Category: ML
Tags: ancientml
Summary: AncientML is a series of paper reading notes. This first edition covers the first mention of AI and the Mathematical Theory of Communication.
Status: published


AncientML is a series of paper reading notes. The purpose is to review
outstanding contributions to machine learning that are valuable to the
formation as an academic field.

Some rules about the papers:

* have at least 500 citations
* be sufficiently old so that interest in them cannot be considered
  a conflict for industry ML researchers and engineers
* have had impact on academia so that they would be considered valuable to teach

It's not supposed to be a summary but rather inspire reading of
the papers itself and discussions in person.


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
* Related: _The Idea Factory_ [@@ideafactory2012gertner] is a book about Bell Labs around that time.
* Related: [@khinchin1957mathematical] is a book that discusses this paper.
* _information_ $H$ is not attached to a particular message but to the amount of
  freedom of choice
* John Tukey suggested the word "bit" for "binary digit"
* example to visualize the connection between probability of a message and information:
    * only two possible messages with $p_1$ and $p_2=1-p_1$
    * what is the amount of information as a function of $p_1$?
    * information is maximum for $p_1 = 0.5$, "when one is completely free to choose"
    * information goes to zero when one of the messages is very probable: "no freedom of choice -- no information"
* p.49: "decomposition of choice" is a beautiful requirement for $H$, and leads with
  the other two requirements to a unique form for $H$
* p.53: origin for terms of the form $p_i\log{}p_i$
* p.56: relative entropy, maximum possible compression, redundancy
* ...

## Backlog

* Multidimensional binary search trees used for associative searching,
  [@@bentley1975multidimensional],
  [PDF](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.160.335&rep=rep1&type=pdf)
* RBM predecessor Harmonium: Information processing in dynamical systems: Foundations of harmony theory,
  [@@smolensky1986information], [PDF](http://stanford.edu/~jlmcc/papers/PDP/Volume%201/Chap6_PDP86.pdf)
* Reducing the Dimensionality of Data,
  [@@hinton2006reducing], [PDF](http://www.cs.toronto.edu/~hinton/science.pdf)
* Online Convex Programming and Generalized Infinitesimal Gradient Ascent
  [@@zinkevich2003online], [PDF](http://www.aaai.org/Papers/ICML/2003/ICML03-120.pdf)
* Supervised Sequence Labelling with Recurrent Neural Networks
  [@@graves2012supervised], [PDF](https://www.cs.toronto.edu/~graves/preprint.pdf)
* High-speed tracking with kernelized correlation filters,
  [@@kcftracker2015high], [PDF](https://arxiv.org/pdf/1404.7584)

Similar resources: @shakir_za tweets a series called "Sunday Classic Paper".
