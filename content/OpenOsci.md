Title: OpenOsci
Date: 2006-06-01
Category: Tech
Tags: open source, open hardware, electronics
Slug: open-osci
Status: draft
Summary: My open source and open hardware oscilloscope with a mobile phone screen.


> Open source and open hardware electronics project to build a low-cost digital oscilloscope with an 8-bit microcontroller and a mobile phone screen.


{% vimeo 21789038 400 300 %}


## Capabilities
* 4 input channels
* no fixed frequencies; the ADC can be run with different clock cycles and then the time for one x-division is displayed in the display; the "td" value (in the images below, 47 microseconds and 9 milliseconds)
* the display also shows a frequency estimate of the signal. The algorithm looks at the time between to successive crossings of the x-axis and calculates a frequency from that. For sine waves, this is reasonably accurate. In the right picture below I measure background noise with a frequency of 49 Hz; the left picture shows a 43 kHz oscillation.

<div style="clear:both"> </div>

## Fotos
[[image:Openosci_2channels_function_generator.jpg|thumb|left|500px|OpenOsci in action]]
<div style="clear:both"></div>
[[image:Openosci_channel_42kHz.jpg|thumb|left|300px|One channel.]]
[[image:Openosci_4channels_50Hz.jpg|thumb|left|300px|Four channels.]]
<div style="clear:both"> </div>

## Hardware
[[image:sketchy_060306_schematic.png|thumb|Prototype schematic]]
[[image:sketchy_060306_board.png|thumb|Prototype board]]
Please be aware that I built only one version. There are many flaws in that one version, but all photos/videos shown here are made with this version.
* Schematic: [[media:sketchy_060306_produced.sch]]
* Board: [[media:sketchy_060306_produced.brd]]

While playing around with this prototype, I was already making improvements to layout and board which I never built or tested.
* Schematic: [[media:sketchy_060426.sch]]
* Board: [[media:sketchy_060426.brd]]

## Software
* [[media:openosci_source_code.zip]]
* code documentation
** [http://www.svenkreiss.com/images/openosci/doc/reference_manual.pdf reference_manual.pdf]
** [http://www.svenkreiss.com/images/openosci/doc/reference_manual_html/ reference_manual_html]

## Links
* [apetech.de](http://www.apetech.de): Graphical Display routines for the Nokia 6100.
* [superkranz.de](http://www.superkranz.de): Port of the above routines to Siemens S65 screens.
* [mikrocontroller.net](http://www.mikrocontroller.net): thread about the screen

## Disclaimer
This is an old project of mine. It was done in 2006 and some parts might be out of date. I cannot guaranty proper functionality or fitness for any particular use.
