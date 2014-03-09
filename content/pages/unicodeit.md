Title: unicodeit
Date: 2013-03-01 12:00
Slug: unicodeit



* This is a project by [Kyle Cranmer](http://physics.as.nyu.edu/object/KyleCranmer.html) and me.
* To use it: highlight some text and use the shortcut to replace latex with unicode characters
* Examples: <span style="font-family:sans-serif">p̅, x̲, ẋ, ∂̸</span>, H → γγ, ℋ, ℒ, x ∈ ℝ, y ∈ ℂ, β, γ, ∑, →, ←, μ⁺, e⁻
* Tested with Mac OS X Lion and Snow Leopard 10.6.4 in Keynote, Safari, Mail, Pages, TextEdit, Sublime Text; also tested on facebook.com, gmail.com, MediaWiki, TWiki using Safari


## Online Version: [www.unicodeit.net](http://www.unicodeit.net) for any platform

Download for Mac OS X: [unicodeit061.zip](http://www.unicodeit.net/automator/unicodeit061.zip)<br />
Linux wrapper: [http://code.google.com/p/unicodeitlinux/](http://code.google.com/p/unicodeitlinux/)<br />
Source on GitHub: [https://github.com/svenkreiss/unicodeit](https://github.com/svenkreiss/unicodeit)<br /><br />

For the new Keynote on Mavericks, text replacements currently do not work. Here is a special version that stores the output on the Clipboard: [unicodeit061clipboard.zip](http://www.unicodeit.net/automator/unicodeit061clipboard.zip)<br />
Install this in parallel to the standard UnicodeIt and assign a different keyboard shortcut to it; for example cmd+ctrl+shift+i.
<br /><br />



![explanation](http://www.svenkreiss.com/wiki/images/b/bd/explanation.png)


Introductory [Slides (pdf)](/files/UnicodeItSlides.pdf) and a list of [all latex expressions and their unicode replacements (pdf)](/files/UnicodeItSymbols06.pdf).<br />


## It's Free

The program is free and we hope you enjoy it as much as we do. If you feel like buying us beer or coffee, please do:
<html>
<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="ZT77WA6BZUWRE">
<input type="image" src="https://www.paypal.com/en_US/i/btn/btn_donate_SM.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>
</html>


## Installation on Mac OS Lion

* Download the workflow and open it
* Select File > Duplicate
* Save the duplicated workflow, e.g. as "UnicodeIt Copy"
* Setup keyboard shortcut under System Preferences > Keyboard > Keyboard Shortcuts > Services > Text > UnicodeIt&nbsp;Copy by clicking into the empty space behind it (e.g. Command+Option+Shift&nbsp;U)
* There is a delay first time you use the shortcut


## Installation on Mac OS Snow Leopard

* Add the workflow to: /Users/<username>/Library/Services/UnicodeIt.workflow (create the Services folder if it is not there already)
* Setup keyboard shortcut under System Preferences > Keyboard > Keyboard Shortcuts > Services > Text > UnicodeIt by clicking into the empty space behind it (e.g. Command+Option+Shift&nbsp;U)
* There is a delay first time you use the shortcut


## Links

* For a more thorough discussion of LaTeX, HTML and Unicode tools and ideas: [http://www.nongnu.org/elyxer/](http://www.nongnu.org/elyxer/) and [http://pages.uoregon.edu/noeckel/Keynote.html#caveats](http://pages.uoregon.edu/noeckel/Keynote.html#caveats)
* Linux wrapper for UnicodeIt: [http://code.google.com/p/unicodeitlinux/](http://code.google.com/p/unicodeitlinux/)


## Changelog

* New in 0.6:
    * improved sub- and superscripts
    * some new symbols including: square root √, cube root ∛, fourth root ∜
* New in 0.5:
    * added combining marks: for example \bar{p} <span style="font-family:sans-serif">p̅</span>, \underline{x} <span style="font-family:sans-serif">x̲</span>, \dot{x} <span style="font-family:sans-serif">ẋ</span>, \slash{\partial} <span style="font-family:sans-serif">∂̸</span>
* New in 0.4:
    * \rightarrow now has the alias \to
    * added mathbb and mathcal symbols including the symbols used for Hamiltonian and Lagrangian densities ℋ, ℒ and for real and complex numbers ℝ, ℂ (for all symbols see the UnicodeItSymbols.pdf file)


## FAQ

* The native Mac applications work fine, but web browsers do not necessarily support the Mac's System Services. Safari and Chrome seem to be working fine, however [Firefox does not work with UnicodeIt](https://wiki.mozilla.org/Firefox/Feature_Brainstorming:Platform_Integration#Services_Integration_in_OS_X).
