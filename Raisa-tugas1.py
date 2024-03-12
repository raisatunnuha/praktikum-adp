print('---Menghitung Volume Bangun Ruang---')

print('A. Volume Kubus')
r = float(input('Panjang rusuk kubus (dalam dm) : '))
a = float(r*r*r)
print('Volume kubus adalah ',a, 'liter')

print('B. Volume Balok')
p = float(input('Panjang balok (dalam dm) : '))
l = float(input('Lebar balok (dalam dm)   : '))
t1 = float(input('Tinggi balok (dalam dm)  : '))
b = float(p*l*t1)
print('Volume Balok adalah ',b, 'liter')

print('C. Volume Kerucut')
j1 = float(input('Jari-jari lingkaran alas (dalam dm) : '))
t2 = float(input('Tinggi kerucut (dalam dm)           : '))
phi = 3.14
c = float(phi*j1*j1*t2/3)
print('Volume kerucut adalah ',c, 'liter')

print('D. Volume Bola')
j2 = float(input('Jari-jari bola (dalam dm) : '))
d = float(4*phi*j2*j2*j2/3)
print('Volume bola adalah ',d, 'liter')

print('E. Volume Tabung')
j3 = float(input('Jari-jari alas tabung (dalam dm) : '))
t3 = float(input('Tinggi tabung (dalam dm)         : '))
e = float(phi*j3*j3*t3)
print('Volume tabung adalah ',e, 'liter')