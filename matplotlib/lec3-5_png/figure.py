
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 22:40:52 2017

@author: wsr
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure(num=1)
plt.plot(x,y1)

plt.figure(num=2,figsize=(8,5)) #在figure2里面打印两条线
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.figure(num=3,figsize=(8,5)) #在figure2里面打印两条线
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.xlim((-1,2)) #坐标轴范围
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y')
new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks) #坐标轴刻度
plt.yticks([-2,-1.8,-1,1.22,3],['really bad','bad','fair','good','excellent'])

plt.figure(num=4,figsize=(8,5)) #在figure2里面打印两条线
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.xlim((-1,2)) #坐标轴范围
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y')
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ bad$',r'$bad$',r'$fair$',r'$good$',r'$excellent$'])
#改了字体

plt.figure(num=5,figsize=(8,5)) #在figure2里面打印两条线
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.xlim((-1,2)) #坐标轴范围
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y')
plt.yticks([-2,-1.8,-1,1.22,3],[r'$\alpha$',r'$\beta$',r'$\gamma$',r'$\delta$',r'$\epsilon$'])
#改了字体
ax=plt.gca() #gca=get current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none') #spines表示边框

plt.figure(num=6,figsize=(8,5)) #在figure2里面打印两条线
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.xlim((-1,2)) #坐标轴范围
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y')
plt.yticks([-2,-1.8,-1,1.22,3],[r'$\alpha$',r'$\beta$',r'$\gamma$',r'$\delta$',r'$\epsilon$'])
#改了字体
ax=plt.gca() #gca=get current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none') #spines表示边框
#下面设置x，y轴的位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))# 'data'表示x轴与y轴交于y=0处
#ax.spines['left'].set_position(('data',0))
ax.spines['left'].set_position(('axes',0.5))# 'axes'表示x轴与y轴交于画面的0.5处（可取0-1）
#set_position参数还有outward等

plt.show()