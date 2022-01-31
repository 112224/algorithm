Antenna = int(input())
Eyes = int(input())

Tf, Vf, Gf = False, False, False

if Antenna >= 3 and Eyes <= 4:
    Tf = True
if Antenna <= 6 and Eyes >= 2:
    Vf = True
if Antenna <= 2 and Eyes <= 3:
    Gf = True
if Tf:
    print("TroyMartian")
if Vf:
    print("VladSaturnian")
if Gf:
    print("GraemeMercurian")