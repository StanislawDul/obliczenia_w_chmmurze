from cmath import pi
from wyzn_alfa import wyzn_alfa1
from wyzn_alfa import wyzn_alfa2
import math

f = open("dane_lotu.txt", "w")
f.write(f'Wielkosci stałe w trakcie lotu\n\n')

dt=0.1
g = 9.81
ro = 1.184
Mi = 0.095 #współczynnik oporu dla kół ok 10 cm

S = 0.35
m_to = 3

print(f'dt = {dt}\ng = {g}\nro = {ro}\nMi = {Mi}')
print(f'\nS = {S}\nm_to = {m_to}\n')
f.write(f'dt = {dt}\ng = {g}\nro = {ro}\nMi = {Mi}\n')
f.write(f'\nS = {S}\nm_to = {m_to}\n')
W0= m_to * g
CD0 = 0.07
Wydluzenie = 10
CLmax = 1.75
CLstart = 0.95 * CLmax
alfa_wzn = 8/360*2*pi
alfa_przel = -1/360*2*pi

#prędkość do startu
v_to = 1.05*((2*W0)/(ro*S*CLmax))**0.5

Rrot1 = v_to**2/0.15/9.81  #m
Rrot2 = Rrot1   #m 

print(f'\nW0 = {W0}\nCD0 = {CD0}\nWydluzenie  = {Wydluzenie}\nCLmax = {CLmax}\nCLstart = {CLstart}\nalfa_wzn = {alfa_wzn}\nalfa_przel = {alfa_przel}\nvto = {v_to}\nRrot1 = {Rrot1}\nRrot2 = {Rrot2}')
f.write(f'\nW0 = {W0}\nCD0 = {CD0}\nWydluzenie  = {Wydluzenie}\nCLmax = {CLmax}\nCLstart = {CLstart}\nalfa_wzn = {alfa_wzn}\nalfa_przel = {alfa_przel}\nvto = {v_to}\nRrot1 = {Rrot1}\nRrot2 = {Rrot2}\n\n')
# Initialisation
t = [0]
alfa = [0]
v = [0]
CL = [CLstart]
CD = [0]
Lift = [0]
Trust = [- 0.009*v[0]**2 - 0.1125*v[0] + 12.995]
Drag = [0]
Droll = [Mi * (W0 - Lift[0])]
a = [(Trust[0] - Droll[0]) / m_to]
H = [0]
s = [0]
sRozbieg = [0]

f.write(f'\nSymulacja misji2test\n')
print("Nr iteracji, czas, alfa, v, CL, CD, Lift, Trust, Drag, Droll, a, H, s, sRozbieg")
print(f'{0}, {t[0]}, {alfa[0]}, {v[0]}, {CL[0]}, {CD[0]} {Lift[0]}, {Trust[0]}, {Drag[0]}, {Droll[0]}, {a[0]}, {H[0]}, {s[0]}, {sRozbieg[0]}')

f.write("Nr iteracji, czas, alfa, v, CL, CD, Lift, Trust, Drag, Droll, a, H, s, sRozbieg\n")
f. write("0, " + str(t[0])+", "+ str(alfa[0])+", " + str(v[0]) + ", "+ str(CL[0]) + ", "+ str(CD[0]) + ", " + str(Lift[0]) + ", " + str(Trust[0]) + ", " + str(Drag[0]) + ", " + str(Droll[0]) + ", " + str(a[0]) + ", " + str(H[0]) + ", " + str(s[0]) + ", " + str(sRozbieg[0]) +"\n")
## Main loop

for i in range (1, 1801):
    t.append(t[i-1]+dt)
    v.append(v[i-1] + a[i-1]*dt)
    s.append(s[i-1] + v[i-1] * dt + a[i-1]*dt**2)
    if v[i-1] <= v_to:
        sRozbieg.append(sRozbieg[i-1] + v[i-1]*dt + a[i-1]*dt**2)
    else:
        sRozbieg.append(0)

    if t[i] <= 60:
        alfa.append(wyzn_alfa1(v[i], v_to, s[i], H[i-1], max(sRozbieg), Rrot1, alfa_wzn))
        #print(f'it = {i}, max(sRozbieg) = {max(sRozbieg)}')
    elif v[600] < v_to:
        alfa.append(wyzn_alfa2(H[i], s[i], s[601], alfa_wzn, Rrot2, alfa_przel))
    else:
        alfa.append(0) #to zostaje

    #CL
    if v[i] <= v_to:
        CL.append(CLstart)
    else:
        CL.append((2*W0*math.cos(alfa[i])) / (ro*S*v[i]**2))
    
    CD.append(CD0 + CL[i]**2 / (pi*0.8*Wydluzenie))

    Trust.append(-0.009*v[i]**2 - 0.1125*v[i] + 12.995)

    Lift.append((0.5*ro*v[i]**2)*S*CL[i])

    Drag.append((0.5*ro*v[i]**2)*S*CD[i])

    # Droll
    if W0*math.cos(alfa[i])-Lift[i] > 0.01: #0.01 by uniknąć błędu numerycznego
        Droll.append(Mi * (W0 - Lift[i]))
    else:
        Droll.append(0)


    if Trust[i] - Drag[i] - Droll[i] - math.sin(alfa[i])*W0 > 0:
        a.append((Trust[i] - Drag[i] - Droll[i]- math.sin(alfa[i])*W0) / m_to)
    else:
        a.append(0)
    
    # Wysokość
    H.append(H[i-1] + (s[i]-s[i-1])*math.sin((alfa[i]+alfa[i-1])/2))

    #print(f'{i}, {t[i]}, {alfa[i]}, {v[i]}, {CL[i]}, {CD[i]} {Lift[i]}, {Trust[i]}, {Drag[i]}, {Droll[i]}, {a[i]}, {H[i]}, {s[i]}, {sRozbieg[i]}')
    f. write(str(i) + ", " + str(t[i])+", "+ str(alfa[i])+", " + str(v[i]) + ", "+ str(CL[i]) + ", "+ str(CD[i]) + ", " + str(Lift[i]) + ", " + str(Trust[i]) + ", " + str(Drag[i]) + ", " + str(Droll[i]) + ", " + str(a[i]) + ", " + str(H[i]) + ", " + str(s[i]) + ", " + str(sRozbieg[i]) +"\n")

g = open("wyniki_lotu.txt", "w")
Rozbieg = max(sRozbieg[0:600])
Pulap = H[600]
Dystans = math.cos(alfa_przel) * (s[1800]-s[600])
print(f'Rozbieg = {Rozbieg}')
g.write(f'Rozbieg = {Rozbieg} m\n')
g.write(f'Pulap w chwili t=60s = {Pulap} m\n')   
g.write(f'Przebyty dystans = {Dystans} m\n')




