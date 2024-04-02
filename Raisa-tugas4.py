#Program Daftar Belanja
print()
print("Selamat Datang di SunFlorist! ")
print("----------------------------------")
print("Kami menyediakan berbagai jenis bunga fresh.")
print("Selamat berbelanja!")
print("-------------------")
print("Daftar produk dan harga : ")
print("Mawar     : Rp.50.000/batang")
print("Matahari  : Rp.75.000/batang")
print("Tulip     : Rp.125.000/batang")
print("Lavender  : Rp.150.000/batang")
print("Orchid    : Rp.200.000/batang")
print("Promo Spesial !!! ")
print("Beli lebih dari 2 batang bunga mawar, diskon 25%")
print("Belanja lebih dari 500 ribu, dapat potongan harga 10%")
print('-------------------------------------')

print()
print("Kami menyediakan 5 jenis bunga, sesuai dengan daftar produk yang tertera")
j = int(input("Berapa jenis bunga yang ingin anda pesan? (1-5) : "))

while j not in range(1,6) :
    print("Input tidak sesuai permintaan. Mohon masukkan angka 1-5")
    j = int(input("Berapa jenis bunga yang ingin anda pesan? (1-5) : "))

if 1<=j<=5 :
    print('---------------------------------------------------')
    print("Silahkan masukkan jenis bunga yang ingin anda pesan")
    total_belanja=0 
    for jenis in range (1,j+1) :
        a = str(input(f"Jenis bunga {jenis} (Note:Masukkan nama bunga): ")). lower()
        while a not in ['mawar', 'matahari', 'tulip', 'lavender', 'orchid']:
            print('Note : Harap masukan nama bunga yang tersedia pada daftar produk')
            a = str(input(f"Jenis bunga {jenis} (Note:Masukkan nama bunga): ")). lower()
        b = int(input(f"Banyak batang untuk jenis {jenis} : "))
        while b <= 0 :
            print("Note : Harap masukan angka bulat positif")
            b = int(input(f"Banyak batang untuk jenis {jenis} : ")) 
        harga=0
        if a == 'mawar':
            if b >= 2:  
                diskon1 = (25/100) * (50000 * b)
                harga = 50000 * b - diskon1
            else:
                harga = 50000 * b
        elif a=='matahari' :
            harga = 75000*b
        elif a=='tulip' :
            harga = 125000*b
        elif a=='lavender' :
            harga = 150000*b
        elif a=='orchid' :
            harga = 200000*b
        print(f"Harga jenis {jenis}: Rp.", harga)
        total_belanja += harga 
    print('-------------------------------------------') 
    print("Total belanja anda : Rp.", total_belanja)
    if total_belanja > 500000 :
        diskon2 = (10/100) * total_belanja
        print('Potongan harga : Rp.',diskon2)
        print('Total bayaran : Rp.',total_belanja-diskon2)