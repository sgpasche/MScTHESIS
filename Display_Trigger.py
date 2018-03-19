#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:56:08 2018

@author: sandieguillaumettepasche

commentaires : first try STA/LTA, only with EIG, with first data set
"""
# import important module from obspy to prevent overwrite

from obspy.core import read, Stream
from obspy.signal.trigger import classic_sta_lta, plot_trigger
st = read()
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
# print(steam)
# print(stream.__str__(extended=True))

for ix in range(len(stream)):
    # parametre du triggering
    df = stream[ix].stats.sampling_rate  # pour le coup c'est la freq en HZ (ICI 200)
    cft = classic_sta_lta(stream[ix].data, int(5 * df), int(10 * df))  # longueur des fenetre
    plot_trigger(stream[ix], cft, 1.001, 0.999)  # set les limites STA/LTA
