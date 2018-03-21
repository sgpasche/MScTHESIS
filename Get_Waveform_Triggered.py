#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:45:05 2018

@author: sandieguillaumettepasche

First try using panda, in order to change my dictionary I get from Obspy
I am going to implement first a coincidence Network and then get the dictionary
to change them into data Serie to display them
So far this is my final version to display triggered data only. 21 mars 2018
"""

import pandas as pd
import matplotlib.pyplot as plt
from obspy.core import Stream
from obspy import UTCDateTime
from obspy.signal.trigger import coincidence_trigger
from obspy.clients.filesystem.sds import Client
import matplotlib.pyplot as plt

wdir = "/Users/sandieguillaumettepasche/Documents/MASTER/Test_data/DATASET_TEST/SDS_"
sta = ['EIG']

# Get the file of our waveformes

def read_allfile():
    client = Client(wdir+sta[0])
    st = Stream()
    t = UTCDateTime("2016-05-05T00")  # après ici je peux faire un loop
    st += (client.get_waveforms('*', sta[0]+'1', '*', '*', t, t+86400))
    # si je met t+ > 86400, cela reach d'autres jours
    return st


# Get the dictionary

st = read_allfile()
st.sort()
st2 = st.copy()  # is that necessary if I dont BP filter ?
trig = coincidence_trigger("classicstalta", 1.005, 0.995, st2, 2, sta=5, lta=10)

# thr_on, thr_off, thrs coincid (min chan have to coincide)
trig = pd.DataFrame(trig)

# Get only interesting traces


def read_triggered():
    client = Client(wdir+sta[0])
    trg = Stream()
    for i in range(len(trig.loc[:, 'trace_ids'])):
        trg += (client.get_waveforms('*', sta[0]+'1', '*', '*', trig.loc[i, 'time'], trig.loc[i, 'time'] + trig.loc[i, 'duration']))
    return trg
trg = read_triggered()
trg.sort()
print(trg.__str__(extended=True))
trg.plot(size=(800, 600))
