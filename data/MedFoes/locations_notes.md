# Locations

### cut and pasted from: ftp://ftp.ncdc.noaa.gov/pub/data/noaa/isd-history.txt
<pre>
USAF   WBAN  STATION NAME                  CTRY ST CALL  LAT     LON      ELEV(M) BEGIN    END
722950 23174 LOS ANGELES INTERNATIONAL AIR US   CA KLAX  +33.938 -118.389 +0029.6 19440101 20170507
724940 23234 SAN FRANCISCO INTERNATIONAL A US   CA KSFO  +37.620 -122.365 +0002.4 19730101 20170507
722900 23188 SAN DIEGO INTERNATIONAL AIRPO US   CA KSAN  +32.734 -117.183 +0004.6 19420101 20170507
722020 12839 MIAMI INTERNATIONAL AIRPORT   US   FL KMIA  +25.791 -080.316 +0008.8 19730101 20170507
722050 12815 ORLANDO INTERNATIONAL AIRPORT US   FL KMCO  +28.434 -081.325 +0027.4 19520507 20170507

723890 93193 FRESNO YOSEMITE INTERNATIONAL US   CA KFAT  +36.780 -119.719 +0101.5 19411204 20170509
722060 13889 JACKSONVILLE  INTERNATIONAL A US   FL KJAX  +30.495 -081.694 +0007.9 19480101 20170509
722110 12842 TAMPA INTERNATIONAL AIRPORT   US   FL KTPA  +27.962 -082.540 +0005.8 19400801 20170509

722430 12960 G BUSH INTERCONTINENTAL AP/HO US   TX KIAH  +29.980 -095.360 +0029.0 19730101 20170509
722880 23152 BURBANK-GLENDALE-PASA ARPT    US   CA KBUR  +34.201 -118.358 +0236.2 19430601 20170509
722860 23119 MARCH AIR RESERVE BASE        US   CA KRIV  +33.900 -117.250 +0468.2 19330101 20170515

722977 93184 J. WAYNE APT-ORANGE CO APT    US   CA KSNA  +33.680 -117.866 +0016.5 19400617 20170507
722865 93180 ONTARIO                       US   CA KONT  +34.067 -117.650 +0303.9 19421215 19991231
</pre>

Not using but parsed:
<pre>
722026 12826 HOMESTEAD AFB AIRPORT         US   FL KHST  +25.483 -080.383 +0001.5 19430201 20170507
722976 03166 FULLERTON MUNICIPAL ARPT      US   CA KFUL  +33.872 -117.979 +0029.3 20060101 20170515
</pre>

Looking at:
<pre>
</pre>

## Problems

KSNA has good data starting on 1999-02-18, but prior to that, every day seems to be missing 05:00 to 13:00 values.  I can't interpolate/fill that.

KMCO has 2 year gap 1971-01-01 04:00:00+00:00	to 1973-01-01 00:00:00+00:00.  Looks good from 1973 onward though.

KBUR has 4 year gap 1969-01-01 06:00:00+00:00	to 1973-01-01 00:00:00+00:00 :1460 days 18:00:00.  Looks decent from 1973 onward... quite a few ~1 day gaps.

KONT is quite fragmented (5 different station lines). Has several big gaps, esp. in 2001. 

KHST Quite a few problems... many significant gaps and some outliers which would have to be removed by hand (not bothering since we're not going to use it).

KFUL is just bad

## Good very long datasets:
* KLAX good from 1947-01-01 14:00:00+00:00
* KSFO good from 1948-01-02 00:00:00+00:00
* KSAN good from 1948-01-01 14:00:00+00:00
* KMIA good from 1948-01-01 00:00:00+00:00
* KFAT good from 1949-08-21 14:00:00+00:00
* KJAX good from 1948-01-01 00:00:00+00:00
* KTPA good from 1948-01-01 11:00:00+00:00
* KRIV good from 1941-09-01 08:00:00+00:00

Good starting in 1973 datasets... all of the above plus:
* KMCO good pretty far back, but missing 1971 and 1972 for some reason.
* KIAH starts 1969-06-01 00:00:00+0000
* KBUR OK starting from 1973

## Done (2017-05-18 version of Fetching and Cleaning scripts):
* KLAX
* KSNA : Not good
* KSFO
* KSAN
* KMIA
* KMCO
* KFAT
* KJAX
* KTPA
* KIAH
* KBUR
* KONT : Not good, 1968+ might be usable but 2001 has an 86 day and 41 day gap.
* KHST : Not good
* KRIV
* KFUL : Bad
