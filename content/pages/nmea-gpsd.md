Title: nmea-gpsd
Date: 2014-03-22
Slug: nmea-gpsd
Status: published


> The NMEA-Parser from the GPSD project.<br />
> This code is hosted on google code now: http://code.google.com/p/gpsd-nmea/


### Old instructions on how to recreate this yourself

To extract the NMEA-Parser out of GPSD is easier than it looks at first. Just download the whole source and copy these files into a separate directory:

* gps.h
* timebase.h
* geoid.c
* gpsutils.c
* nmea_parse.c


The next step is to replace all references to ''gpsd.h'' by ''gps.h'' and remove ''#include gpsd_config.h''.
You will also need to move some ''#define'' from ''gpsd_config.h'' and ''gpsd.h'' to ''gps.h''. Next step is to rewrite the functions in ''nmea_parse.c'' to take structs of type gps_data_t instead of gps_device_t. All what is necessary is to move the struct ''nmea'' from gps_device_t.driver to gps_data_t. Last thing is the dependency on gpsd_report. I just disabled it by putting a ''#define gpsd_report(...)'' at the beginning of ''gps.h''.
