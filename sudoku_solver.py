import time
import os

def is_valid(board, row, col, num):
    """Fungsi untuk mengecek nomor yang disimpan pada cell (baris, kolom) adalah valid."""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty(board):
    """Fungsi mencari cell kosong (di tampilkan dengan angka 0)."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def solve_sudoku(board):
    """Fungsi untuk menyelesaikan puzzle Sudoku menggunakan backtracking (brute-force)."""
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  # Jika cell kosong sudah habis maka puzzle selesai.

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            print_board(board)  # Menampilkan board setiap ada perubahan
            time.sleep(0.01)     # time delay untuk backtracking

            if solve_sudoku(board):
                return True

            board[row][col] = 0
            print_board(board)  # Menampilkan board setelah melakukan backtracking
            time.sleep(0.01)

    return False

def print_board(board):
    """Print the Sudoku board in a formatted way with clear screen animation.
       Fungsi untuk mencetak board Sudoku dalam format 9x9 board dengan animasi layar yang jelas.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # membersihkan terminal
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)

        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")

            if col == 8:
                print(board[row][col])
            else:
                print(f"{board[row][col]} ", end="")

if __name__ == "__main__":
    # Contoh persoalan:
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

    print("Unsolved Sudoku:")
    print_board(sudoku_board)
    time.sleep(2)  # Pause before solving
    
    # program ini mencoba untuk menyelesaikan puzzle menggunakan fungsi solve_sudoku(). jika sukses maka akan mencetak board yang terselesaikan
    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku:")
        print_board(sudoku_board)
    else:
    # jika tidak maka akan mencetak hal berikut karena soal sudoku yang random.
        print("No solution exists!")