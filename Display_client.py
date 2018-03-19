#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 11:12:50 2018

@author: sandieguillaumettepasche
"""

from obspy.clients.filesystem.sds import Client
from obspy import  UTCDateTime
client = Client("/Volumes/LACIE/DATASETS/SDS_BSG/")
t = UTCDateTime("2015-06-20T00")
st = client.get_waveforms('*', 'BSG1', '*', '*', '*', '*')  # Faux !
st.plot()