import tkinter as tk
import random
import os
from collections import deque

# Daftar makanan di Tembalang dengan informasi tambahan
makanan_tembalang = {
    "Sarapan Pagi": [
        {"nama": "Mi Ayam Bang Mail", "harga": "Rp 12.000", "alamat": "Jl Baskoro no, 75"},
        {"nama": "Bubur Ayam Jakarta", "harga": "Rp 10.000", "alamat": "Depan Pembatas Jalan Gondang"},
        {"nama": "Ketoprak LPPU", "harga": "Rp 10.000", "alamat": "Depan Masjid LPPU"},
        {"nama": "Nasi Uduk/Kuning Depan Hutan Kampus", "harga": "Rp 8.000", "alamat": "Depan Masjid LPPU"},
        {"nama": "Warteg Du Dewi", "harga": "Rp 13.000", "alamat": "Jl. Prof. Soedarto No.12i"},
        {"nama": "Pecel Bu Mar", "harga": "Rp 14.000", "alamat": "Depan Pembatas Jalan Gondang"},
        {"nama": "Food Truck Undip", "harga": "Rp 0", "alamat": "Student Center Undip"},
        {"nama": "Warteg Mama Ros", "harga": "Rp 14.000", "alamat": " Jl. Kedungmundu No.18"},
        {"nama": "Orak Arik Telur Burjo Priangan 1", "harga": "Rp 10.000", "alamat": " Jl. Gondang Tim. II"},
        {"nama": "Bubur Kacang Ijo Burjo SS", "harga": "Rp 8.000", "alamat": "Jl. Gondang Raya"},
        {"nama": "Ketoprak Jakarta", "harga": "Rp 10.000", "alamat": "Jl. Gondang Raya"}

    ],
    "Makan Siang": [
        {"nama": "Ayam Panggang Lombok Cengis", "harga": "Rp 20.000", "alamat": "Jl. Tirto Agung No.17a"},
        {"nama": "Nasi Goreng Motekar 10", "harga": "Rp 15.000", "alamat": " Jl. Gondang Raya No.1"},
        {"nama": "Mie Ayam Afui Palembang", "harga": "Rp 19.000", "alamat": "Jl. Banyu Putih Raya No.14"},
        {"nama": "Mi Ayam Bang Mail", "harga": "Rp 12.000", "alamat": "Jl baskoro no, 75"},
        {"nama": "Nasi Campur Kedai Toba(NON HALAL)", "harga": "Rp 25.000", "alamat": "Gg. Maerasari 2 No.2"},
        {"nama": "Mie Ayam Afui Palembang", "harga": "Rp 15.000", "alamat": "Jl. Banyu Putih Raya No.14"},
        {"nama": "OTI Fried Chicken", "harga": "Rp 22.000", "alamat": "Jl. Timoho Raya No.18"},
        {"nama": "Lapo Sinar Medan(NON HALAL)", "harga": "Rp 25.000", "alamat": "Jl. Imam Soeparto No.20 "},
        {"nama": "Nasi Balap Burjo SS", "harga": "Rp 14.000", "alamat": "Jl. Gondang Raya"},
        {"nama": "Ayam goreng Abah Gatot", "harga": "Rp 22.000", "alamat": "Jl. Ngesrep Tim. V No.124"},
        {"nama": "Ayam Geprek Petir", "harga": "Rp 15.000", "alamat": "Jl. Timoho Bar. III"},
        {"nama": "Orak arik Telur Priangan 1", "harga": "Rp 10.000", "alamat": "Jl. Gondang Tim. II"},
        {"nama": "Nasi Ayam Bali Crispy Priangan 1", "harga": "Rp 13.000", "alamat": "Jl. Gondang Tim. II"},
        {"nama": "Mie Gacoan Setiabudi Semarang", "harga": "Rp 25.000", "alamat": "Tinjomoyo, Banyumanik"},
        {"nama": "Warung Penyet Sami Seneng", "harga": "Rp 18.000", "alamat": "Belakang Maskam"},
        {"nama": "Warung Makan & Penyetan Pak Eko", "harga": "Rp 14.000", "alamat": "Jl. Ngesrep Tim. III Dalam No.24"},
        {"nama": "Warteg MJ", "harga": "Rp 18.000", "alamat": " Jl. Lkr. Utara Undip,"},
        {"nama": "WARPAD", "harga": "Rp 15.000", "alamat": "Jl. Gondang Barat I No.7"},
        {"nama": "Padang MM", "harga": "Rp 20.000", "alamat": " Jl. Tirto Agung,"},
        {"nama": "Ayama Saus Leleh", "harga": "Rp 13.000", "alamat": "Jl. Bulusan Selatan Raya"}

    ],
    "Malam": [
        {"nama": "Gurame Bakar", "harga": "Rp 30.000", "alamat": "Jl. Gurame No. 11"},
        {"nama": "Ikan Bakar Sulawesi", "harga": "Rp 25.000", "alamat": "Jl. Ngesrep Tim. V No.31"},
        {"nama": "Sate Bang Amir", "harga": "Rp 20.000", "alamat": "Jl. Banjarsari No.48"},
        {"nama": "Nasi Goreng Sadewa", "harga": "Rp 15.000", "alamat": "Jl. Prof. Soedarto"},
        {"nama": "Burjo PK Biru", "harga": "Rp 15.000", "alamat": "Jl. Gondang Barat II No.6"},
        {"nama": "Ayam Panggang Lombok Cengis", "harga": "Rp 20.000", "alamat": "Jl. Tirto Agung No.17a"},
        {"nama": "Nasi Goreng Motekar 10", "harga": "Rp 15.000", "alamat": " Jl. Gondang Raya No.1"},
        {"nama": "Mie Ayam Afui Palembang", "harga": "Rp 19.000", "alamat": "Jl. Banyu Putih Raya No.14"},
        {"nama": "Mi Ayam Bang Mail", "harga": "Rp 12.000", "alamat": "Jl baskoro no, 75"},
        {"nama": "Nasi Campur Kedai Toba(NON HALAL)", "harga": "Rp 25.000", "alamat": "Gg. Maerasari 2 No.2"},
        {"nama": "Mie Ayam Afui Palembang", "harga": "Rp 15.000", "alamat": "Jl. Banyu Putih Raya No.14"},
        {"nama": "OTI Fried Chicken", "harga": "Rp 22.000", "alamat": "Jl. Timoho Raya No.18"},
        {"nama": "Lapo Sinar Medan(NON HALAL)", "harga": "Rp 25.000", "alamat": "Jl. Imam Soeparto No.20 "},
        {"nama": "Nasi Balap Burjo SS", "harga": "Rp 14.000", "alamat": "Jl. Gondang Raya"},
        {"nama": "Ayam goreng Abah Gatot", "harga": "Rp 22.000", "alamat": "Jl. Ngesrep Tim. V No.124"},
        {"nama": "Ayam Geprek Petir", "harga": "Rp 15.000", "alamat": "Jl. Timoho Bar. III"},
        {"nama": "Orak arik Telur Priangan 1", "harga": "Rp 10.000", "alamat": "Jl. Gondang Tim. II"},
        {"nama": "Nasi Ayam Bali Crispy Priangan 1", "harga": "Rp 13.000", "alamat": "Jl. Gondang Tim. II"},
        {"nama": "Mie Gacoan Setiabudi Semarang", "harga": "Rp 25.000", "alamat": "Tinjomoyo, Banyumanik"},
        {"nama": "Warung Penyet Sami Seneng", "harga": "Rp 18.000", "alamat": "Belakang Maskam"},
        {"nama": "Warung Makan & Penyetan Pak Eko", "harga": "Rp 14.000", "alamat": "Jl. Ngesrep Tim. III Dalam No.24"},
        {"nama": "Warteg MJ", "harga": "Rp 18.000", "alamat": " Jl. Lkr. Utara Undip,"},
        {"nama": "WARPAD", "harga": "Rp 15.000", "alamat": "Jl. Gondang Barat I No.7"},
        {"nama": "Padang MM", "harga": "Rp 20.000", "alamat": " Jl. Tirto Agung,"},
        {"nama": "Ayama Saus Leleh", "harga": "Rp 13.000", "alamat": "Jl. Bulusan Selatan Raya"},
        {"nama": "Seblak Dago Bandung", "harga": "Rp 24.000", "alamat": "Jl. Jatimulyo No.10a"},
        {"nama": "Bakso Premier", "harga": "Rp 20.000", "alamat": "Jl. Prof. Soedarto No.16"},
        {"nama": "Debox Ricebox", "harga": "Rp 25.000", "alamat": "Sumurboto"}


    ],
    "Ngemil Malam": [
        {"nama": "Panchong Burketsu", "harga": "Rp 301.000", "alamat": "Deket Unpan"},
        {"nama": "Sate Depan Hutan Kampus", "harga": "Rp 10.000", "alamat": "Jl. LPPU"},
        {"nama": "Panchong Burcok", "harga": "Rp 15.000", "alamat": "Jl. Burcok No. 7"},
        {"nama": "Jajanan taman tirto", "harga": "Rp 10.000", "alamat": "Jl. Taman Tirto"},
        {"nama": "Kebab depan Indomaret Banjarsari", "harga": "Rp 15.000", "alamat": "Depan Indomaret Banjarsari"},
        {"nama": "Roti Bakar Enakk", "harga": "Rp 20.000", "alamat": "Gg. Margoyoso No.29b"},
        {"nama": "Martabak Markos", "harga": "Rp 20.000", "alamat": " depan Rumi, Jl. Gondang Raya No.11,"},
        {"nama": "Martabak Sumo Sumurboto Banyuman", "harga": "Rp 15.000", "alamat": "Jl. Ngesrep Tim. V No.88"},
        {"nama": "Pisang Brondol", "harga": "Rp 15.000", "alamat": "Jl. Galang Sewu Raya Jl. Baskoro Raya No.7"},
        {"nama": "Lekker Story", "harga": "Rp 10.000", "alamat": "Jl. Ngesrep Tim. V No.54"},
        {"nama": "Dcrepes", "harga": "Rp 25.000", "alamat": "Jl. Ngesrep Tim. V No.92"}

    
    ]
}

