def read_matrix(n, matrix_number):
    print(f"{matrix_number}. matrisin elemanlarını giriniz (satır satır):")
    matrix = []
    for i in range(n):
        while True:
            try:
                row = input(f"Satır {i}: ").strip().split()
                if len(row) != n:
                    raise ValueError(f"Satır {i} için tam olarak {n} değer girmeniz gerekiyor.")
                row = [int(x) for x in row]
                matrix.append(row)
                break
            except ValueError as ve:
                print(f"Hata: {ve}. Lütfen tekrar deneyiniz.")
    return matrix

def compute_indegree(matrix, n):
    indegree = [0] * n
    for j in range(n):
        for i in range(n):
            if matrix[i][j] != 0:
                indegree[j] += 1
    return indegree

def find_top_two(indegree):
    first = second = -1
    for i, val in enumerate(indegree):
        if first == -1 or val > indegree[first]:
            second = first
            first = i
        elif second == -1 or val > indegree[second]:
            second = i
    return first, second

def main():
    try:
        n = int(input("Matris boyutunu (n) giriniz: "))
        if n <= 0:
            raise ValueError("Matris boyutu pozitif bir tam sayı olmalıdır.")
    except ValueError as ve:
        print(f"Hata: {ve}")
        return

    # İki matrisin girişini al
    matrix1 = read_matrix(n, 1)
    matrix2 = read_matrix(n, 2)

    # Indegree centrality hesapla
    indegree1 = compute_indegree(matrix1, n)
    indegree2 = compute_indegree(matrix2, n)

    # En popüler iki aktörü bul
    top1_1, top2_1 = find_top_two(indegree1)
    top1_2, top2_2 = find_top_two(indegree2)

    # Sonuçları yazdır
    print("\nİlk matris için en popüler iki aktör:")
    print(f"1. Aktör {top1_1} with indegree {indegree1[top1_1]}")
    print(f"2. Aktör {top2_1} with indegree {indegree1[top2_1]}")

    print("\nİkinci matris için en popüler iki aktör:")
    print(f"1. Aktör {top1_2} with indegree {indegree2[top1_2]}")
    print(f"2. Aktör {top2_2} with indegree {indegree2[top2_2]}")

    # En popüler aktörleri karşılaştır
    print("\nEn popüler aktör karşılaştırması:")
    if indegree1[top1_1] > indegree2[top1_2]:
        print(f"İlk matrisin en popüler aktörü (Aktör {top1_1}) daha ünlü.")
    elif indegree1[top1_1] < indegree2[top1_2]:
        print(f"İkinci matrisin en popüler aktörü (Aktör {top1_2}) daha ünlü.")
    else:
        print("Her iki matrisin en popüler aktörleri eşit ünlülükte.")

if __name__ == "__main__":
    main()
