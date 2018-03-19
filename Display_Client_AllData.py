#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:57:02 2018

@author: sandieguillaumettepasche

commentaires :
Sinon ok, met les données hors du loop
teste avec echantillion que du jour 1
"""
# Import the modules needed to run the script.

import matplotlib.pyplot as plt
from obspy.clients.filesystem.sds import Client
from obspy import UTCDateTime
from obspy.core import Stream

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = 12, 8
# from obspy import read

# file directory
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
                                        t, t+30000))
        elif sta[i] == 'BWG':
            t = UTCDateTime("2015-07-10T00")
            st += (client.get_waveforms('*', sta[i]+"1", '*', '*',
                                        t, t+30000))
        else:
            t = UTCDateTime("2016-05-05T00")
            st += (client.get_waveforms('*', sta[i]+"1", '*', '*',
                                        t, t+30000))
    # print(st)
    # st.plot(size=(800, 600))
    # plt.show()
    return st


st = read_file__()
st.sort()
# print(st)
print(st.__str__(extended=True))
st.plot(size=(800, 600))
plt.show()


# singlechannel = read(wdir+"/4D.EIG1..EHZ.D.2016.111")
# singlechannel.plot(type='dayplot') # Trying different type of plotting

# Open the file and display
# def read_file__():
#    threechannels = obspy.Stream()
#    chan = ('E','N','Z')
#    day = ('1','2') #Change for more days, maybe bigger file later...
#    for i in range(len(day)):
#        threechannels +=(read(wdir+"/4D.EIG"+day[i]+"..EH"+chan[0]+".D.2016.111"))
#        threechannels +=(read(wdir+"/4D.EIG"+day[i]+"..EH"+chan[1]+".D.2016.111"))
#        threechannels +=(read(wdir+"/4D.EIG"+day[i]+"..EH"+chan[2]+".D.2016.111"))
#
#    return threechannels
#
# data= read_file__()
# print(data)
# print(data[0].stats.mseed)
# data.plot()

# Zoom in our data (choose start time, color and number of ticks)
# dt = threechannels[0].stats.starttime
# threechannels.plot(color='red', number_of_ticks=7,
#                  tick_rotation=5, tick_format='%I:%M %p',
#                   starttime=dt + 60*60, endtime=dt + 60*60 + 120)
