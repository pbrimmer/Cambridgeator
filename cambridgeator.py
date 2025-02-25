import numpy as np
import matplotlib.pyplot as plt
import sys

#This code is intended to reproduce the Brusselator model.
#I call it the "Cambridgeator" not because it is original; it's just
#the Brusselator model. I call it that because it's part of
#Cambridge's PSLU course. You can read about the Brusselator
#and the much more realistic Oregonator from:

#Prigogine, I.; Lefever, R. (1968-02-15). "Symmetry Breaking Instabilities 
#in Dissipative Systems. II". The Journal of Chemical Physics. 48 (4): 
#1695–1700. doi:10.1063/1.1668896

#Field, R.J. and Noyes, R.M., 1977. Oscillations in chemical systems. 18. 
#Mechanisms of chemical oscillators: Conceptual bases. 
#Accounts of Chemical Research, 10(6), pp.214-221.

#This brilliant sequence is an autocatylitic set (is autocatalysis
#required for chemical oscillators?) consisting of only four reactions.

#The reactions are:

#A -> X, k1
#X + X + Y -> X + X + X, k2
#B + X -> Y + D, k3
#X -> E, k4

t = 0.0       #initial time, t = 0s

count = 0
cmax = 50000      #Maximum number of steps

tmax = 100.0      #Maximum time

alpha = 0.2     #Difference between dt and the chemical timescale.
                #SHOULD BE < 0.5 to keep the Courant condition!

k1 = 1.0      #Rate constant for A -> X
k2 = 1.0      #Rate constant for X + X + Y -> X + X + X
k3 = 1.0      #Rate constant for B + X -> Y + D
k4 = 1.0      #Rate constant for X -> E

A0 = 1.0        #Initial concentration of A
B0 = 1.0        #Initial concentration of B
X0 = 0.0        #Initial concentration of X
Y0 = 0.0        #Initial concentration of Y
D0 = 0.0        #Initial concentration of D
E0 = 0.0        #Initial concentration of E

n = A0 + B0 + X0 + Y0 + D0 + E0     #Total concentration, sum of A+B+X+Y+D+E

#Set the old values.
Aold = A0
Bold = B0
Xold = X0
Yold = Y0
Dold = D0
Eold = E0

#Generate the arrays.
#AN IMPROVEMENT FOR THE FUTURE: Only save some entries, so these arrays don't kill memory.
tdat = np.array([t])
Adat = np.array([A0])
Bdat = np.array([B0])
Xdat = np.array([X0])
Ydat = np.array([Y0])
Ddat = np.array([D0])
Edat = np.array([E0])

while t < tmax and count < cmax:

    #Initiate A and B

    A = Aold
    B = Bold
    X = Xold
    Y = Yold
    D = Dold
    E = Eold

    #Find the rates

    dA_dt = 0.0
    dB_dt = 0.0
    dX_dt = k1*A + k2*X*X*Y - k3*B*X - k4*X
    dY_dt = -k2*X*X*Y + k3*B*X
    dD_dt = k3*B*X
    dE_dt = k4*X

    #Figure out the timestep (loosely based on Courant conditions)

    RA = np.abs(dA_dt)
    RB = np.abs(dB_dt)
    RX = np.abs(dX_dt)
    RY = np.abs(dY_dt)
    RD = np.abs(dD_dt)
    RE = np.abs(dE_dt)

    dtmin = 1e-2*n/(np.max(np.array([RA,RB,RX,RY,RD,RE])))

    taumin = dtmin

    dt = alpha*taumin

    #Update the new values

    Anew = (Aold + dA_dt*dt)
    Bnew = (Bold + dB_dt*dt)
    Xnew = (Xold + dX_dt*dt)
    Ynew = (Yold + dY_dt*dt)
    Dnew = (Dold + dD_dt*dt)
    Enew = (Eold + dE_dt*dt)

    #step forward with time
    t += dt
    count += 1

    #Keep record of the new values
    #Need a more clever implementation here to give active memory a break!
    tdat = np.append(tdat,t)
    Adat = np.append(Adat,Anew) 
    Bdat = np.append(Bdat,Bnew)
    Xdat = np.append(Xdat,Xnew)
    Ydat = np.append(Ydat,Ynew)
    Ddat = np.append(Ddat,Dnew)
    Edat = np.append(Edat,Enew)

    #Copy over new to old

    Aold = Anew
    Bold = Bnew
    Xold = Xnew
    Yold = Ynew
    Dold = Dnew
    Eold = Enew

#Plot the output chemistry. It can be worth exploring changes in species commented out. There are prebiotic implications for these choices.

#Concentration (A,B,X,Y,D,E) vs. time (s).

#plt.plot(tdat,Adat,label='[A]')
#plt.plot(tdat,Bdat,label='[B]')
plt.plot(tdat,Xdat,label='[X]')
plt.plot(tdat,Ydat,label='[Y]')
#plt.plot(tdat,Ddat,label='[D]')
#plt.plot(tdat,Edat,label='[E]')

#plt.xscale('log')
#plt.yscale('log')

plt.xlabel('t (s)')
plt.ylabel('concentration (a.u.)')

plt.legend()

plt.savefig('./ChemTime.pdf',bbox_inches='tight')

plt.clf()

#Concentration of X vs concentration of Y.
plt.plot(Xdat,Ydat,'k-')
plt.xlabel('[X]')
plt.ylabel('[Y]')

plt.savefig('./ChemParam.pdf',bbox_inches='tight')