# Stack untuk riwayat makanan
history_stack = []

# Queue untuk rekomendasi makanan
recommendation_queue = deque()

def randomize_makanan():
    makanan_terpilih = pilih_makanan_random()
    if makanan_terpilih:
        nama = makanan_terpilih["nama"]
        harga = makanan_terpilih["harga"]
        alamat = makanan_terpilih["alamat"]
        label_hasil.config(text=f"Enak nih {combo_waktu.get()}:\n{nama}\nHarga: {harga}\nAlamat: {alamat}", fg="blue")

        # Tambahkan ke stack history
        history_stack.append(makanan_terpilih)

        # Tambahkan ke queue rekomendasi
        recommendation_queue.append(makanan_terpilih)

        # Batasi ukuran queue rekomendasi hingga 5
        if len(recommendation_queue) > 5:
            recommendation_queue.popleft()
    else:
        label_hasil.config(text="Mood makan apa dulu nih?", fg="red")

def pilih_makanan_random():
    waktu_makan = combo_waktu.get()
    if waktu_makan in makanan_tembalang:
        return random.choice(makanan_tembalang[waktu_makan])
    else:
        return None

def tampilkan_semua_makanan():
    semua_makanan = dapatkan_semua_makanan()
    if semua_makanan:
        label_hasil.config(text=f"Semua makanan untuk {combo_waktu.get()}:\n{semua_makanan}", fg="green")
    else:
        label_hasil.config(text="Mood makan apa dulu nih?", fg="red")

