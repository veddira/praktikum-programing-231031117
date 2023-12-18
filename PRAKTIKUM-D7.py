pwd_benar = 'heyzel'
a = True
limit = 3
i = 0
while a:
    i += 1
    pwd = input('masukkan password: ')
    if pwd == pwd_benar:
        print('password benar! selamat anda login')
        a = False
    else:        
        print('password salah!')
        if i == limit:          
            print('sayang sekali kesempatan anda habis!!!')
            a = False
        else:
            print(f'kesempatan anda tersisa {limit-i} kali')

# tugas = buat password berlapis 3
# jika salah = password salah, anda gagal pada halaman 1
# jika salah = password salah, anda gagal pada halaman 2
# jika salah = password salah, anda gagal pada halaman 3
# jika benar pertama = password benar, selamat datang di halaman 1
# jika benar kedua   = password benar, selamat datang di halaman 2
# jika benar ketiga  = password benar, selamat datang di halaman 3

# tiap halaman, memiliki kesempatan 3 kali masukkan password
