#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 11:06:03 2018

@author: sandieguillaumettepasche

Comments : here the idea is to trigger data and then display only the output
and not the cfc etc.
ARTUNG: you need to make a copy of you data if you rescale them, otherwise
they are forever changed
"""

# import module
from obspy.core import Stream, read
from obspy import UTCDateTime
from obspy.signal.trigger import coincidence_trigger, plot_trigger, trigger_onset, classic_sta_lta
from obspy.clients.filesystem.sds import Client

wdir = "/Users/sandieguillaumettepasche/Documents/MASTER/Test_data"


def read_file__():
    threechannels = Stream()
    chan = ('E', 'N', 'Z')
    day = ('1')  # Change for more days, maybe bigger file later...
    for i in range(len(day)):
        print(i)
        threechannels += (read(wdir + "/4D.EIG" + day[i] +
                               "..EH" + chan[0] + ".D.2016.111"))
        threechannels += (read(wdir + "/4D.EIG" + day[i] +
                               "..EH" + chan[1]+".D.2016.111"))
        threechannels += (read(wdir + "/4D.EIG" + day[i] +
                               "..EH" + chan[2] + ".D.2016.111"))
    return threechannels


stream = read_file__()
stream.sort()
stream2 = stream.copy()
# print(steam)
# print(stream.__str__(extended=True))

for ix in range(len(stream)):
    # parametre du triggering
    stream[ix].trigger('recstalta', sta=1.001, lta=0.999)
    stream.plot()
