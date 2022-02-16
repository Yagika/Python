# створити пустый список users_list = []
#
# стврорити меню в якому потрібно реалізувати:
#
# 1) додававання нового юзера
# 2) вивід всіх юзерів
# 3) вивід всіх юзерів за віком
# 4) видалення юзера по id
# 5) заміна статуса юзера на протилежний
# 6) вихід з меню
#
# приклад юзера {'id':1,'name':'Max', 'age':35,'status':False},{'id':2,'name':'Bil', 'age':14,'status':True}
# ,{'id':3,'name':'Kira', 'age':18,'status':False}
st = True
users_list = [{'id': 1, 'name': 'Max', 'age': 35, 'status': False}, {'id': 2, 'name': 'Bil', 'age': 14, 'status': True},
              {'id': 3, 'name': 'Kira', 'age': 18, 'status': False}]
while st:
    st = input('1)додававання нового юзера' + '\n' +
               '2)вивід всіх юзерів' + '\n' +
               '3)вивід всіх юзерів за віком' + '\n' +
               '4)видалення юзера по id' + '\n' +
               '5)заміна статуса юзера на протилежний' + '\n' +
               '6) вихід з меню\nСделайте свой выбор: ')
    if st == '1':
        users_list.append(input())
    elif st == '2':
        print('users_list=', users_list)
    elif st == '3':
        print('users_list=', sorted(users_list, key=lambda d: d['age']))
    elif st == '4':
        ui = input('Users_id:')
        for i in range(len(users_list) - 1):
            if users_list[i]['id'] == int(ui):
                users_list.remove(users_list[i])
    elif st == '5':
        ui = input('Users_id:')
        for i in range(len(users_list) - 1):
            if users_list[i]['id'] == int(ui):
                if not users_list[i]['status']:
                    users_list[i]['status'] = True
                else:
                    users_list[i]['status'] = False
    elif st == '6':
        break
    else:
        print('error')
