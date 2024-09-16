def generate_arithmetic_sequence(n, a=2, d=3):
    """
    Fungsi untuk menghasilkan deret bilangan aritmatika.

    :param n: Jumlah elemen dalam deret
    :param a: Nilai awal deret (default 2)
    :param d: Selisih antara elemen-elemen deret (default 3)
    :return: Daftar bilangan dalam deret
    """
    print(f"Menghasilkan deret bilangan aritmatika dengan {n} elemen:")
    sequence = [a + i * d for i in range(n)]
    return sequence

def main():
    try:
        # Meminta input dari pengguna
        n = int(input("Masukkan jumlah elemen deret: "))
        if n <= 0:
            raise ValueError("Jumlah elemen harus lebih dari 0.")

        # Menghasilkan deret
        sequence = generate_arithmetic_sequence(n)

        # Menampilkan hasil
        print("Output:")
        print(', '.join(map(str, sequence)))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
