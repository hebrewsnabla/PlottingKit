#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:55:54 2018

@author: jean
"""

import numpy as np
#import scipy as sp
from scipy import optimize
import matplotlib.pyplot as plt
import sys

ss = sys.argv[1]
#L = 0.0090
#d = 0.880

f = open("%s.txt"%ss,'r')
data = f.readlines()
xraw = []
yraw = []
for line in data:
    line = line.split()
    xraw.append(float(line[0]))
    yraw.append(float(line[1]))
N = len(xraw)
#----------floating correction
xave = np.mean(xraw)
yave = np.mean(yraw)

x = np.array(xraw) - np.ones(N) * xave
y = np.array(yraw) - np.ones(N) * yave

#-----------calc pr
#for i in range(N):
#    if abs(x[i]) < 0.01 and abs(y[i]) < 0.1:
#        x[i] = 0.0
#        y[i] = 0.0
prth = float(sys.argv[2])

prlist = []
prneg = []
for i in range(N):
    if abs(x[i]) < prth and y[i] > 0.0:
        prlist.append(y[i])
    if abs(x[i]) < prth and y[i] < 0.0:
        prneg.append(y[i])

sum = 0.0
index = 0
for l in prlist:
    sum += l
    index += 1
if index != 0:
    pr = sum/index
    #pr = round((sum / index) * 11.0 / (np.pi * ((d/2)**2)), 4)
prn = np.mean(prneg)
print(prlist, prneg)
print("P_r+ = %12.6f"%pr, "P_r- = %12.6f"%prn)

#-----------calc ec
ecth = float(sys.argv[3])
eclist = []
ecpos = []
for i in range(N):
    if abs(y[i]) < ecth and x[i] < 0.0:
        eclist.append(x[i])
    if abs(y[i]) < ecth and x[i] > 0.0:
        ecpos.append(x[i])
sum2 = 0.0
index2 = 0
for k in eclist:
    sum2 += k
    index2 += 1
if index != 0:
    ec = sum2/index2
    #ec = round((sum2 / index2) / L, 4)
ecp = np.mean(ecpos)
print(ecpos, eclist) 
print("E_c+ = %12.6f"%ecp, "E_c- = %12.6f"%ec)

#------------calc ps
psx = []; psy = []
psxneg = []; psyneg = []
xmax  = 0.0; ymax = 0.0
xmin = 0.0; ymin = 0.0
for i in range(N):
    if x[i] > xmax:
        xmax = x[i]
        ymax = y[i]
    if x[i] < xmin:
        xmin = x[i]
        ymin = y[i]

psth1 = float(sys.argv[4])
#psth2 = float(sys.argv[5])
#psth3 = float(sys.argv[6])

for i in range(N//2,0,-1):
    if x[i] > xmax*psth1:
        #if y[i] > ymax*psth3:
        psx.append(x[i])
        psy.append(y[i])
        if x[i] == xmax:
            break
for i in range(N-1,N//2,-1):
    if x[i] < xmin*psth1:
        #if y[i] < ymin*psth3:
        psxneg.append(x[i])
        psyneg.append(y[i])
        if x[i] == xmin: 
            break
def f1(x0, A, B):  
    return A*x0 + B
A1, ps = optimize.curve_fit(f1, psx, psy)[0]
A2, psn = optimize.curve_fit(f1, psxneg, psyneg)[0]
#ps = round(B1 * 11.0 / (np.pi * ((d/2)**2)), 4)
print("P_s+ = %12.6f"%ps, "P_s- = %12.6f"%psn)

g = open('data.txt', 'a')
out = [ss, ' ', str(pr), ' ', str(prn), ' ', str(ecp), ' ', str(ec), ' ', str(ps), ' ', str(psn), '\n']
for line in out:
    g.write(line)
g.close()

l1, = plt.plot(xraw, yraw, 'yo', markersize = 0.6)
l2, = plt.plot(x, y, 'ro', markersize = 0.6)
#plt.plot(psx,psy,'ko', markersize = 1.0)

fitx = np.arange(0, xmax +0.01 ,0.01)
l3, = plt.plot(fitx, f1(fitx, A1, ps), 'k-')
fitxn = np.arange(0, xmin-0.01, -0.01)
plt.plot(fitxn, f1(fitxn, A2, psn), 'k-')

plt.xlabel('                                               $E$ / V')
plt.ylabel('                                      $P$ / mV')
plt.legend(handles = [l1, l2, l3,], labels = ['raw data', 'translated data', 'fitting'], loc = 'best')

ax=plt.gca() #gca=get current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.savefig("%s.png"%ss)
