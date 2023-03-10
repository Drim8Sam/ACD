#!/usr/bin/env python3

# 5 -> 4 -> 3 -> 2 -> None
# ^              ^
# |              |
# head          last

class Elem:
    def __init__(self, x: int, p):
        self.val = x
        self.next = p

# Объектно-ориентированный стиль

class List:
    def __init__(self):
        self.head = None
        self.last = None

    def prepend(self, x: int):
        self.head = Elem(x, self.head)
        # после добавления в пустой список
        # last должен начать указывать на
        # единственный элемент
        if self.last is None:
            self.last = self.head

    def append(self, x: int):
        if self.head is None:
            self.head = Elem(x, None)
            self.last = self.head
        else:
            self.last.next = Elem(x, None)
            self.last = self.last.next

    def print_list(self):
        p = self.head
        while p is not None:
            print(p.val)
            p = p.next

    def length(self) -> int:
        n = 0
        p = self.head
        while p is not None:
            n = n+1
            p = p.next
        return n

# Из списка orig скопировать чётные элементы в новый список
# Исходный список остаётся без изменений
def only_even(orig: List) -> List:
    evens = List()
    p = orig.head
    while p is not None:
        if p.val % 2 == 0:
            evens.append(p.val)
        p = p.next
    return evens

# Удаляет элементы, которые делятся на 3
# Поменять исходный список!
def delete_mod3(orig: List):
    p = orig.head
    while p is not None and p.val % 3 == 0:
        p = p.next
    orig.head = p
    if p is None:
        orig.last = p
    else:
        q = p.next
        while q is not None:
            if q.val % 3 == 0:
                p.next = q.next
                q = p.next
            else:
                p = p.next
                q = q.next
        orig.last = p


# Сортировка слиянием
def confluence_two_list(left, right):
    # Создаем список, где будут храняться отсортированные элементы
    sorted_lst = []

    # Создаем указатели i и j, они будут отвечать за индекс своего списка
    i = 0
    j = 0

    # Прогоняем оба списка через while, сортируя элементы двух списков и добавляя в наш отсортированный список
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1

    # Проверяем, все ли элементы попали в конечный список(ведь может быть ситуация, когда на вход подается спискок с нечетным кол. элементов)
    if i < len(left):
        sorted_lst += left[i:]
    if j < len(right):
        sorted_lst += right[j:]

    return sorted_lst


def merge_sorted(lst):
    if len(lst) == 1:
        return lst
    # Разбиваем список на две части
    middle = len(lst) // 2

    # возвращаем снова в функцию, тем самым на выходе получаем отсортированные части списка lst
    left = merge_sorted(lst[:middle])
    right = merge_sorted(lst[middle:])

    # две части передаются в другую функцию, где будет происходить слияние, и получеам отсортированный список слиянием
    return confluence_two_list(left, right)


if __name__ == '__main__':
    head = List()
    head.prepend(3)
    head.prepend(4)
    head.prepend(6)
    head.prepend(5)
    head.append(2)
    head.print_list()

    print('Length')
    print(head.length())

    print('Only even')
    evens = only_even(head)
    print('Orig')
    head.print_list()           # 5,6,4,3
    print('Evens')
    evens.print_list()          # 6,4

    head.prepend(30)
    head.prepend(33)
    head.append(9)
    print('Delete mod3')
    head.print_list()
    print('After deletion')
    delete_mod3(head)
    head.print_list()           # 5,4

    print('Сортировка слиянием')
    print(*merge_sorted([1, 4, 7, 3, 9, 6, 2]))
    print(*merge_sorted([6, 4, 45, 3, 8, 1]))
    print(*merge_sorted([5, 2, 8]))

    
