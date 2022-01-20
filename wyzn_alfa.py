def wyzn_alfa1(v, v_to, s, H, sRozbiegu, Rrot1, alfa_wzn):

    if v < v_to:
        return 0 
    else:
        if (s-sRozbiegu)/Rrot1 < alfa_wzn:
            return (s-sRozbiegu)/Rrot1
            #JEŻELI(N9<100; Z$5; 0))); JEŻELI(N$603<100; JEŻELI(Z$5-(P10-P$603)/AC$3>AC$5; Z$5-(P10-P$603)/AC$3; AC$5); JEŻELI(0-(P10-P$603)/AC$3>AC$5; 0-(P10-P$603)/AC$3; AC$5)))
        else:
            if H < 100:
                return alfa_wzn
            else:
                return 0
            
def wyzn_alfa2(H, s, s60, alfa_wzn, Rrot2, alfa_przel):
    if H<100:
        if alfa_wzn-(s-s60)/Rrot2 > alfa_przel:
            return alfa_wzn-(s-s60)/Rrot2 #AC$5); JEŻELI(0-(P11-P$603)/AC$3>AC$5; 0-(P11-P$603)/AC$3; AC$5)))
        else:
            return  alfa_przel
    else:
        if 0-(s-s60)/Rrot2>alfa_przel:
            return 0-(s-s60)/Rrot2
        else:
            return alfa_przel
    
    
