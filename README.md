# 🌸 Kalkulator Transformasi Kekinian (Sakura UI)

![Sakura Anime UI](https://img.shields.io/badge/UI-Sakura_Anime-pink?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask&logoColor=white)

Selamat datang di repositori **Kalkulator Transformasi Kekinian**! Proyek ini adalah aplikasi web kalkulator serbaguna yang dibangun menggunakan **Flask (Python)** dengan antarmuka modern bertema **Sakura Anime (Glassmorphism & Bento Grid)**. 

Aplikasi ini tidak hanya dapat melakukan perhitungan matematika dasar, tetapi juga konversi berbagai sistem bilangan dan operasi logika.

## ✨ Fitur Utama

- 🔢 **Aritmatika Dasar**: Penjumlahan, Pengurangan, Perkalian, Pembagian, Modulo, dll.
- 🔄 **Konversi Sistem Bilangan**: Desimal ke Biner, Oktal, Hexadesimal (dan sebaliknya).
- 🧠 **Operasi Logika (Gerbang Logika)**: AND, OR, NOT, XOR, NAND, dll.
- 🎁 **Fitur Tambahan (Bonus)**: Fitur kalkulasi tambahan (misalnya perhitungan khusus atau bangun ruang).
- 🎨 **UI/UX Modern**: Desain antarmuka bertema Sakura yang estetik, menggunakan efek *Glassmorphism* yang memanjakan mata dan navigasi bergaya *Bento Grid*.

## 🛠️ Teknologi yang Digunakan

- **Backend**: Python 3, Flask (Modular dengan Blueprints)
- **Frontend**: HTML5, Vanilla CSS (Glassmorphism, Flexbox/Grid), JavaScript
- **Lainnya**: Virtual Environment (`venv`), Git

## 📂 Struktur Direktori

Aplikasi ini menggunakan struktur modular untuk kemudahan *maintenance*:

```text
├── routes/                 # Blueprint Flask untuk setiap fitur
│   ├── aritmatika.py       # Logika perhitungan aritmatika
│   ├── konversi.py         # Logika konversi bilangan
│   ├── logika.py           # Logika gerbang logika
│   ├── bonus.py            # Fitur tambahan
│   └── main.py             # Route utama (Home)
├── static/                 # File statis (CSS, JS, Gambar, Font)
├── templates/              # File HTML untuk antarmuka
├── app.py                  # Entry point / File utama aplikasi Flask
├── requirements.txt        # Daftar dependensi library Python
└── README.md               # Dokumentasi proyek (File ini)
```

## 🚀 Cara Instalasi & Menjalankan (Local)

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di komputer lokal Anda:

1. **Clone Repositori ini:**
   ```bash
   git clone https://github.com/USERNAME_ANDA/NAMA_REPOSITORI.git
   cd "Tugas Kalkulator Kekinian"
   ```
   *(Jangan lupa ubah link di atas dengan link repositori GitHub Anda!)*

2. **Buat dan Aktifkan Virtual Environment:**
   - **Windows:**
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi:**
   ```bash
   python app.py
   ```

5. **Buka di Browser:**
   Buka browser Anda dan akses: `http://127.0.0.1:5000`

## 🤝 Cara Berkontribusi (Contributing)

Jika Anda ingin berkontribusi untuk mengembangkan aplikasi ini:
1. Lakukan **Fork** pada repositori ini.
2. Buat *branch* fitur Anda (`git checkout -b fitur-keren-saya`).
3. Lakukan *Commit* perubahan Anda (`git commit -m 'Menambahkan fitur keren'`).
4. Lakukan *Push* ke *branch* (`git push origin fitur-keren-saya`).
5. Buat **Pull Request**.

## 📝 Lisensi

[MIT License](https://opensource.org/licenses/MIT) - Bebas digunakan dan dimodifikasi untuk tujuan pembelajaran atau komersial.
