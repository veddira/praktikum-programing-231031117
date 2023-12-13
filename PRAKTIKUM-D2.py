print()
print('praktikum-d\n\n')
print()

a = True
b = False
hasil = a and a
print('nilai',a,'and',a,'hasil',hasil)
hasil = a and b
print('nilai',a,'and',b,'hasil',hasil)
hasil = b and a
print('nilai',b,'and',a,'hasil',hasil)
hasil = b and b
print('nilai',b,'and',b,'hasil',hasil)

print('n==============ini or=================')
hasil = a or a
print('nilai',a,'or',a,'hasil',hasil)
hasil = a or b
print('nilai',a,'or',b,'hasil',hasil)
hasil = b or a
print('nilai',b,'or',a,'hasil',hasil)
hasil = b or b
print('nilai',b,'or',b,'hasil',hasil)

print('n==============ini not=================')
hasil = not a
print('hasil not',a,'adalah',hasil)
hasil = not b
print('hasil not',b,'adalah',hasil)

print('n==============ini xor=================')
hasil = a ^ a
print('nilai',a,'xor',a,'hasil',hasil)
hasil = a ^ b
print('nilai',a,'xor',b,'hasil',hasil)
hasil = b ^ a
print('nilai',b,'xor',a,'hasil',hasil)
hasil = b ^ b
print('nilai',b,'xor',b,'hasil',hasil)

print('n==============ini not=================')
hasil = not (a and a)
print('nilai',a,'nand',a,'hasil',hasil)
hasil = not (a and b)
print('nilai',a,'nand',b,'hasil',hasil)
hasil = not (b and a)
print('nilai',b,'nand',a,'hasil',hasil)
hasil = not (b and b)
print('nilai',b,'nand',b,'hasil',hasil)

print('n==============ini not=================')
hasil = not (a or a)
print('nilai',a,'nor',a,'hasil',hasil)
hasil = not (a or b)
print('nilai',a,'nor',b,'hasil',hasil)
hasil = not (b or a)
print('nilai',b,'nor',a,'hasil',hasil)
hasil = not (b or b)
print('nilai',b,'nor',b,'hasil',hasil)

print('n==============ini nxor=================')
hasil = a ^ a
print('nilai',a,'nxor',a,'hasil',not hasil)
hasil = a ^ b
print('nilai',a,'nxor',b,'hasil',not hasil)
hasil = b ^ a
print('nilai',b,'nxor',a,'hasil',not hasil)
hasil = b ^ b
print('nilai',b,'nxor',b,'hasil',not hasil)

print('n\================IS')
a = 5
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',a,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b=',hasil)

a = 6
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',a,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b=',hasil)

a = 6
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',a,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b=',hasil)

print('n\================= in')
nama = 'Bacharuddin Jusuf Habibie'
test = 'rud'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'bach'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ib'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('n\============== not in')
 # tugas buat nama menjadi nama lengkap masing masing
nama = 'MUHAMMAD HEYZEL IKRAM'
test = 'eL'
cek = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('n\=============== in')
data = ['institut',
        'Teknologi',
        'Bacharudin',
        'Jusuf',
        'Habibie',]

print('data adalah',data)
test1 = 'habibie'
test2 = 'Parepare'
test3 = 'Kampus'
test4 = 'Institut'
cek = test1 in data
print(test1,'terdapat di',nama,'adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di',nama,'adalah '+str(cek))
cek = test3 in data
print(test3,'terdapat di',nama,'adalah '+str(cek))
cek = test4 in data
print(test4,'terdapat di',nama,'adalah '+str(cek))

print('n\============== not in')
# tugas dengan cara yang sama buat operator not in

# INI OPERATOR BITWISE
a = 16 #isi dengan tanggal lahir
b = 1 #isi dengan bulan lahir
b += 80
print('\n ==================== AND')
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('---------------------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'biner adalah',format(c,'08b'))

print('\n ==================== OR')
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('---------------------------------------------OR')
c = a | b
print('Nilai',a,'&',b,'biner adalah',format(c,'08b'))

#tugas unruk operator XOR c = a^b
print('\n ==================== XOR')
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('---------------------------------------------XOR')
c = a ^ b
print('Nilai',a,'^',b,'biner adalah',format(c,'08b'))

#tugas untuk operator not, c = ~a
print('\n ==================== NOT a')
print('Nilai',a,'dalam biner  = ',format(a,'08b'))
print('---------------------------------------------NOT a')
c = ~a
print('Nilai','~',a,'biner adalah',format(c,'08b'))

#tugas untuk operator not, c = ~b
print('\n ==================== NOT b')
print('Nilai',b,'dalam biner  = ',format(b,'08b'))
print('---------------------------------------------NOT b')
c = ~b
print('Nilai','~',b,'biner adalah',format(c,'08b'))

#tugas untuk operator geser kanan, c = a >> 2
print('\n ==================== Geser Kanan')
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('--------------------------------------------- >> 2')
c = a >> 2
print('Nilai',a,'>> 2','biner adalah',format(c,'08b'))

#tugas untuk operator geser kiri, c = a << 2
print('\n ==================== Geser Kiri')
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('--------------------------------------------- << 2')
c = a << 2
print('Nilai',a,'<< 2','biner adalah',format(c,'08b'))

#tugas untuk operator not and, c = ~ (a & b)
print('\n ==================== not AND')
print('Nilai',a,'dalam biner          = ',format(a,'08b'))
print('Nilai',b,'dalam biner          = ',format(b,'08b'))
print('-------------------------------------------------not AND')
c = ~ (a & b)
print('Nilai','~(',a,'&',b,')','biner adalah',format(c,'08b'))

#tugas untuk operator not or, c = ~ (a | b)
print('\n ==================== not OR')
print('Nilai',a,'dalam biner          = ',format(a,'08b'))
print('Nilai',b,'dalam biner          = ',format(b,'08b'))
print('-------------------------------------------------not OR')
c = ~ (a | b)
print('Nilai','~(',a,'|',b,')','biner adalah',format(c,'08b'))

#tugas untuk operator not xor, c = ~ ( a ^ b )
print('\n ==================== not XOR')
print('Nilai',a,'dalam biner          = ',format(a,'08b'))
print('Nilai',b,'dalam biner          = ',format(b,'08b'))
print('-------------------------------------------------not XOR')
c = ~ (a ^ b)
print('Nilai','~(',a,'^',b,')','biner adalah',format(c,'08b'))

#tugas untuk operator not geser kanan, c = ~(a >> 2)
print('\n ==================== not Geser Kanan')
print('Nilai',a,'dalam biner         = ',format(a,'08b'))
print('---------------------------------------------not >> 2')
c = ~(a >> 2)
print('Nilai','~(',a,'>> 2)','biner adalah',format(c,'08b'))

#tugas untuk operator not geser kiri, c = ~(a << 2)
print('\n ==================== not Geser Kiri')
print('Nilai',a,'dalam biner         = ',format(a,'08b'))
print('---------------------------------------------not << 2')
c = ~(a << 2)
print('Nilai','~(',a,'<< 2)','biner adalah',format(c,'08b'))


