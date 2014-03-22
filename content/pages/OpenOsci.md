Title: OpenOsci
Date: 2014-03-09 19:36
Slug: openosci



> Open source and open hardware electronics project to build a low-cost digital oscilloscope with an 8-bit microcontroller and a mobile phone screen.

{% vimeo 21789038 600 400 %}


## Capabilities
* 4 input channels
* no fixed frequencies; the ADC can be run with different clock cycles and then the time for one x-division is displayed in the display; the "td" value (in the images below, 47 microseconds and 9 milliseconds)
* the display also shows a frequency estimate of the signal. The algorithm looks at the time between to successive crossings of the x-axis and calculates a frequency from that. For sine waves, this is reasonably accurate. In the right picture below I measure background noise with a frequency of 49 Hz; the left picture shows a 43 kHz oscillation.

<div style="clear:both"> </div>


## Fotos
{% img /images/openosci/2channels_function_generator.jpg 500 OpenOsci in action %}
<div style="clear:both"></div>
{% img /images/openosci/channel_42kHz.jpg 300 one channel %}
{% img /images/openosci/4channels_50Hz.jpg 300 four channels %}
<div style="clear:both"> </div>


## Hardware
{% img /images/openosci/sketchy_060306_schematic.png 500 Prototype schematic %}
{% img /images/openosci/sketchy_060306_board.png 380 Prototype board %}

Please be aware that I built only one version. There are many flaws in that one version, but all photos/videos shown here are made with this version.

* Schematic: [openosci_060306_produced.sch](/files/openosci/sketchy_060306_produced.sch)
* Board: [openosci_060306_produced.brd](/files/openosci/sketchy_060306_produced.brd)

While playing around with this prototype, I was already making improvements to layout and board which I never built or tested.

* Schematic: [openosci_060426.sch](/files/openosci/sketchy_060426.sch)
* Board: [openosci_060426.brd](/files/openosci/sketchy_060426.brd)


## Software

* Download: [source_code.zip](/files/openosci/source_code.zip)
* code reference manual: [pdf](/files/openosci/reference_manual.pdf), [html](/files/openosci/reference_manual_html/)

## Links
* _apetech.de (broken)_: Graphical Display routines for the Nokia 6100.
* _superkranz.de (broken)_: Port of the above routines to Siemens S65 screens.
* [mikrocontroller.net](http://www.mikrocontroller.net): thread about the screen

## Disclaimer
This is an old project of mine. It was done in 2006 and some parts might be out of date. I cannot guaranty proper functionality or fitness for any particular use.