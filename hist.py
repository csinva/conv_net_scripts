import os
import matplotlib.cm as cm
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.pyplot as plt
import h5py
import array


# fibsem data
out = 'fibsem5'
hdf5_pred_file = '/tier2/turaga/turagas/research/pygt_models/fibsem5/test_out_0.h5' #'',0,2,3,4,6
hdf5_aff = h5py.File(hdf5_pred_file, 'r')
aff = np.asarray(hdf5_aff[hdf5_aff.keys()[0]],dtype='float32').flatten()


# paper data
'''
out = 'paper'
f = open("/groups/turaga/home/singhc/evaluation/data/ws_test_256.raw")
aff = array.array("f")
aff.fromfile(f, 256*256*256*3)
aff = np.frombuffer(aff,dtype='float32').flatten()
'''

fig = plt.figure(figsize=(20,10))
ax1,ax2,ax3 = fig.add_subplot(1,3,1),fig.add_subplot(1,3,2),fig.add_subplot(1,3,3)
ax1.hist(aff, bins=[.00025*i for i in range(0,100)])
ax1.set_xlim([0,.025])

ax2.hist(aff, bins=[.001*i for i in range(0,1001)])

ax3.hist(aff, bins=[1-.0001*(1000-i) for i in range(0,1000)])
ax3.set_xlim([.9,1])
plt.savefig('figs/'+out+'_hist.png')

plt.show()

fig = plt.figure(figsize=(20,10))
ax1,ax2,ax3 = fig.add_subplot(1,3,1),fig.add_subplot(1,3,2),fig.add_subplot(1,3,3)
ax1.hist(aff, bins=[.000002*i for i in range(0,100)])
ax1.set_xlim([0,.0002])
ax3.hist(aff, bins=[1-.00001*(100-i) for i in range(0,100)])
ax3.set_xlim([.999,1])
plt.savefig('figs/'+out+'_hist_detailed.png')
plt.show()
