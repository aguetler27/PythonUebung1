# beispiel1.py
land = "AT"
blz = "38282"
konto = "3026713"
check = "96"

# ziel: formatierte IBAN ausgabe
# AT96 3828 2000 0302 6713
p1 = land + check
p2 = blz[0:4]
p3 = blz[4:5] + konto[0:3]
p4 = konto[4:8]
p5 = konto[9:12]
print (p1,p2,p3,p4,p5)

