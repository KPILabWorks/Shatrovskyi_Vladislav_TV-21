def next_bigger_number(n):
    digits = list(str(n))
    i = len(digits) - 2

    # Знайти перший елемент (з кінця), який менший за наступний
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1  # якщо немає більшого числа з тими ж цифрами

    # Знайти найменший елемент праворуч від i, більший за digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Поміняти їх місцями
    digits[i], digits[j] = digits[j], digits[i]

    # Відсортувати все після i в порядку зростання
    digits = digits[:i + 1] + sorted(digits[i + 1:])

    return int(''.join(digits))

# Тестуємо
print(next_bigger_number(1234))  # 1243
print(next_bigger_number(4321))  # -1
print(next_bigger_number(534976))  # 536479
