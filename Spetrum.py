#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:40:06 2018

@author: sandieguillaumettepasche

commentaires : Je veux aussi plotter le spectrogramm, ensuite peut-être que je 
filtrerais les raw data selon le resultat du spectrogram !
Voilà, merci à vous <3
"""

import matplotlib.pyplot as plt
from obspy.core import Stream
from obspy import UTCDateTime
from obspy.clients.filesystem.sds import Client


wdir = "/Users/sandieguillaumettepasche/Documents/MASTER/Test_data/DATASET_TEST/SDS_"
sta = ['EIG']

# Get the file of our waveformes


def read_allfile():
    client = Client(wdir+sta[0])
    st = Stream()
    t = UTCDateTime("2016-05-05T00")  # après ici je peux faire un loop
    st += (client.get_waveforms('*', sta[0]+'1', '*', '*', t, t+100))
    # si je met t+ > 86400, cela reach d'autres jours
    return st


st = read_allfile()
st.sort()
print(st[0])
st2 = st.copy()  # is that necessary if I dont BP filter ?
st2.spectrogram(log=True, title='try')
