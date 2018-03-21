#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:57:02 2018

@author: sandieguillaumettepasche

commentaires: pour avoir un stream
le sort de la fonction donc cool
"""
# Import the modules needed to run the script.

import matplotlib.pyplot as plt
import obspy
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = 12, 8

# file directory
wdir = "/Users/sandieguillaumettepasche/Documents/MASTER/Test_data"

# singlechannel = obspy.read(wdir+"/4D.EIG1..EHZ.D.2016.111")
# singlechannel.plot(type='dayplot') # Trying different type of plotting

# Open the file and display


def read_file__():
    threechannels = obspy.Stream()
    chan = ('E', 'N', 'Z')
    day = ('1', '2')  # Change for more days, maybe bigger file later...
    for i in range(len(day)):
        print(i)
        threechannels +=(obspy.read(wdir+"/4D.EIG"+day[i]+"..EH"+chan[0]+".D.2016.111"))
        threechannels +=(obspy.read(wdir+"/4D.EIG"+day[i]+"..EH"+chan[1]+".D.2016.111"))
        threechannels +=(obspy.read(wdir+"/4D.EIG"+day[i]+"..EH"+chan[2]+".D.2016.111"))
        # threechannels.update({"%s"%i:threechannels})

    return threechannels


data = read_file__()

print(data)
print(data[0].stats.mseed)


# Zoom in our data (choose start time, color and number of ticks)
# dt = threechannels[0].stats.starttime
# threechannels.plot(color='red', number_of_ticks=7,
#                  tick_rotation=5, tick_format='%I:%M %p',
#                   starttime=dt + 60*60, endtime=dt + 60*60 + 120)

# Use fonction
threechannels = read_file__()

# Use UTCDateTime
# print(obspy.UTCDateTime()) #current time
# To add an hour = en seconde +3600; to get the year => time = obspy.UTC...("")
# .year

# ==========================================================================
# Waveforms