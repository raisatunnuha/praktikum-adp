#Fungsi Untuk Menginput Data Sebanyak n
def banyak_data () :
    n = int(input('Masukkan jumlah data yang ingin diinput : '))
    data = []
    for i in range (1,n+1) :
        angka = int(input(f'Data ke-{i} : ')) 
        data.append(angka)
    return data
data_input = banyak_data()
print("Data      = ",data_input)
      
#Fungsi Untuk Menghitung Mean, Modus, Variance dari Data
def hitung_mean (data_input) :
    hitung = 0
    jumlah = 0
    for i in (data_input)  :
        jumlah += i
        hitung += 1
    mean = jumlah/hitung
    return mean
def hitung_modus (data_input) :
    nilai_max = data_input[0]
    for i in (data_input) :
        if i > nilai_max :
            nilai_max = i
    freq = [0] * (nilai_max+1)
    for i in (data_input) :
        freq[i] += 1
    freq_max = freq[0]
    for x in range(len(freq)):
        if freq[x] > freq_max:
            freq_max = freq[x]
    modus = []
    for x in range(len(freq)):
        if freq[x] == freq_max:
            modus.append(x)
    return modus
def hitung_variance (data_input) :
    sigma = 0
    for data in (data_input) :
        sigma += (data-hitung_mean(data_input))**2
    count = 0
    for i in (data_input) :
        count += 1
    variance = sigma/count
    return variance

#Fungsi Untuk Menampilkan Hasil dalam Format Tabel
def output(data_input) :
    a = str (hitung_mean(data_input))
    b = str (hitung_modus(data_input))
    c = str (hitung_variance(data_input))
    print('|  ' + 'mean' + ' '*(10-len('mean')) + '| ' + a + ' '*(19-len(a)) + ' |')
    print('|  ' + 'modus' + ' '*(10-len('modus')) + '| ' + b + ' '*(19-len(b)) + ' |')
    print('|  ' + 'variance' + ' '*(10-len('variance')) + '| ' + c + ' '*(19-len(c)) + ' |')
print()
output(data_input)