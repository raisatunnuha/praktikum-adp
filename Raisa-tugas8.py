#Dictionary and File Text

#Fungsi Untuk Menambahkan Data Film
def add(data_film) :
    with open ("data_film.txt", "a") as file :
        file.write(f"Judul Film : {data_film['j']}, Penulis skenario : {data_film['p']}, Sutradara : {data_film['s']}, Tahun rilis : {data_film['t']}, Negara asal : {data_film['n']}, Jumlah episode : {data_film['e']}\n")
    print("Data film berhasil ditambahkan.")

#Fungsi Untuk Menghapus Data Film
def delete(judul) :
    with open ("data_film.txt", "r") as file :
        lines = file.readlines()
    with open ("data_film.txt", "w") as file :  
        for line in lines :
            if line.split(":")[1].strip().split(",")[0].strip() != judul :
                file.write(line)
    print("Data film berhasil dihapus.")

#Fungsi Untuk Mengedit Data Film
def edit(judul, data_film) :
    with open ("data_film.txt", "r") as file :
        lines = file.readlines()
    with open ("data_film.txt", "w") as file :
        for line in lines :
            if line.split(":")[1].strip().split(",")[0].strip() == judul:
                file.write(f"Judul Film : {data_film['j']}, Penulis skenario : {data_film['p']}, Sutradara : {data_film['s']}, Tahun rilis : {data_film['t']}, Negara asal : {data_film['n']}, Jumlah episode : {data_film['e']}\n")
            else :
                file.write(line)
    print("Data film berhasil diedit")

#Fungsi Untuk Menampilkan Data Film
def show() :
    with open ("data_film.txt", "r") as file :
        datafilm = file.readlines()
    if datafilm :
        print()
        print ("Data film anda selama ini : ")
        for data in datafilm :
            print(f'- {data.strip()}')
    else :
        print ("Data film kosong")

#MAIN PROGRAM
while True :   
    print()
    print("Menu : ")
    print("1. Add movie data")
    print("2. Delete movie data")
    print("3. Edit movie data")
    print("4. Show all movie data")
    print("5. Exit the program")

    choice = int(input("Select menu (1-5) : "))
    if choice == 1 :
        print("\n~ Data Film ~")
        judul = input("Judul film : ")
        penulis = input("Nama penulis skenario : ")
        sutradara = input("Nama sutradara : ")
        tahun = input("Tahun rilis : ")
        negara = input("Negara asal : ")
        episode = input("Jumlah episode : ")
        data_film = {
            "j" : judul,
            "p" : penulis,
            "s" : sutradara,
            "t" : tahun,
            "n" : negara,
            "e" : episode
            }
        add(data_film)
    elif choice == 2 : 
        judul = input("Judul film yang akan dihapus : ")
        delete(judul)
    elif choice == 3 :
        judul = input("Judul film yang akan diubah : ")
        judulnew = input("Judul film yang baru : ")
        penulis = input("Nama penulis skenario yang baru : ")
        sutradara = input("Nama sutradara yang baru : ")
        tahun = input("Tahun rilis yang baru : ")
        negara = input("Negara asal yang baru : ")
        episode = input("Jumlah episode : ")
        data_film = {
            "j" : judulnew,
            "p" : penulis,
            "s" : sutradara,
            "t" : tahun,
            "n" : negara,
            "e" : episode
            }
        edit(judul, data_film)
    elif choice == 4 :
        show()
    elif choice == 5 :
        print ("Thank you for using this program")
        break
    else :
        print ("Your choice is invalid. Please enter number 1/2/3/4/5 to select the menu") 