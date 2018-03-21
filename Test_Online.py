#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 09:53:07 2018

@author: sandieguillaumettepasche
Les données en ligne n'ont pas été cut de leur unwanted signal
"""

from obspy.core import Stream, read
st = Stream()
files = ["BW.UH1..SHZ.D.2010.147.cut.slist.gz",
         "BW.UH2..SHZ.D.2010.147.cut.slist.gz",
         "BW.UH3..SHZ.D.2010.147.cut.slist.gz",
         "BW.UH4..SHZ.D.2010.147.cut.slist.gz"]
for filename in files:
    st += read("https://examples.obspy.org/" + filename)
st.plot()
print(st)

# si je veux pouvoir display mes trace je suis obligée d'utilisé le format
# 4 Trace(s) in Stream:
"""BW.UH1..SHZ | 2010-05-27T16:24:03.679998Z -
2010-05-27T16:27:53.999998Z | 50.0 Hz, 11517 samples"""
