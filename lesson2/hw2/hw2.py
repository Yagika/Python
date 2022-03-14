# 1) написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все
# 2) протипизировать первое задание
def notebook() -> list:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        return todo_list.append(todo)

    def get_all() -> list:
        return todo_list

    return [add_todo, get_all]


add_todo, get_all = notebook()
add_todo('Eat')
add_todo('Surf the Net')
add_todo('Do homework')
add_todo('Play game')
add_todo('Sleep')
print(get_all())


# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
#
# Пример:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
def expanded_form(n: int) -> str:
    l: str = str(n)
    listr: list[str] = []
    for i in range(len(l)):
        if l[i] == '0':
            pass
        else:
            list.append(l[i] + '0' * (len(l) - 1 - i))
    return '+'.join(listr)


print(expanded_form(7003048))
