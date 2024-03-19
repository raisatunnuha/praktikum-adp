#Program Pesan-Antar Makanan Online
print('  ')
print('===== "HALO, Selamat Datang!" =====')
print('  ')
print('Berikut adalah menu yang tesedia di restaurant kami : ')
print('1. PAKET A     >>     Rp.25.000')
print('2. PAKET B     >>     Rp.30.000')
print('3. PAKET C     >>     Rp.45.000')
print('  ')
p = str(input('Mau pesan paket apa ? (A,B,atau C) : ')).lower()
if p!="a" and p!='b' and p!='c' : 
    print("Note : Dimohon kepada customer untuk hanya mengetik huruf A, a, B, b, C, atau c saja")
    p = str(input('Mau pesan paket apa ? (A,B,atau C) : ')).lower()
a = 25000
b = 30000
c = 45000
print('  ')
j = float(input('Jarak rumah bapak/ibuk ke restaurant kami (Note : dalam meter) = '))
if j < 0 :
    print('Note : masukkan jarak dalam bilangan positif')
    j = float(input('Jarak rumah bapak/ibuk ke restaurant kami (Note : dalam meter) = '))
if 0<=j<500 and p=='a' :
    t1 = a+0
    print('Total harga pesanan anda : Rp.',t1)
    print('Terimakasih! Pesanan akan segera kami antar. ')
elif 0<=j<500 and p=='b' :
    t2 = b+0
    print('Total harga pesanan anda : Rp.',t2)
    print('Terimakasih! Pesanan akan segera kami antar. ')
elif 0<=j<500 and p=='c' :
    t3 = c+0
    print('Total harga pesanan anda : Rp.',t3)
    print('Terimakasih! Pesanan akan segera kami antar. ')
elif 500<=j<=1500 and p=='a' :
    t4 = a+10000
    print('Total harga pesanan anda : Rp.',t4)
    print('Terimakasih! Pesanan akan segera kami antar. ')
elif 500<=j<=1500 and p=='b' :
    t5 = b+10000
    print('Total harga pesanan anda : Rp.',t5)
    print('Terimakasih! Pesanan akan segera kami antar. ')
elif 500<=j<=1500 and p=='c' :
    t6 = c+10000
    print('Total harga pesanan anda : Rp.',t6)
    print('Terimakasih! Pesanan akan segera kami antar. ')
elif j>1500 and p=='a' :
    t7 = a+20000
    print('Total harga pesanan anda : Rp.',t7)
    print('Terimakasih! Pesanan akan segera kami antar. ')
elif j>1500 and p=='b' :
    t8 = b+20000
    print('Total harga pesanan anda : Rp.',t8)
    print('Terimakasih! Pesanan akan segera kami antar. ')
elif j>1500 and p=='c' :
    t9 = c+20000
    print('Total harga pesanan anda : Rp.',t9)
    print('Terimakasih! Pesanan akan segera kami antar. ')
else : 
    print('Harap masukan huruf/angka sesuai permintaan program')