import os


def menuUtama():
    print("")
    print("PROGRAM PEMBELIAN BARANG DITOKO ONLINE")
    print("...................................................")
    print("""Nama barang yang dijual :
		1.pakaian
		2.kecantikan
        3.camping""")
    pilihan = int(input("Pilih barang yang ingin anda beli [1-5]:"))
    if (pilihan == 1):
        jenis = ("pakaian")
        print("""jenis pakaian yang dijual :
						1.baju kemeja dewasa
						2.baju kaos dewasa
						3.baju kemeja anak 
						4.baju kaos anak
						5.rok kain
						6.celana kain
						7.celan levis
						8.gamis
						9.rok levis""")
        print("""Harga barang :
						1.100.000,
						2.50.000,
						3.80.000,
						4.50.000,
						5.35.000,
						6.35.000,
						7.60.000,
						8.90.000,
						9.70.000""")
        pakaian = int(input("jenis pakaian yang anda beli : "))
        harga = [100000, 50000, 80000, 50000,
                 35000, 35000, 60000, 90000, 70000]
        if (pakaian == 1):
            harga = harga[0]
        elif (pakaian == 2):
            harga = harga[1]
        elif (pakaian == 3):
            harga = harga[2]
        elif (pakaian == 4):
            harga = harga[3]
        elif (pakaian == 5):
            harga = harga[4]
        elif (pakaian == 6):
            harga = harga[5]
        elif (pakaian == 7):
            harga = harga[6]
        elif (pakaian == 8):
            harga = harga[7]
        elif (pakaian == 9):
            harga = harga[8]
    if (pilihan == 2):
        jenis = "make up"
        print("""jenis barang yang dibeli
						1.lipstik
						2.eye liner
						3.maskara
						4.blus on
						5.pensil alis
						6.pelembab
						7.bedak
						8.eye shadow
						9.hair dryer
						10.lensa kontak
						11.krim wajah
						12.masker
						13.parfum
						14.kutek""")
        print("""harga barang 
								1.60.000,
								2.40.000,
								3.48.000,
								4.80.000,
								5.20.000,
								6.30.000,
								7.50.000,
								8.58.000,
								9.400.000,
								10.120.000,
								11.300.000,
								12.5.000,
								13.119.000,
								14.28.000""")
        make_up = int(input("jenis barang kecantikan yang anda beli : "))
        harga = [60000, 40000, 48000, 80000, 20000, 30000, 50000,
                 58000, 400000, 120000, 300000, 5000, 119000, 28000]
        if (make_up == 1):
            harga = harga[0]
        elif (make_up == 2):
            harga = harga[1]
        elif (make_up == 3):
            harga = harga[2]
        elif (make_up == 4):
            harga = harga[3]
        elif (make_up == 5):
            harga = harga[4]
        elif (make_up == 6):
            harga = harga[5]
        elif (make_up == 7):
            harga = harga[6]
        elif (make_up == 8):
            harga = harga[7]
        elif (make_up == 9):
            harga = harga[8]
        elif (make_up == 10):
            harga = harga[9]
        elif (make_up == 11):
            harga = harga[10]
        elif (make_up == 12):
            harga = harga[11]
        elif (make_up == 13):
            harga = harga[12]
        elif (make_up == 14):
            harga = harga[13]
    if (pilihan == 3):
        jenis = "camping"
        print("""jenis camping yang dibeli
						1.Tas
						2.Tenda
						3.Kompor mini
						4.gas
                        5.kursi/Bangku camping fc 300""")
        print("""harga barang
				1.2.000.000,
				2.5.000.000,
				3.3.000.000,
				4.3.50000,
				5.2.000.000,""")
        camping = int(input("jenis barang camping yang anda beli : "))
        harga = [2000000, 500000, 3000000, 350000,
                 2000000, 1000000, 700000, 500000]
        if (camping == 1):
            harga = harga[0]
        elif (camping == 2):
            harga = harga[1]
        elif (camping == 3):
            harga = harga[2]
        elif (camping == 4):
            harga = harga[3]
        elif (camping == 5):
            harga = harga[4]
        elif (camping == 6):
            harga = harga[5]
        elif (camping == 7):
            harga = harga[6]
        elif (camping == 8):
            harga = harga[7]

    print("Harga yang harus dibayar Rp."+str(harga))
    print("""jenis transaksi yang dipilih
				1.Bank,
				2.Indomart""")
    transaksi = input("transaksi jenis apa yang anda pilih 1/2 :")
    if (transaksi == 1):
        jenis = input("Bank")
    elif (transaksi == 2):
        jenis = input("Indomart")
    x = input("terima kasih sudah berbelanja ditoko kami :)")
    print("..............................................")
    if(input("mau lanjut?[Y/N] :") == "N" or "n"):
        exit()
    else:
        os.system


loop = True
while loop:
    menuutama()