def dapatkan_semua_makanan():
    waktu_makan = combo_waktu.get()
    if waktu_makan in makanan_tembalang:
        semua_makanan = "Makanan yang tersedia:\n"
        for makanan in makanan_tembalang[waktu_makan]:
            semua_makanan += f"- {makanan['nama']} (Harga: {makanan['harga']}, Alamat: {makanan['alamat']})\n"
        return semua_makanan
    else:
        return None

def tampilkan_riwayat():
    if history_stack:
        riwayat = "Riwayat makanan yang dipilih:\n"
        for makanan in history_stack:
            riwayat += f"- {makanan['nama']} (Harga: {makanan['harga']}, Alamat: {makanan['alamat']})\n"
        label_hasil.config(text=riwayat, fg="purple")
    else:
        label_hasil.config(text="Belum ada riwayat makanan yang dipilih.", fg="red")

def tampilkan_rekomendasi():
    if recommendation_queue:
        rekomendasi = "Rekomendasi makanan terakhir:\n"
        for makanan in recommendation_queue:
            rekomendasi += f"- {makanan['nama']} (Harga: {makanan['harga']}, Alamat: {makanan['alamat']})\n"
        label_hasil.config(text=rekomendasi, fg="orange")
    else:
        label_hasil.config(text="Belum ada rekomendasi makanan.", fg="red")

# Membuat GUI
root = tk.Tk()
root.title("Randomizer Makanan di Tembalang")
root.geometry("500x700")  # Mengatur ukuran jendela

# Judul Aplikasi
label_judul = tk.Label(root, text="Randomizer Makanan di Tembalang", font=("Helvetica", 16), fg="red")
label_judul.pack(pady=10)

# Dropdown untuk memilih waktu makan
combo_waktu = tk.StringVar()
combo_waktu.set("Lagi Mood Makan hari apa nich?")  # Default value
dropdown_waktu = tk.OptionMenu(root, combo_waktu, "Sarapan Pagi", "Makan Siang", "Malam", "Ngemil Malam")
dropdown_waktu.pack(pady=5)

# Tombol untuk merandom makanan
button_randomize = tk.Button(root, text="Bingung mau makan apa? tekan aku sini!", command=randomize_makanan, bg="yellow")
button_randomize.pack(pady=5)

# Tombol untuk menampilkan semua makanan
button_tampilkan_semua = tk.Button(root, text="Tampilkan semua pilihan", command=tampilkan_semua_makanan, bg="lightgreen")
button_tampilkan_semua.pack(pady=5)

# Tombol untuk menampilkan riwayat makanan
button_riwayat = tk.Button(root, text="Tampilkan riwayat makanan", command=tampilkan_riwayat, bg="lightblue")
button_riwayat.pack(pady=5)

# Tombol untuk menampilkan rekomendasi terakhir
button_rekomendasi = tk.Button(root, text="Tampilkan rekomendasi terakhir", command=tampilkan_rekomendasi, bg="lightcoral")
button_rekomendasi.pack(pady=5)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="", font=("Helvetica", 12))
label_hasil.pack(pady=10)

# Menambahkan keterangan penutup
label_footer = tk.Label(root, text="Selamat menikmati makanan di Tembalang!", font=("Helvetica", 10), fg="grey")
label_footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
