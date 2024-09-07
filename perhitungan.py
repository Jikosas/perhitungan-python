def kalkulator():
    print("Selamat datang di kalkulator Python")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    operasi = input("Masukkan pilihan operasi (1/2/3/4): ")
    bilangan_1 = float(input("Masukkan bilangan pertama: "))
    bilangan_2 = float(input("Masukkan bilangan kedua: "))

    if operasi == '1':
        hasil = bilangan_1 + bilangan_2
        print(f"Hasil dari {bilangan_1} + {bilangan_2} adalah {hasil}")
    elif operasi == '2':
        hasil = bilangan_1 - bilangan_2
        print(f"Hasil dari {bilangan_1} - {bilangan_2} adalah {hasil}")
    elif operasi == '3':
        hasil = bilangan_1 * bilangan_2
        print(f"Hasil dari {bilangan_1} * {bilangan_2} adalah {hasil}")
    elif operasi == '4':
        if bilangan_2 != 0:
            hasil = bilangan_1 / bilangan_2
            print(f"Hasil dari {bilangan_1} / {bilangan_2} adalah {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        print("Pilihan operasi tidak valid.")

kalkulator()
