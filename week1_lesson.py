# ══════════════════════════════════════════════════════════════════
# ЧАСТЬ 1. BIG O — ПРИМЕРЫ КОДА
# ══════════════════════════════════════════════════════════════════

# ── O(1) — константная сложность ──────────────────────────────────
# Время НЕ зависит от размера данных.

arr = [10, 20, 30, 40, 50]

print(arr[3])        # O(1) — доступ по индексу
print(arr[0])        # O(1) — не зависит от длины массива
print(arr[-1])       # O(1) — последний элемент
print(len(arr))      # O(1) — длина хранится отдельно

d = {"key": "value"}
print(d["key"])      # O(1) — доступ к словарю


# ── O(log n) — логарифмическая сложность ──────────────────────────
# На каждом шаге отбрасываем ПОЛОВИНУ данных.
# Из 1 000 000 элементов → всего ~20 шагов!

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1       # Отбрасываем левую половину
        else:
            right = mid - 1      # Отбрасываем правую половину
    return -1

sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(sorted_arr, 7))   # 3 (индекс)
print(binary_search(sorted_arr, 10))  # -1 (не найден)


# ── O(n) — линейная сложность ─────────────────────────────────────
# Один проход по всем элементам.
# В 2 раза больше данных → в 2 раза дольше.

def find_max(arr):
    max_val = arr[0]
    for x in arr:           # Один проход — O(n)
        if x > max_val:
            max_val = x
    return max_val

print(find_max([3, 7, 1, 9, 4]))  # 9

# Два последовательных цикла — всё равно O(n)!
# O(n) + O(n) = O(2n) = O(n)  ← константы отбрасываем
def sum_and_max(arr):
    total = 0
    for x in arr:          # O(n)
        total += x
    max_val = arr[0]
    for x in arr:          # O(n)
        if x > max_val:
            max_val = x
    return total, max_val


# ── O(n log n) — эффективные сортировки ───────────────────────────

arr = [5, 2, 8, 1, 9, 3]
arr.sort()                  # O(n log n) — Timsort в Python
print(arr)                  # [1, 2, 3, 5, 8, 9]

# sorted() возвращает НОВЫЙ список, оригинал не трогает
original = [5, 2, 8, 1]
new_arr = sorted(original)  # O(n log n)
print(original)             # [5, 2, 8, 1] — не изменился!
print(new_arr)              # [1, 2, 5, 8]


# ── O(n²) — квадратичная сложность ────────────────────────────────
# Вложенный цикл = умножаем: O(n) × O(n) = O(n²)

def has_duplicate_brute(arr):
    """Проверяем КАЖДУЮ пару — O(n²)"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

print(has_duplicate_brute([1, 2, 3, 4]))  # False
print(has_duplicate_brute([1, 2, 3, 1]))  # True


# ── O(2ⁿ) — экспоненциальная сложность ───────────────────────────
# Рекурсия, которая ветвится.

def fib_naive(n):
    """Наивный Фибоначчи — O(2ⁿ). НЕ делайте так!"""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# fib_naive(10)  → 55 (быстро)
# fib_naive(30)  → 832040 (заметная задержка)
# fib_naive(40)  → уже тормозит
# fib_naive(50)  → можете не дождаться


# ══════════════════════════════════════════════════════════════════
# ЧАСТЬ 2. ПРАВИЛА УПРОЩЕНИЯ BIG O
# ══════════════════════════════════════════════════════════════════

# Правило 1: Отбрасываем константы
# O(2n) = O(n)
# O(100n) = O(n)
# O(n/2) = O(n)

# Правило 2: Берём самый быстрорастущий член
# O(n² + n) = O(n²)
# O(n + log n) = O(n)
# O(n³ + n² + n) = O(n³)

# Правило 3: Последовательные → складываем, вложенные → умножаем
# Два цикла подряд:  O(n) + O(n) = O(n)
# Цикл в цикле:     O(n) × O(n) = O(n²)


# ── Задачка: определите сложность ─────────────────────────────────

def mystery(arr):
    n = len(arr)
    total = 0                 # O(1)
    for i in range(n):        # O(n)
        total += arr[i]

    arr.sort()                # O(n log n)

    for i in range(n):        # O(n)
        for j in range(n):    #   × O(n)  →  O(n²)
            if arr[i] + arr[j] == 0:
                return True
    return False

# Итого: O(1) + O(n) + O(n log n) + O(n²)
# Берём максимальный → O(n²)


# ══════════════════════════════════════════════════════════════════
# ЧАСТЬ 3. LIVE CODING — от O(n²) к O(n)
# ══════════════════════════════════════════════════════════════════

# ── Contains Duplicate (LeetCode #217) ────────────────────────────
# Есть ли в массиве дубликаты?

# Способ 1: Brute Force — O(n²)
def containsDuplicate_v1(nums):
    """Проверяем каждую пару."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Способ 2: Через set — O(n)  
