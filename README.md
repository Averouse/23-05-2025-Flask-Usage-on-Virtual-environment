# 23-05-2025-Flask-Usage-on-Virtual-environment

### 1. **Pengertian Virtual Environment (Lingkungan Virtual)**
Lingkungan virtual di Python adalah sebuah lingkungan terisolasi yang memungkinkan kamu menginstal paket-paket (library) Python secara terpisah dari sistem utama. Dengan lingkungan virtual, setiap proyek bisa memiliki versi dependensi yang berbeda tanpa saling mengganggu.  
Pada proyek ini, lingkungan virtual dikelola menggunakan **pipenv**, yang memudahkan instalasi dan pengelolaan dependensi melalui file Pipfile dan Pipfile.lock.

### 2. **Framework Flask**
**Flask** adalah framework web minimalis untuk Python. Flask memudahkan pembuatan aplikasi web dengan sedikit kode dan sangat cocok untuk proyek kecil hingga menengah.  
Pada proyek ini, Flask digunakan untuk membuat beberapa halaman web (route) yang bisa diakses melalui browser.

### 3. **Penjelasan Kode**
- **Impor Library**  
  Kode mengimpor Flask untuk membuat aplikasi web dan random untuk menghasilkan data acak.

- **Inisialisasi Aplikasi**  
  `app = Flask(__name__)` membuat instance aplikasi Flask.

- **Daftar Fakta**  
  `facts_list` adalah list berisi fakta-fakta menarik yang akan ditampilkan secara acak.

- **Routing / Halaman**
    - `/` : Halaman utama, menampilkan pesan sambutan.
    - `/fact` : Menampilkan fakta acak dari `facts_list`.
    - `/about` : Menjelaskan tentang aplikasi.
    - `/coin` : Menampilkan hasil lempar koin secara acak (Heads/Tails).
    - `/password` : Menghasilkan password acak sepanjang 12 karakter.
    - `/pictures` : Menampilkan gambar acak dari daftar URL gambar.

- **Menjalankan Aplikasi**
  Pada bagian akhir kode:
  ```python
  if __name__ == "__main__":
      app.run(debug=True)
  ```
  Artinya aplikasi akan berjalan dalam mode debug saat file ini dijalankan langsung.

### 4. **Menjalankan Proyek**
Pastikan kamu sudah berada di lingkungan virtual pipenv.  
Untuk menjalankan aplikasi, gunakan perintah berikut di terminal:
```sh
pipenv run python main.py
```
Setelah itu, buka browser dan akses `http://localhost:5000/` untuk melihat aplikasi.

### 5. **Manfaat Penggunaan Virtual Environment**
- Menghindari konflik versi library antar proyek.
- Memudahkan pengelolaan dependensi.
- Proyek lebih mudah dipindahkan atau dibagikan ke orang lain.

---

**Kesimpulan:**  
Proyek ini adalah contoh aplikasi web sederhana menggunakan Flask di lingkungan virtual Python. Aplikasi ini memiliki beberapa fitur interaktif seperti menampilkan fakta acak, lempar koin, generator password, dan gambar acak. Semua dependensi dikelola secara terpisah menggunakan pipenv agar pengembangan lebih terstruktur dan aman.
