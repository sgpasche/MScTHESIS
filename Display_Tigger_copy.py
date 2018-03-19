#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:00:37 2018

@author: sandieguillaumettepasche

commentaires : Essaie trigger 2 avec le deuxième data set test

USELESS --> IL FAUT REFAIRE MAIS AVEC Network Coincidence Trigger Example¶
"""

# import important module from obspy to prevent overwrite

from obspy.core import read, Stream
from obspy.signal.trigger import classic_sta_lta, plot_trigger
from obspy.clients.filesystem.sds import Client
from obspy import UTCDateTime
wdir = "/Users/sandieguillaumettepasche/Documents/MASTER/Test_data/DATASET_TEST/SDS_"
sta = ['BSG', 'BWG', 'EIG']


def read_file__():
    st = Stream()
    for i in range(len(sta)):
        print(i) 
        client = Client(wdir+sta[i])
        if sta[i] == 'BSG':
            t = UTCDateTime("2015-06-20T00")
            st += (client.get_waveforms('*', sta[i]+"1", '*', '*',
                                        t+10000, t+300000))
        elif sta[i] == 'BWG':
            t = UTCDateTime("2015-07-10T00")
            st += (client.get_waveforms('*', sta[i]+"1", '*', '*',
                                        t+10000, t+300000))
        else:
            t = UTCDateTime("2016-05-05T00")
            st += (client.get_waveforms('*', sta[i]+"1", '*', '*',
                                        t+10000, t+300000))
    # print(st)
    # st.plot(size=(800, 600))
    # plt.show()
    return st


stream = read_file__()
stream.sort()
# print(steam)
# print(stream.__str__(extended=True))

for ix in range(len(stream)):
    # parametre du triggering
    df = stream[ix].stats.sampling_rate
    cft = classic_sta_lta(stream[ix].data, int(0.5 * df), int(0.5 * df))
    plot_trigger(stream[ix], cft, 1.5, 0.5) # haallloo, c'est juste pour le plot, change pas ca !
