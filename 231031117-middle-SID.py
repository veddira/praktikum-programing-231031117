'''
Misalkan anda diberikan tugas untuk membuat program struk pembelian pada kasir di perusahaan alat-alat komputer. Pilih 5 barang Alat Komputer dengan harga masing-masing barang kemudian buatkan program dan ouputnya seperti berikut.

- Buat list data perusahaan
mdata = [PT. XYZ Komputer,
        JL. BALAIKOTA NO.1,
        Kota Parepare,
        Nama Lengkap,
        mahasiswa@ith.ac.id,
        Nama Kasir,
        25 Oktober 2023]
(NOTED: ubah Nama Lengkap, e-mail, Nama Kasir, Tanggal-Bulan-Tahun Lahir)

- Buat Nested list untuk 5 barang:

djual = [['D0001','D0002','D0003','D0004','D0005'],
        ['Barang1','Barang2','Barang3','Barang4','Barang5'],
        [15,5,75,3,10],
        [3,3,3,3,3]]
(NOTED: ubah nama barang dan harga barang sesuai keinginan)

- Hasil Runing
                                 PT. XYZ KOMPUTER
                          JL. BALAIKOTA NO.2 KOTA PAREPARE
                             e-Mail: mahasiswa@ith.ac.id


MANAJER           : Nama Lengkap
KASIR             : Nama Kasir
Tanggal Pembelian : 25 Oktober 2023
|--     16    --|--       19      --|--     15    --|--  8 --|--    14    --| 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
No. Kode Barang |    Nama Barang    |   H. Satuan   | Jumlah |     Total    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1   D1101       | Barang1           |      Rp15000,-|    3   |     Rp45000,-|
2   D1102       | Barang2           |       Rp5000,-|    3   |     Rp15000,-|
3   D1103       | Barang3           |      Rp50000,-|    3   |    Rp150000,-|
4   D1104       | Barang4           |       Rp3000,-|    3   |     Rp15000,-|
5   D1105       | Barang5           |      Rp10000,-|    3   |     Rp30000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                    SUBTOTAL:           15   |    Rp245000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Summary:
Harga tertinggi adalah    : Rp50000,-  (D1103 - Barang3)
Harga terendah  adalah    : Rp3000,-   (D1104 - Barang4)
Harga rata-rata pembelian : Rp ,-
                                                   Parepare, 25 Oktober 2023
                                          



                                                         NAMA LENGKAP      
                                                         ------------
                                                            MANAJER

'''


# Write your code in below!

print('''
Nama\t\t: Muhammad Heyzel Ikram
NIM\t\t: 231031117
Nomor Komputer\t: 07
Kelas\t\t: Sistem Informasi D''')

#Answer in below

mdata = ['PT. XYZ Komputer',
        'JL. BALAIKOTA NO.1',
        'Kota Parepare',
        'Muhammad Heyzel Ikram',
        'Heyzel@ith.ac.id',
        'Muhammad Heyzel Ikram',
        '24 jun 2005']

djual = [['D0001','D0002','D0003','D0004','D0005'],
        ['kopi','susu','ayam','air','roti'],
        [15,5,50,3,10],
        [3,3,3,3,3]]
r = 1000
sp = 77
                                 # PT. XYZ KOMPUTER
print(mdata[0].center(72))
print(mdata[1].center(72))
print(mdata[4].center(72))
print('\n')
print(f'''MANAJER           : {mdata[3]}
KASIR             : {mdata[-2]}
Tanggal Pembelian : {mdata[-1]}''')
print('-'*(77))
print('No. Kode Barang'.ljust(16)+'|'+'Nama Barang'.center(19)+'|'+'H. Satuan'.center(15)+'|'+'Jumlah'.center(8)+'|'+'Total'.center(14)+'|')
print('-'*(77))

print(f'1.  {djual[0][0]}'.ljust(16)+'|'+f' {djual[1][0]}'.ljust(19)+'|'+f'Rp{djual[2][0]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*djual[2][0]*r},-'.rjust(14)+'|')
print(f'2.  {djual[0][1]}'.ljust(16)+'|'+f' {djual[1][1]}'.ljust(19)+'|'+f'Rp{djual[2][1]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*djual[2][1]*r},-'.rjust(14)+'|')
print(f'3.  {djual[0][2]}'.ljust(16)+'|'+f' {djual[1][2]}'.ljust(19)+'|'+f'Rp{djual[2][2]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*djual[2][2]*r},-'.rjust(14)+'|')
print(f'4.  {djual[0][3]}'.ljust(16)+'|'+f' {djual[1][3]}'.ljust(19)+'|'+f'Rp{djual[2][3]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*djual[2][3]*r},-'.rjust(14)+'|')
print(f'5.  {djual[0][4]}'.ljust(16)+'|'+f' {djual[1][4]}'.ljust(19)+'|'+f'Rp{djual[2][4]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp{3*djual[2][4]*r},-'.rjust(14)+'|')

print('-'*(77))
harga_satuan = (djual[2][0]+djual[2][1]+djual[2][2]+djual[2][3]+djual[2][4])*r
total_jumlah = sum(djual[3])
total_hasil = (djual[2][0]+djual[2][1]+djual[2][2]+djual[2][3]+djual[2][4])*r*3
print(f'subtotal: |     Rp{harga_satuan},-|  {total_jumlah}  | Rp{total_hasil},-|'.rjust(77))

print('-'*77)
rata_rata = (sum(djual[2]) / total_jumlah)*3*r
print(f'''Summary:
       Harga tertinggi adalah    : Rp{r*max(djual[2])},- ({djual[0][2]} - {djual[1][2]})
       Harga terendah adalah     : Rp{r*min(djual[2])},- ({djual[0][3]} - {djual[1][3]})
       Harga rata-rata adalah    : Rp{float(rata_rata):.2f}
             ''')
print('\n')


nama_kota = mdata[2]
tanggal = mdata[-1]
gabung = (nama_kota+','+tanggal).rjust(sp)
print(gabung)
print('\n'*2)
nama = mdata[3]
strip_akhir  = '-'*12
print(nama.rjust(71))
print(strip_akhir.rjust(70))
print('MANAJER'.rjust(68))



                        #   JL. BALAIKOTA NO.2 KOTA PAREPARE
                        #      e-Mail: mahasiswa@ith.ac.id 

