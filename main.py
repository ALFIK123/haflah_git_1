import os


def menuUtama():
    print("")
    print("PROGRAM PEMBELIAN BARANG DITOKO ONLINE")
    print("...................................................")
    print("""Nama barang yang dijual :
		1.pakaian
		2.elektroniks
		3.tas     
		4.sepatu/sandal
		5.kecantikan""")
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
        jenis = "elektronik"
        print("""jenis elektronik yang dibeli
						1.Tv
						2.Kulkas
						3.Ac
						4.penanak nasi
						5.Mesin cuci
						6.Microwave
						7.kipas angin
						8.VCD Player""")
        print("""harga barang
				1.2.000.000,
				2.5.000.000,
				3.3.000.000,
				4.3.50000,
				5.2.000.000,
				6.1.000.000,
				7.700.000,
				8.500.000""")
        elektronik = int(input("jenis barang elektronik  yang anda beli : "))
        harga = [2000000, 500000, 3000000, 350000,
                 2000000, 1000000, 700000, 500000]
        if (elektronik == 1):
            harga = harga[0]
        elif (elektronik == 2):
            harga = harga[1]
        elif (elektronik == 3):
            harga = harga[2]
        elif (elektronik == 4):
            harga = harga[3]
        elif (elektronik == 5):
            harga = harga[4]
        elif (elektronik == 6):
            harga = harga[5]
        elif (elektronik == 7):
            harga = harga[6]
        elif (elektronik == 8):
            harga = harga[7]
    if (pilihan == 3):
        jenis = "tas"
        print("""jenis tas yang dibeli
						1.Tas anak anak
						2.Tas jalan 
						3.Tas ransel
						4.Tas sekolah anak
						5.Tas sekolah dewasa
						6.Totebag
						7.Handbag""")
        print("""harga barang 
								1.50.000,
								2.115.000,
								3.100.000,
								4.150.000,
								5.200.000
								6.65.000
								7.150.000""")
        tas = int(input("jenis barang tas  yang anda beli : "))
        harga = [50000, 115000, 100000, 150000, 200000, 65000, 150000]
        if (tas == 1):
            harga = harga[0]
        elif (tas == 2):
            harga = harga[1]
        elif (tas == 3):
            harga = harga[2]
        elif (tas == 4):
            harga = harga[3]
        elif (tas == 5):
            harga = harga[4]
        elif (tas == 6):
            harga = harga[5]
        elif (tas == 7):
            harga = harga[6]
    if (pilihan == 4):
        jenis = "sepatu/sandal"
        print("""jenis sepatu yang dibeli
						1.sepatu sekolah sd
						2.sepatu sekolah smp
						3.sepatu sma
						4.sepatu pantofel
						5.sepatu kets
						6.sepatu flat
						7.sepatu gunung
						8.sepatu olahraga
						9.sendal jalan pria
						10.sendal jalan wanita""")
        print("""harga barang 
							1.60.000,
							2.100.000,
							3.120.000,
							4.100.000,
							5.70.000,
							6.50.000,
							7.200.000,
							8.250.000,
							9.70.000,
							10.80.000""")
        sepatu = int(input("jenis barang sepatu  yang anda beli : "))
        harga = [60000, 100000, 120000, 100000, 70000,
                 50000, 200000, 250000, 700000, 80000]
        if (sepatu == 1):
            harga = harga[0]
        elif (sepatu == 2):
            harga = harga[1]
        elif (sepatu == 3):
            harga = harga[2]
        elif (sepatu == 4):
            harga = harga[3]
        elif (sepatu == 5):
            harga = harga[4]
        if (sepatu == 6):
            harga = harga[5]
        elif (sepatu == 7):
            harga = harga[6]
        elif (sepatu == 8):
            harga = harga[7]
        elif (sepatu == 9):
            harga = harga[8]
        elif (sepatu == 10):
            harga = harga[9]
    if (pilihan == 5):
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
