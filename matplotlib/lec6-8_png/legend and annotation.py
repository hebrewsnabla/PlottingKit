# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:43:17 2017

@author: wsr
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure(num=7,figsize=(8,5)) #在figure2里面打印两条线
plt.plot(x,y2,label='p')
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='q')
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
ax.spines['left'].set_position(('axes',0.5))# 'axes'表示x轴与y轴交于画面的0.5处（可取0-1）
plt.legend(labels=['ppp','qqq'],loc='upper right') # 图例

plt.figure(num=8,figsize=(8,5)) #在figure2里面打印两条线
plt.plot(x,y2,label='p')
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='q')
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
ax.spines['left'].set_position(('data',0))# 'axes'表示x轴与y轴交于画面的0.5处（可取0-1）
plt.legend(labels=['ppp','qqq'],loc='best') # 图例
#best表示自动选择最佳位置
x0=0.5
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='b') # scatter 散点图，s=size
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)# k=black,--表示虚线，lw=linewidth

plt.annotate(r'$this$ $is$ $an$ $annotation$',xy=(x0,y0),xycoords='data',xytext=(+20,-20),textcoords='offset points')


plt.figure(num=9,figsize=(8,5)) #在figure2里面打印两条线
plt.plot(x,y2,label='p')
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='q')
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
ax.spines['left'].set_position(('data',0))# 'axes'表示x轴与y轴交于画面的0.5处（可取0-1）
plt.legend(labels=['ppp','qqq'],loc='best') # 图例
#best表示自动选择最佳位置
x0=0.5
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='b') # scatter 散点图，s=size
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)# k=black,--表示虚线，lw=linewidth

plt.annotate(r'$this$ $is$ $an$ $annotation$',xy=(x0,y0),xycoords='data',xytext=(+20,-50),textcoords='offset points',
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.2'))


plt.figure(num=10,figsize=(8,5)) #在figure2里面打印两条线
plt.plot(x,y2,label='p')
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='q')
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
ax.spines['left'].set_position(('data',0))# 'axes'表示x轴与y轴交于画面的0.5处（可取0-1）
plt.legend(labels=['ppp','qqq'],loc='best') # 图例
#best表示自动选择最佳位置
x0=0.5
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='b') # scatter 散点图，s=size
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)# k=black,--表示虚线，lw=linewidth

plt.text(-0.5,1.5,r'$this\ is\ a\ text$',
         fontdict={'size':16,'color':'r'})

plt.show()