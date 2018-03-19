#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


Created on Thu Mar 15 16:31:16 2018

@author: sandieguillaumettepasche

commentaires: Première essaie avec "Network Coincidence Trigger Example"
Ici je vais essayer de traiter que les données de Eiger West

ok, alors pour l'instant pas de display precis etc, mais les data des mes picks
qui dépasse les parameters que j'introduit ! J'ai accès aux infos grâce a une
liste ensuite.

coincidence_trigger:
The routine works in the following steps:
take every single trace in the stream
apply specified triggering routine (can be skipped to work on precomputed
custom characteristic functions)
evaluate all single station triggering results
compile chronological overall list of all single station triggers
find overlapping single station triggers
calculate coincidence sum of every individual overlapping trigger
add to coincidence trigger list if it exceeds the given threshold
optional: if master event templates are provided, also check
single station triggers individually and include any single station
trigger if it exceeds the specified similarity threshold even if no
other stations coincide with the trigger
return list of network coincidence triggers



"""

from obspy.core import Stream, read
from obspy import UTCDateTime
from obspy.signal.trigger import coincidence_trigger, plot_trigger, trigger_onset, classic_sta_lta
from obspy.clients.filesystem.sds import Client
from pprint import pprint
import matplotlib.pyplot as plt

wdir = "/Users/sandieguillaumettepasche/Documents/MASTER/Test_data/DATASET_TEST/SDS_"
sta = ['EIG']
# mon problem ici c'est que c'est pas Sta/Lta classic mais recursive
# programme info. organisé de manière telle qu'il puisse se rappeler lui
# meme, c'esr-à-dire demander sa propore exécution au cours de son déroulement
# ici trouver une façon cool d'ouvrir toutes mes données Eiger DATASET
# Si je veux les 3 channels, je dois utiliser un client !
# Mais le client je dois mettre un temps et tout...


def read_file__():
    client = Client(wdir+sta[0])
    st = Stream()
    t = UTCDateTime("2016-05-05T00")
    st += (client.get_waveforms('*', sta[0]+'1', '*', '*', t, t+30000))
    # print(st)
    # st.plot(size=(800, 600))
    # plt.show()
    return st


st = read_file__()
st.sort()
st2 = st.copy()  # is that necessary if I dont BP filter ?
trig = coincidence_trigger("classicstalta", 1.01, 0.99, st, 3, sta=0.5, lta=10,)
# la ligne supperieur c'est les meme param que lorsque que je display
# details=True pour avoir les details, mais du coup il faut select un tring [0]
pprint(trig)

# Partie a travailler

# For convenience
# tr = st[0]  # only one trace in mseed volume
# print(tr)
# df = tr.stats.sampling_rate

# Characteristic function and trigger onsets
# cft = classic_sta_lta(tr.data, int(2.5 * df), int(10. * df))
# on_of = trigger_onset(cft, 1.01, 0.99)

# Plotting the results
# for ix in range(len(tr)):
    # parametre du triggering
    # df = stream[ix].stats.sampling_rate  # pour le coup c'est la freq en HZ (ICI 200)
    # cft = classic_sta_lta(stream[ix].data, int(5 * df), int(10 * df))  # longueur des fenetre
    # plot_trigger(stream[ix], cft, 1.001, 0.999)  # set les limites STA/LTA