def containsDuplicate_v2(nums):
    """Множество для отслеживания встреченных."""
    seen = set()
    for num in nums:
        if num in seen:          # O(1) — проверка в set
            return True
        seen.add(num)            # O(1) — добавление в set
    return False

# Способ 3: Самый короткий — O(n)
def containsDuplicate_v3(nums):
    return len(nums) != len(set(nums))

# Тесты:
print("--- Contains Duplicate ---")
print(containsDuplicate_v1([1, 2, 3, 1]))  # True
print(containsDuplicate_v2([1, 2, 3, 4]))  # False
print(containsDuplicate_v3([1, 1, 1, 1]))  # True


# ── Two Sum (LeetCode #1) ────────────────────────────────────────
# Найти два числа с заданной суммой. Вернуть их индексы.

# Наивно: O(n²)
def twoSum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Оптимально: O(n) через словарь
def twoSum(nums, target):
    seen = {}                        # число → индекс
    for i, num in enumerate(nums):
        complement = target - num    # Что ищем?
        if complement in seen:       # O(1) — есть в словаре?
            return [seen[complement], i]
        seen[num] = i                # Запоминаем
    return []

print("\n--- Two Sum ---")
print(twoSum([2, 7, 11, 15], 9))   # [0, 1]  (2 + 7 = 9)
print(twoSum([3, 2, 4], 6))         # [1, 2]  (2 + 4 = 6)
print(twoSum([3, 3], 6))            # [0, 1]  (3 + 3 = 6)


# ══════════════════════════════════════════════════════════════════
# ЧАСТЬ 4. GIT КОМАНДЫ — СПРАВОЧНИК
# ══════════════════════════════════════════════════════════════════

"""
═══ УСТАНОВКА И НАСТРОЙКА ═══

git --version                                  # Проверить установку
git config --global user.name "Ваше Имя"       # Имя для коммитов
git config --global user.email "your@email.com" # Email (как на GitHub!)
git config --list                              # Проверить настройки

═══ СОЗДАНИЕ РЕПОЗИТОРИЯ ═══

# Способ 1: С нуля (git init)
mkdir practicum-algorithms
cd practicum-algorithms
git init
mkdir lab1 lab2 lab3 lab4 lab5 lab6 lab7 lab8
echo "# Practicum Algorithms" > README.md

# Способ 2: Клонирование (git clone)
git clone https://github.com/username/repo.git

═══ ЕЖЕДНЕВНЫЙ ЦИКЛ РАБОТЫ ═══

git status                                # 1. Что изменилось?
git add .                                 # 2. Добавить всё в staging
git commit -m "lab1: solve Two Sum (#1)"  # 3. Зафиксировать
git push                                  # 4. Отправить на GitHub

═══ ПОДКЛЮЧЕНИЕ К GITHUB ═══

git remote add origin https://github.com/USERNAME/practicum-algorithms.git
git branch -M main
git push -u origin main

═══ ПОЛЕЗНЫЕ КОМАНДЫ ═══

git log --oneline              # История коммитов (коротко)
git diff                       # Что изменилось (до add)
git diff --staged              # Что в staging (после add)
git checkout -- файл           # Откатить файл
git reset --soft HEAD~1        # Отменить последний коммит
git remote -v                  # Куда пушим?

═══ .gitignore (создать в корне проекта) ═══

__pycache__/
*.pyc
.env
.DS_Store
.idea/
.vscode/
node_modules/
"""


