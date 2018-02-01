Title: Decouple
Date: 2016-12-31
Category: Science
Tags: physics
Slug: decouple
Summary: Decoupling theoretical uncertainties from measurements of the Higgs boson.


## Decoupling theoretical uncertainties from measurements of the Higgs boson ([Phys Rev D91](http://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.054032), [arXiv:1401.0080](http://arxiv.org/abs/1401.0080))

This paper [@@Cranmer:2013hia] by Kyle Cranmer, David Lopez-Val, Tilman Plehn and me is now published in [Phys Rev D91](http://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.054032) and also available at [arXiv:1401.0080](http://arxiv.org/abs/1401.0080).

> We develop a technique to present Higgs coupling measurements, which decouple the poorly defined theoretical uncertainties associated to inclusive and exclusive cross section predictions. The technique simplifies the combination of multiple measurements and can be used in a more general setting. We illustrate the approach with toy LHC Higgs coupling measurements and a collection of new physics models.

We share all the software that was involved. That includes that we published the model files and a Mathematica notebook on [figshare](http://figshare.com/articles/Supplementary_Material_for_A_Novel_Approach_to_Higgs_Coupling_Measurements_/888607). We put all the code on [github](http://github.com/svenkreiss/decouple) which can be used for new models or to reproduce all plots in the paper simply by typing `make`. We even have a little [demo project](http://github.com/svenkreiss/decoupledDemo) that pulls three pre-made decoupled models from a webpage and recouples them and produces two plots of combined benchmark coupling models.
