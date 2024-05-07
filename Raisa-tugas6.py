print()
print('~~~ Operasi Perkalian dan Penjumlahan pada Matriks ~~~')
print()
print('Pilih Ukuran Matriks A')
ba = int(input('Banyak baris matriks A : '))
ka = int(input('Banyak kolom matriks A : '))
print('Pilih Ukuran Matriks B')
bb = int(input('Banyak baris matriks B : '))
kb = int(input('Banyak kolom matriks B : '))
while ba!=ka or ba!=bb or ka!=kb:
    print()
    print("NOTE : Matriks A dan B harus memiliki ukuran yang sama (nxn)")
    print('Pilih Ukuran Matriks A')
    ba = int(input('Banyak baris matriks A : '))
    ka = int(input('Banyak kolom matriks A : '))
    print('Pilih Ukuran Matriks B')
    bb = int(input('Banyak baris matriks B : '))
    kb = int(input('Banyak kolom matriks B : '))
print()

#Input Matriks A
print('Masukkan Elemen Matriks A')
matriksa = []
for i in range (1,ba+1) :
    barisa = []
    for j in range (1,ka+1) :
        n1 = int(input(f'Baris ke-{i}, kolom ke-{j} : '))
        barisa.append(n1)
    matriksa.append(barisa)

#Input Matriks B
print('Masukkan Elemen Matriks B')
matriksb = []
for i in range (1,bb+1) :
    barisb = []
    for j in range (1,kb+1) :
        n2 = int(input(f'Baris ke-{i}, kolom ke-{j} : '))
        barisb.append(n2)
    matriksb.append(barisb)

#Mencari Matriks C (hasil kali matriks A dan B)    
matriksc = []
for i in range (ba) :
    barisc = []
    for j in range (kb) :
        hasilkali = 0
        for k in range (ka) :
            hasilkali += matriksa[i][k]*matriksb[k][j]
        barisc.append(hasilkali)
    matriksc.append(barisc)

#Mencari A Transpose 
at = []
for i in range (ka) :
    barisat = []
    for j in range (ba) :
        barisat.append(matriksa[j][i])
    at.append(barisat)
#Mencari B Transpose
bt = []
for i in range (kb) :
    barisbt = []
    for j in range (bb) :
        barisbt.append(matriksb[j][i])
    bt.append(barisbt)

#Mencari Matriks D (hasil penjumlahan matriks A transpose dan B transpose)
matriksd = []
for i in range (ka) :
    barisd = []
    for j in range (ba) :
        hasiljumlah = at[i][j] + bt[i][j]
        barisd.append(hasiljumlah)
    matriksd.append(barisd)

print()
print("Matriks A : ",matriksa)
print("Matriks B : ",matriksb)
print("Hasil Perkalian Matriks A dan Matriks B : ")
print("Matriks C : ",matriksc)
print("Hasil Penjumlahan Matriks A Transpose dan B Transpose :")
print("Matriks D : ", matriksd)