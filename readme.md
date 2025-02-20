# Sudoku Solver dengan Brute Force

Program sederhana untuk menyelesaikan teka-teki Sudoku menggunakan algoritma brute force (backtracking) yang diimplementasikan dengan Python.

## Cara Kerja Program

- **Brute Force Backtracking**: Program akan menempatkan angka 1-9 di setiap kotak kosong dan memeriksa apakah penempatan tersebut valid sesuai aturan Sudoku. Jika menemui konflik, program akan mundur (backtrack) dan mencoba angka lain.
- **Animasi**: Setelah setiap angka ditempatkan, program akan menampilkan papan Sudoku yang diperbarui dengan jeda waktu pendek.

## Fitur

- Pemecahan Sudoku menggunakan algoritma **backtracking**.
- **Animasi real-time** dari proses penyelesaian di terminal.
- Dapat menangani puzzle Sudoku ukuran 9x9.

## Prasyarat

Pastikan Python sudah terinstall di komputer Anda. Anda bisa mengeceknya dengan menjalankan perintah berikut di terminal:

```bash
python --version
```

Jika Python belum terinstal, silakan unduh dan instal dari [situs Python](https://www.python.org/).

## Cara Menggunakan

1. **Clone repositori**:

   ```bash
   git clone https://github.com/katsurameen/sudoforce.git
   ```

2. **Masuk ke direktori proyek**:

   ```bash
   cd sudoforce
   ```

3. **Jalankan program**:
   Jalankan script Python menggunakan perintah berikut di terminal:

   ```bash
   python sudoku_solver.py
   ```

4. **Tonton proses pemecahan Sudoku**:
   Program akan menampilkan teka-teki Sudoku awal, lalu memulai proses penyelesaian dengan animasi.

## Struktur Kode

- **`is_valid`**: Fungsi ini mengecek apakah suatu angka bisa ditempatkan di kotak tertentu berdasarkan aturan Sudoku.
- **`find_empty`**: Mencari kotak kosong berikutnya yang harus diisi.
- **`solve_sudoku`**: Fungsi utama yang menjalankan algoritma brute force dengan backtracking untuk menyelesaikan Sudoku.
- **`print_board`**: Fungsi untuk menampilkan papan Sudoku di terminal dengan format yang rapi.
- **`time.sleep()`**: Menambahkan jeda waktu antara setiap perubahan untuk membuat animasi berjalan.

## Contoh Puzzle

Contoh puzzle yang digunakan dalam kode:

```python
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

Puzzle ini akan dipecahkan dan ditampilkan di terminal.

## Penyesuaian

- Anda bisa mengganti **puzzle Sudoku** dengan mengganti nilai-nilai pada variabel `sudoku_board` di dalam file.
- Untuk mengatur kecepatan animasi, ubah nilai di dalam fungsi `time.sleep()` di dalam kode. Misalnya:
  ```python
  time.sleep(0.05)  # Lebih cepat
  time.sleep(0.2)   # Lebih lambat
  ```

## Kontribusi

Jika Anda ingin berkontribusi untuk memperbaiki kode atau menambah fitur baru, silakan fork proyek ini dan kirimkan pull request!

## Lisensi

- MIT

