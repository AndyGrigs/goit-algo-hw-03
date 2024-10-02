def hanoi(n, source, auxiliary, target, rods):
    if n > 0:
        # Переміщуємо n-1 дисків з джерела на допоміжний стрижень
        hanoi(n - 1, source, target, auxiliary, rods)

        # Переміщуємо найбільший диск з джерела на цільовий стрижень
        disk = rods[source].pop()
        rods[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {rods}")

        # Переміщуємо n-1 дисків з допоміжного стрижня на цільовий стрижень
        hanoi(n - 1, auxiliary, source, target, rods)

def main():
    n = int(input("Введіть кількість дисків: "))
    rods = {
        'A': list(range(n, 0, -1)),  # Стрижень A з дисками від найбільшого до найменшого
        'B': [],
        'C': []
    }
    print(f"Початковий стан: {rods}")
    hanoi(n, 'A', 'B', 'C', rods)
    print(f"Кінцевий стан: {rods}")

if __name__ == "__main__":
    main()
