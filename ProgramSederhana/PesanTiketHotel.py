i = 1
while i == 1:
    print('\n')
    print('Selamat Datang di Hotel Agung Tower')
    print('Moto kami : Anda nyaman kami senang :)')
    print('Silahkan pilih kamar yang anda sukai')
    print(
    '''
    1. Jomblo Suite
    2. Couple Suite
    3. Deluxe Suite
    4. Keluar Program
    '''
    )
    pilihan = int(input('Silahkan Masukan Nomor Kamar Pilihan Anda: '))
    if pilihan == 1:
        print(
            '''
            -> Jomblo Suite
            adalah kamar yang pas bagi anda yang jomblo atau sendirian
            fasilitas yang tersedia:
            1. Kasur single bed
            2. TV 22 Inc
            3. WiFi
            4. Meja
            5. Kursi
            6. Lemari Pakaian
            7. AC

            HARGA = Rp. 356.500 / malam
            '''
        )
        print('')
        print('Apakah anda berminat memesan tipe kamar Jomblo?')
        print(
            '''
            1. Ya
            2. Tidak
            '''
        )
        pesan = int(input('Masukan Nomor Pilihan Anda: '))
        if pesan == 1:
            lamaMenginap = int(input('Berapa lama anda akan menginap: '))
            biaya = lamaMenginap*356500
            print('Total Biaya Menginap : ', biaya)
            pembayaran = int(input('Silahkan masukan uang anda: '))
            if pembayaran >= biaya:
                print('Uang anda: ', pembayaran)
                print('Kembalian: ', pembayaran - biaya)
                print('Terimakasih telah melakukan pemesanan')
                print('Apakah anda ingin mengulangi proses pemesanan?')
                print(
                    '''
                    1. Ya
                    2. Tidak
                    '''
                    )
                jawaban = int(input('Silahkan masukan nomor pilihan anda: '))
                if jawaban == 1:
                    i = 1
                else:
                    i = 0
            else:
                print('Mohon maaf uang yang nada masukan tidak mencu')
                print('Apakah anda ingin mengulangi proses pemesanan?')
                print(
                    '''
                    1. Ya
                    2. Tidak
                    '''
                    )
                jawaban = int(input('Silahkan masukan nomor pilihan anda: '))
                if jawaban == 1:
                    i = 1
                else:
                    i = 0
        elif pesan == 2:
            i = 1
        else:
            print('Pilihan tidak tersedia..')
            print('Apakah anda ingin mengulangi proses pemesanan?')
            print(
                '''
                1. Ya
                2. Tidak
                ''')
            jawaban = int(input('Silahkan masukan nomor pilihan anda: '))
            if jawaban == 1:
                i = 1
            else:
                i = 0
    elif pilihan == 2:
        print(
            '''
            -> Couple Suite
            adalah kamar yang pas bagi anda dan pasangan yang bernuansa romatis ala paris
            fasilitas yang tersedia:
            1. Kasur double bed
            2. LED TV 40 Inc
            3. WiFi
            4. Meja
            5. Kursi
            6. Lemari Pakaian
            7. AC
            8. Toilet dengan air panas
            9. bathtub

            HARGA = Rp. 674.500 / malam
            '''
        )
        print('')
        print('Apakah anda berminat memesan tipe kamar Couple?')
        print(
            '''
            1. Ya
            2. Tidak
            '''
        )
        pesan = int(input('Masukan Nomor Pilihan Anda: '))
        if pesan == 1:
            lamaMenginap = int(input('Berapa lama anda akan menginap: '))
            biaya = lamaMenginap*674000
            print('Total Biaya Menginap : ', biaya)
            pembayaran = int(input('Silahkan masukan uang anda: '))
            if pembayaran >= biaya:
                print('Uang anda: ', pembayaran)
                print('Kembalian: ', pembayaran - biaya)
                print('Terimakasih telah melakukan pemesanan')
                print('Apakah anda ingin mengulangi proses pemesanan?')
                print(
                    '''
                    1. Ya
                    2. Tidak
                    '''
                )
                jawaban = int(input('Silahkan masukan nomor pilihan anda: '))
                if jawaban == 1:
                    i = 1
                else:
                    i = 0
            else:
                print('Mohon maaf uang yang anda masukan tidak mencukupi')
                print('Apakah anda ingin mengulangi proses pemesanan?')
                print(
                    '''
                    1. Ya
                    2. Tidak
                    '''
                )
                jawaban = int(input('Silahkan masukan nomor pilihan anda: '))
                if jawaban == 1:
                    i = 1
                else:
                    i = 0
        elif pesan == 2:
            i = 1
        else:
            print('Pilihan tidak tersedia..')
            print('Apakah anda ingin mengulangi proses pemesanan?')
            print(
                '''
                1. Ya
                2. Tidak
                ''')
            jawaban = int(input('Silahkan masukan nomor pilihan anda: '))
            if jawaban == 1:
                i = 1
            else:
                i = 0
    elif pilihan == 3:
        print(
            '''
            -> Deluxe Suite
            adalah kamar yang pas bagi anda dan keluarga atau pasangan dengan ruangan luas dan fasilitas lengkap
            fasilitas yang tersedia:
            1. Kasur single bed
            2. TV 22 Inc
            3. WiFi
            4. Meja
            5. Kursi
            6. Lemari Pakaian
            7. AC
            8. Toilet dengan air panas
            9. bathtub
            10. Bufet Services
            11. Private Pool
            12. Fitnes Place

            HARGA = Rp. 1.056.900 / malam
            '''
        )
        print('')
        print('Apakah anda berminat memesan tipe kamar Deluxe?')
        print(
            '''
            1. Ya
            2. Tidak
            '''
        )
        pesan = int(input('Masukan Nomor Pilihan Anda: '))
        if pesan == 1:
            lamaMenginap = int(input('Berapa lama anda akan menginap: '))
            biaya = lamaMenginap*1056900
            print('Total Biaya Menginap : ', biaya)
            pembayaran = int(input('Silahkan masukan uang anda: '))
            if pembayaran >= biaya:
                print('Uang anda: ', pembayaran)
                print('Kembalian: ', pembayaran - biaya)
                print('Terimakasih telah melakukan pemesanan')
                print('Apakah anda ingin mengulangi proses pemesanan?')
                print(
                    '''
                    1. Ya
                    2. Tidak
                    '''
                )
                jawaban = int(input('Silahkan masukan nomor pilihan anda: '))
                if jawaban == 1:
                    i = 1
                else:
                    i = 0
            else:
                print('Mohon maaf uang yang anda masukan tidak mencukupi')
                print('Apakah anda ingin mengulangi proses pemesanan?')
                print(
                    '''
                    1. Ya
                    2. Tidak
                    '''
                )
                jawaban = int(input('Silahkan masukan nomor pilihan anda: '))
                if jawaban == 1:
                    i = 1
                else:
                    i = 0
        elif pesan == 2:
            i = 1
        else:
            print('Pilihan tidak tersedia..')
            print('Apakah anda ingin mengulangi proses pemesanan?')
            print(
                '''
                1. Ya
                2. Tidak
                ''')
            jawaban = int(input('Silahkan masukan nomor pilihan anda: '))
            if jawaban == 1:
                i = 1
            else:
                i = 0

    elif pilihan == 4:
        i = 0
    else:
        print('Pilihan yang anda masukan tidak tersedia')
        print('Apakah anda ingin mengulangi proses pemesanan?')
        print(
            '''
            1. Ya
            2. Tidak
            ''')
        jawaban = int(input('Silahkan masukan nomor pilihan anda: '))
        if jawaban == 1:
            i = 1
        else:
            i = 0

print('Terimakasih telah mencoba program saya :)')


