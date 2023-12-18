vd = {'key1' : 'Nilai 1', 
      'key2' : 'Nilai 2',
      'key3' : 'Nilai 3'
      }

Vl = ['Nilai1',
      'Nilai2',
      'Nilai3']

print(Vl[1])
print(vd['key2'])

print('\n')

data = {'nama' : 'Muhammad Heyzel Ikram', 
        'nim'  : '231031117',
        'lulus': False
        }
print(data)
# mengakses data
print(data['nama'])

#Mengupdate data
data.update({'lulus':True})
data['lulus'] = True # mengupdate
# data['Lulus'] = True # Tambah data

del data['nama'] # menghapus data

print(data)

print('\n')
biodata = {'nama'  : 'Muhammad Heyzel Ikram', 
       'umur'   : '18',
       'status' : 'mahasiswa',
       'prodi'  : 'sistem informasi',
       'nim'    : '231031117',
       'alamat' : 'jln garuda',
        'a.s'   : 'smk 2 pare pare',

       }
print(biodata['nama'])
print(biodata['umur'])
print(biodata['status'])
