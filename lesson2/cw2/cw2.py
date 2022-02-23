# создать декоратор который будет считать сколько раз была запущена функция
# и будет выводит это значение после каждого запуска функции

def decor(func):
    count = 0

    def inner():
        nonlocal count
        count += 1
        print('count:', count, '\n')
        func()
        print('\n' + '-' * 20 + '\n')

    return inner


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()


# сделайте функцию на замыкания которая будет возвращать декоратор который будет считать
# общее количество запущенных  функций декорированных этим декоратором
count = 0


def make_decorator():
    def decor(func):
        def inner():
            global count
            count += 1
            print('count:', count, '\n')
            func()
            print('\n' + '-' * 20 + '\n')

        return inner

    return decor


decor = make_decorator()


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()
