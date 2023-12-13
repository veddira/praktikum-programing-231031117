import random

players = ["Player 1", "Player 2", "Player 3", "Player 4"]
print('Selamat datang di game truth or dare\n')
print('''Aturan Permainan:
1. Pemain berjumlahkan 4 orang.
2. Terdapat 2 opsi yaitu truth untuk kebenaran dan dare untuk tantangan.
3. Pemain yang terpilih berhak memilih salah satu dari 2 opsi.
4. ketik iya untuk lanjut bermain.
5. ketik tidak untuk berhenti bermain.''')
print(input('\nTekan tombol "Enter" untuk memulai permainan'))
# looping program berjalan
while True:
    player_terpilih = random.choice(players)

    # List untuk truth
    truths = [
        "Jika kamu bisa menjadi binatang, kamu ingin menjadi apa?",
        "Apa hal paling aneh yang pernah kamu lakukan?",
        "Jika kamu bisa memiliki satu kekuatan super, apa yang kamu pilih?",
        "Jika kamu harus makan satu jenis makanan selama sebulan penuh, apa yang akan kamu pilih?",
        "Apa kebiasaan terburuk yang ingin kamu hilangkan, tapi sulit dilakukan?",
        "Apa hal paling gila yang pernah kamu beli?",
        "Jika kamu memiliki waktu satu hari untuk menjalani kehidupan di masa depanmu, apa yang ingin kamu lihat?",
        "Jika kamu bisa memiliki obrolan pribadi dengan satu tokoh sejarah, siapa yang akan kamu pilih dan mengapa?",
        "Jika kamu bisa bertukar hidup dengan seseorang selama satu hari, siapa yang akan kamu pilih?",
        "Ceritakan rahasia terkecil yang kamu simpan dari teman-temanmu."
        ]

    # List untuk dare
    dares = [
        "Lakukan tarian konyol selama 1 menit.",
        "Telepon seseorang dan berikan selamat ulang tahun, meskipun bukan ulang tahun mereka.",
        "Pergi ke luar dan nyanyikan lagu favoritmu sekuat hati selama 1 menit.",
        "Kirim pesan teks kepada temanmu dan berpura-puralah meminjam uang.",
        "Pergi ke luar dan berbicaralah kepada benda atau tumbuhan sekitarmu selama 5 menit, seolah-olah mereka adalah temanmu.",
        "Kirim pesan teks kepada temanmu dan minta mereka untuk memberikan tiga kata yang mendeskripsikanmu secara akurat.",
        'Pergi ke luar dan berteriak, "Saya mencintai sayuran!" setidaknya selama 1 menit.',
        "Ambil benda di sekitarmu dan buatlah lagu pendek tentang benda tersebut, lalu nyanyikan di depan semua pemain.",
        "Kirim pesan suara kepada temanmu dengan ucapan selamat ulang tahun, bahkan jika hari ulang tahun mereka masih jauh.",
        "Ambil foto dirimu dan unggah ke story instagrammu selama satu jam."
        ]

    print(f"""\nHai {player_terpilih}, Silahkan pilih salah satu:
1. Truth
2. Dare""")
    choice = input("Pilih opsi (1/2): ")

    # looping truth or dare
    while(choice!="1" and choice != "2"):
        choice =(input("""Pilihan tidak valid.
Silakan pilih 1 untuk kebenaran atau 2 untuk tantangan.
Pilih opsi (1/2): """))
    if choice == "1":
        print(random.choice(truths))
    elif choice == "2":
        print(random.choice(dares))

    # konfirmasi ulang
    ulang = input('\nMau main lagi (iya/tidak)?:').lower()
    while( ulang != 'iya' and ulang != 'tidak'):
        ulang = input('Maaf inputan anda salah. silahkan coba lagi.\nMau main lagi? :').lower()
   
    if ulang == 'iya' :
        print('\nSilahkan main lagi.')
    elif ulang == 'tidak' :
        print('\nTerima kasih telah bermain. Sampai jumpa!\n')
        break
