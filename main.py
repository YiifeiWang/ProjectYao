 # -*- coding: utf-8 -*-
 
import utils
import pickle
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

info_dict_list = []

with open('gua.pi', 'rb') as f:
    info_dict_list = pickle.load(f,)

upper_list = []
lower_list = []

for i in range(len(info_dict_list)):
    upper = utils.GuaXiang(info_dict_list[i]).upper
    lower = utils.GuaXiang(info_dict_list[i]).lower
    upper_list.append(upper)
    lower_list.append(lower)

codebook = utils.GuaDict3

upper_list1 = [codebook[x] for x in upper_list]
lower_list1 = [codebook[x] for x in lower_list]

X1 = np.array(upper_list1)
Y1 = np.array(lower_list1)

Z1 = X1+Y1*1j
Z1_DFT = np.fft.fft(Z1)

X1 = X1.reshape([-1,1])
Y1 = Y1.reshape([-1,1])
tilde_X1 = np.concatenate([np.cos(X1/8*np.pi*2),np.sin(X1/8*np.pi*2)],axis=1)
tilde_Y1 = np.concatenate([np.cos(Y1/8*np.pi*2),np.sin(Y1/8*np.pi*2)],axis=1)

tilde_Z1 = tilde_X1+1j*tilde_Y1
tilde_Z1_DFT = np.fft.fft(tilde_Z1)

def illustration1():
    fig, ax = plt.subplots(2,2,figsize=(16,16))
    ax_sub = ax[0,0]
    ax_sub.plot(X1, 'r',label='upper')
    ax_sub.legend()
    ax_sub = ax[0,1]
    ax_sub.plot(Y1, 'b',label='lower')
    ax_sub.legend()
    ax_sub = ax[1,0]
    ax_sub.plot(np.absolute(Z1_DFT), 'r',label='magnitude')
    ax_sub.legend()
    ax_sub = ax[1,1]
    ax_sub.plot(np.angle(Z1_DFT), 'b',label='angle')
    ax_sub.legend()
    fig.savefig('卦象.png',dpi=100)

def illustration2():
    fig, ax = plt.subplots(4,2,figsize=(16,32))
    ax_sub = ax[0,0]
    ax_sub.plot(tilde_X1[:,0], 'r',label='upper-x')
    ax_sub.legend()
    ax_sub = ax[0,1]
    ax_sub.plot(tilde_Y1[:,0], 'b',label='lower-x')
    ax_sub.legend()
    ax_sub = ax[1,0]
    ax_sub.plot(tilde_X1[:,1], 'r',label='upper-y')
    ax_sub.legend()
    ax_sub = ax[1,1]
    ax_sub.plot(tilde_Y1[:,1], 'b',label='lower-y')
    ax_sub.legend()
    ax_sub = ax[2,0]
    ax_sub.plot(np.absolute(tilde_Z1_DFT[:,0]), 'r',label='magnitude-x')
    ax_sub.legend()
    ax_sub = ax[2,1]
    ax_sub.plot(np.angle(tilde_Z1_DFT[:,0]), 'b',label='angle-x')
    ax_sub.legend()
    ax_sub = ax[3,0]
    ax_sub.plot(np.absolute(tilde_Z1_DFT[:,1]), 'r',label='magnitude-y')
    ax_sub.legend()
    ax_sub = ax[3,1]
    ax_sub.plot(np.angle(tilde_Z1_DFT[:,1]), 'b',label='angle-y')
    ax_sub.legend()
    fig.savefig('卦象2.png',dpi=100)

def illustration3():
    fig, ax = plt.subplots(1,1,figsize=(8,8))
    ax.plot(X1,Y1)
    fig.savefig('卦象3.png',dpi=100)


print('时')
dt = datetime.now(tz=None).microsecond%64
utils.GuaXiang(info_dict_list[dt]).print_info()
print('日')
dt = datetime.now(tz=None).toordinal()%64
utils.GuaXiang(info_dict_list[dt]).print_info()

