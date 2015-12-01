Title: About
Date: 2014-03-06 22:27
Slug: about
url: /
save_as: index.html
Summary: Sven Kreiss is a Data Scientist in New York City.


<!-- {% img img-thumbnail float-right http://www.gravatar.com/avatar/1838de72eb5ce4b000c41c06dedb52c4.png?s=180 %} -->
{% img img-thumbnail float-right /images/me_nyc_square_500.jpeg 250 Sven Kreiss in front of Freedom Tower. %}

I am a Data Scientist at [Wildcard](http://www.trywildcard.com/) in New York City. We are processing millions of news articles every month. I apply machine learning techniques and especially computer vision algorithms to content extraction problems to convert websites into cards.

I recently earned a PhD in Particle Physics from [New York University (NYU)](http://physics.nyu.edu/) where I worked with [Kyle Cranmer](http://physics.as.nyu.edu/object/kylecranmer.html). At the end of 2012, I returned to New York from a year at [CERN](http://www.cern.ch), Switzerland. Originally, I am from Germany, then studied for my bachelor's and master's degree in Mathematical Physics at the University of Edinburgh, Scotland, and then went to New York University for my PhD.

During my PhD, I wrote code for the statistical analysis tool [RooStats](http://twiki.cern.ch/twiki/bin/view/RooStats/WebHome) which is part of [CERN's Root Data Analysis tool](http://root.cern.ch/). My [ATLAS](http://atlas.web.cern.ch/Atlas/Collaboration/) work was focused on the the H→ZZ*→4l analysis, the Higgs Combination and I was involved in the discovery (see [New York Times article](/blog/chasing-the-higgs-nyt/)), the first mass measurement, the first evidence for VBF production and property measurements related to the coupling strengths of the Higgs Boson.

Here is a list of my [<i class="fa fa-cogs"></i> side projects](/projects.html), my blog [<i class="fa fa-rss"></i> trivial.io](http://trivial.io), my [old blog](/blog/) and my [<i class="fa fa-file-text"></i> CV](/files/cv.html). Selected talks and papers are at the bottom of the page.
My social media profiles are [<i class="fa fa-twitter"></i> Twitter](https://twitter.com/svenkreiss), [<i class="fa fa-linkedin-square"></i> LinkedIn](http://www.linkedin.com/in/svenkreiss) and [<i class="fa fa-github"></i> GitHub](https://github.com/svenkreiss/) and my email address is [<i class="fa fa-envelope"></i> me@svenkreiss.com](mailto:me@svenkreiss.com).



## Chasing the Higgs - The New York Times

My part of the Higgs discovery story in the New York Times.

{% img /images/nyt_science_front_page.jpeg 200 Science Times section front page %}
{% img /images/nyt_science_my_part.jpeg 350 Chasing the Higgs, my part %}

<div style="clear:both;"></div>

That "joyful expletive" was "Holly shit" (not correcting the typo) sent from his phone.<br />
Read the full story on the [New York Times website](http://www.nytimes.com/2013/03/05/science/chasing-the-higgs-boson-how-2-teams-of-rivals-at-CERN-searched-for-physics-most-elusive-particle.html?view=Opening_the_Box) from March 5, 2013.<br />
The New Yorker also had a piece about our [Nobel Prize Party](/blog/nobel-prize-party-new-yorker).



## Decoupling theoretical uncertainties from measurements of the Higgs boson ([Phys Rev D91](http://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.054032), [arXiv:1401.0080](http://arxiv.org/abs/1401.0080))

This paper by Kyle Cranmer, David Lopez-Val, Tilman Plehn and me is now published in [Phys Rev D91](http://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.054032) and also available at [arXiv:1401.0080](http://arxiv.org/abs/1401.0080).

> We develop a technique to present Higgs coupling measurements, which decouple the poorly defined theoretical uncertainties associated to inclusive and exclusive cross section predictions. The technique simplifies the combination of multiple measurements and can be used in a more general setting. We illustrate the approach with toy LHC Higgs coupling measurements and a collection of new physics models.

We share all the software that was involved. That includes that we published the model files and a Mathematica notebook on [figshare](http://figshare.com/articles/Supplementary_Material_for_A_Novel_Approach_to_Higgs_Coupling_Measurements_/888607). We put all the code on [github](http://github.com/svenkreiss/decouple) which can be used for new models or to reproduce all plots in the paper simply by typing `make`. We even have a little [demo project](http://github.com/svenkreiss/decoupledDemo) that pulls three pre-made decoupled models from a webpage and recouples them and produces two plots of combined benchmark coupling models.



## MorphDemo using `d3.js`

{% img img-thumbnail float-right /images/kdtreemorph_preview.png 350 Preview of kd-tree based morphing algorithm %}
[This](/files/morphDemo.html) is an interactive demo for a new morphing algorithm with special properties that are motivated from Physics. It uses KD trees and kernel density estimates that are calculated in real time in this demo. All visualization is done using `d3.js` and custom code for KD trees and kernel densities in JavaScript.

Link: [morphDemo.html](/files/morphDemo.html), [blog post](/blog/morph-demo/)

<div style="clear:both;"></div>



## Selected Publications

I had major contributions to the discovery of the Higgs Boson at CERN,
Switzerland, in 2012 and I am a co-author of the statistics software used
for Higgs Boson studies, RooStats. Analyses that I worked on and plots that
I made are part of publications in the journal Science, Physics Letters B
and the Particle Data Group among others.

* 01/2014: Cranmer, Kreiss, Lopez-Val, Plehn. _Decoupling theoretical uncertainties from measurements of the Higgs boson_. [Phys Rev D91](http://journals.aps.org/prd/abstract/10.1103/PhysRevD.91.054032), [arXiv:1401.0080](http://arxiv.org/abs/1401.0080).
* 07/2013: ATLAS collaboration. _Measurements of Higgs boson production and couplings in diboson final states with the ATLAS detector at the LHC_. I was an editor. [Inspire](http://inspirehep.net/record/1241574). Phys.Lett. B726 (2013) 88-119.
* 07/2013: ATLAS collaboration. _Evidence for the spin-0 nature of the Higgs boson using ATLAS data_. [Inspire](http://inspirehep.net/record/1241575). Phys.Lett. B726 (2013) 120-144.
* 03/2013: ATLAS collaboration. _Combined coupling measurements of the Higgs-like boson with the ATLAS detector using up to 25 fb−1 of proton-proton collision data_. I was an editor for the main supporting document. [Inspire](http://inspirehep.net/record/1229948).
* 03/2013: ATLAS collaboration. _Study of the spin of the new boson with up to 25 fb−1 of ATLAS data_. [Inspire](http://inspirehep.net/record/1229942).
* 12/2012: ATLAS Collaboration. _A Particle Consistent with the Higgs Boson Observed with the ATLAS Detector at the Large Hadron Collider_. [Science, vol 338, issue 6114, 1576-1582](http://www.sciencemag.org/content/338/6114/1576.full.pdf).
* 07/2012: ATLAS Collaboration. _Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC_. CERN-PH-EP-2012-218, [Phys.Lett. B716 (2012) 1-29](http://www.sciencedirect.com/science/article/pii/S037026931200857X), [arXiv:1207.7214](http://arxiv.org/abs/arXiv:1207.7214).
* 07/2012: ATLAS Collaboration. _Combined search for the Standard Model Higgs boson in pp collisions at √s&nbsp;=&nbsp;7&nbsp;TeV with the ATLAS detector_. Phys.Rev. D86 (2012) 032003.
* 02/2012: ATLAS collaboration. _Combined search for the Standard Model Higgs boson using up to 4.9 fb⁻¹ of pp collision data at √s&nbsp;=&nbsp;7&nbsp;TeV with the ATLAS detector at the LHC_. [Phys.Lett. B710 (2012) 49-66](http://www.sciencedirect.com/science/article/pii/S0370269312001852), [arXiv:1202.1408](http://arxiv.org/abs/1202.1408).
* 12/2010: ATLAS collaboration. _Measurement of the top quark pair production cross-section with ATLAS in pp collisions at √s&nbsp;=&nbsp;7&nbsp;TeV_. Eur.Phys.J.C71:1577,2011, [arXiv:1012.1792](http://arxiv.org/abs/1012.1792).
* 10/2010: L. Moneta, K. Belasco, K.S. Cranmer, S. Kreiss, A. Lazzaro, et al. _The RooStats Project_. [PoS&nbsp;(ACAT2010)&nbsp;057](http://pos.sissa.it/archive/conferences/093/057/ACAT2010_057.pdf).
* 03/2008: M.M. Nojiri et al. _Physics Beyond the Standard Model: Supersymmetry._ SUSY working group report: Les Houches 2007. [arXiv:0802.3672](http://arxiv.org/abs/0802.3672).
* 01/2008: B.C. Allanach et al. _SUSY Les Houches Accord 2_. CPC&nbsp;180&nbsp;(2009)&nbsp;1, [arXiv:0801.0045](http://arxiv.org/abs/0801.0045).

On Inspire: [Paper list](http://inspirehep.net/search?ln=en&ln=en&p=find+a+%22s+kreiss%22&action_search=Search&sf=&so=d&rm=&rg=25&sc=0&of=hb), [Author page](http://inspirehep.net/author/S.Kreiss.1/).


## Selected Talks

I gave talks at conferences, universities and companies in Hamburg, Goettingen and Dresden (Germany),
Split (Croatia), Geneva (Switzerland), Rome (Italy), Cambridge (UK),
Raleigh (NC, USA) and New York (NY, USA).

* 09/2015: Deep ML Architecture at Wildcard, MLconf, Atlanta
* 05/2015: Data and the Higgs Boson Discovery, Betaworks, New York
* 04/2014: Collaborative Statistical Modeling, Opening of the Center for Data Science at NYU, New York, [Poster](http://cds.nyu.edu/projects/collaborative-statistical-modeling/)
* 01/2014: Factorizing Theoretical Uncertainties from LHC Higgs Coupling Measurements, Seminar, University of Cambridge, UK
* 07/2013: Modeling and Statistical Analysis for Higgs Physics at the Large Hadron Collider, Knowledge Extraction via Comparison of Complex Computational Models to Massive Data Sets, Durham, NC, USA, [Conference page](http://www.samsi.info/workshop/2013-knowledge-extraction-comparison-complex-computational-models-massive-data-sets-july-29), [PDF](http://www.samsi.info/sites/default/files/Kreiss_madai_july2013.pdf)
* 01/2013: H→ZZ*→4l  Likelihood in ATLAS, Likelihoods for the LHC Searches, CERN, [Conference Indico](http://indico.cern.ch/conferenceOtherViews.py?view=standard&confId=218693), [PDF](http://indico.cern.ch/getFile.py/access?contribId=13&resId=0&materialId=slides&confId=218693)
* 10/2012: Standard Model Higgs Combination and Properties, LHC Days 2012, Split, Croatia, [Conference Indico](https://indico.cern.ch/event/186656/other-view?view=standard), [ATL-PHYS-SLIDE-2012-609](http://cdsweb.cern.ch/record/1490096)
* 05/2012: RooStats: Statistical Tools for the LHC, CHEP 2012, New York, [Slides](http://indico.cern.ch/contributionDisplay.py?contribId=371&confId=149557)

