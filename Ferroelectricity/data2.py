from matplotlib import pyplot as plt
import numpy as np
from scipy import optimize

with open("data2.txt", 'r') as f:
    data = f.readlines()
V = []
prp = []
prn = []
pr = []
ecp = []
ecn = []
ec = []
psp = []
psn = []
ps = []
for line in data:
    line = line.split()
    V.append(int(line[0][:-1]))
    prp.append(float(line[1]))
    prn.append(-float(line[2]))
    pr.append((float(line[1]) - float(line[2]))/2)
	
    ecp.append(float(line[3]))
    ecn.append(-float(line[4]))
    ec.append((float(line[3]) - float(line[4]))/2)
    psp.append(float(line[5]))
    psn.append(-float(line[6]))
    ps.append((float(line[5]) - float(line[6]))/2)

plt.figure(num=0)
l1, = plt.plot(V,prp, 'o')
l2, = plt.plot(V,prn, 'o')
l3, = plt.plot(V,pr,'o')
def f(x, a1, b1):
    return a1*x + b1
a1, b1 = optimize.curve_fit(f, V, prp)[0]
a2, b2 = optimize.curve_fit(f, V, prn)[0]
a3, b3 = optimize.curve_fit(f, V, pr)[0]
V1 = np.arange(700,1075,25)
print(V,V1)
l4, = plt.plot(V,f(V1,a1,b1),'-')
l5, = plt.plot(V,f(V1,a2,b2),'-')
l6, = plt.plot(V,f(V1,a3,b3),'-')

plt.legend([l1, l2,l3,],[r'$P_r+$', r'$P_r-$', r'$P_r$'])
plt.savefig("last.png")

plt.figure(num=1)
l1, = plt.plot(V,ecp, 'o')
l2, = plt.plot(V,ecn, 'o')
l3, = plt.plot(V,ec, 'o')
#def f(x, a1, b1):
#    return a1*x + b1
a1, b1 = optimize.curve_fit(f, V, ecp)[0]
a2, b2 = optimize.curve_fit(f, V, ecn)[0]
a3, b3 = optimize.curve_fit(f, V, ec)[0]
V1 = np.arange(700,1075,25)
l4, = plt.plot(V,f(V1,a1,b1),'-')
l5, = plt.plot(V,f(V1,a2,b2),'-')
l6, = plt.plot(V,f(V1,a3,b3),'-')

plt.legend([l1, l2,l3,],[r'$E_c+$', r'$E_c-$', r'$E_c$'])
plt.savefig("last2.png")

plt.figure(num=2)
l1, = plt.plot(V,psp, 'o')
l2, = plt.plot(V,psn, 'o')
l3, = plt.plot(V,ps, 'o')
#def f(x, a1, b1):
#    return a1*x + b1
a1, b1 = optimize.curve_fit(f, V, psp)[0]
a2, b2 = optimize.curve_fit(f, V, psn)[0]
a3, b3 = optimize.curve_fit(f, V, ps)[0]
V1 = np.arange(700,1075,25)
l4, = plt.plot(V,f(V1,a1,b1),'-')
l5, = plt.plot(V,f(V1,a2,b2),'-')
l6, = plt.plot(V,f(V1,a3,b3),'-')

plt.legend([l1, l2,l3,],[r'$P_s+$', r'$P_s-$', r'$P_s$'])
plt.savefig("last3.png")



