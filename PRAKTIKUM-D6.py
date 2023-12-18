a = True

while a:
    jawab = input('Apakah Ingin Lanjutkan? (y/n)')
    if jawab == 'y':
        print('Terima Kasih')
        a = True
    elif jawab == 'n':
        print('samapai jumpa')
        a = False
    else:
        print('cepat jawab -_-')
        a = True