# ══════════════════════════════════════════════════════════════════
#
#     КЛАССНАЯ РАБОТА — ВАРИАНТ A (группы 1/2)
#
# ══════════════════════════════════════════════════════════════════

# ── Задача A1. Определите сложность (устно) ──────────────────────

# Фрагмент 1: какая сложность?
def fragment_a1(n):
    for i in range(n):
        for j in range(10):       # ← 10 — это КОНСТАНТА!
            print(i * j, end=" ")

# Ответ: O(n)
# Внутренний цикл всегда 10 раз — не зависит от n
# O(n × 10) = O(n).


# Фрагмент 2: какая сложность?
def fragment_a2(n, arr):
    for i in range(n):            # O(n)
        print(i)

    for i in range(n):            # O(n)
        for j in range(n):        # × O(n) → O(n²)
            print(i + j, end=" ")

# Ответ: O(n²)
# Два шага: O(n) + O(n²). Берём максимальный → O(n²)


# ── Задача A2. Напишите функцию ──────────────────────────────────
# Вернуть True если ВСЕ элементы массива уникальны.
# Сложность должна быть O(n).

# Примеры:
# all_unique([1, 2, 3, 4])  → True
# all_unique([1, 2, 2, 4])  → False
# all_unique([])             → True

def all_unique(arr):
    pass  # Ваш код здесь


# ─── Эталонные решения ───

def all_unique_solution_1(arr):
    """Через set — самый короткий"""
    return len(arr) == len(set(arr))

def all_unique_solution_2(arr):
    """Через цикл — более наглядный"""
    seen = set()
    for x in arr:
        if x in seen:
            return False
        seen.add(x)
    return True

# ── Задача A3. Git (практическая) ────────────────────────────────
# Создайте lab1/hello.py → git add → commit → push
# Покажите файл на GitHub.


# ══════════════════════════════════════════════════════════════════
#
#     КЛАССНАЯ РАБОТА — ВАРИАНТ B (группы 3/4)
#
# ══════════════════════════════════════════════════════════════════

# ── Задача B1. Определите сложность (устно) ──────────────────────

# Фрагмент 1: какая сложность?
def fragment_b1(n):
    i = n
    while i > 0:
        print(i)
        i = i // 2             

# Ответ: O(log n)
# n → n/2 → n/4 → ... → 1
# Количество шагов = log₂(n)


# Фрагмент 2: какая сложность?
def fragment_b2(arr):
    arr.sort()                  # ← O(n log n)
    for i in range(len(arr)):   # + O(n)
        print(arr[i])

# Ответ: O(n log n)
# sort() = O(n log n), цикл = O(n)
# Берём максимальный → O(n log n)


# ── Задача B2. Напишите функцию ──────────────────────────────────
# Вернуть массив ОБЩИХ элементов двух массивов (пересечение).
# Без дубликатов в результате. Сложность O(n + m).

# Примеры:
# intersection([1, 2, 2, 3], [2, 3, 4])  → [2, 3]
# intersection([1, 2], [3, 4])            → []
# intersection([], [1, 2])                → []

def intersection(arr1, arr2):
    pass  # Ваш код здесь


# ─── Эталонные решения ───

def intersection_solution_1(arr1, arr2):
    """Через set — короткий"""
    return list(set(arr1) & set(arr2))

def intersection_solution_2(arr1, arr2):
    """Через цикл — более наглядный"""
    set1 = set(arr1)          # O(n)
    result = []
    for x in set(arr2):       # O(m)
        if x in set1:         # O(1) — проверка в set!
            result.append(x)
    return result

# ── Задача B3. Git (практическая) ────────────────────────────────
# 1) Создайте lab1/hello.py → add → commit → push
# 2) Измените файл → add → commit (второй!) → push
# 3) Покажите git log с ДВУМЯ коммитами