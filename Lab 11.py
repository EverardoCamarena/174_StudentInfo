#Everardo Camarena
#cecs 174, march 4, 2020
student = {}

def main():
    menu = '1. Add new student\n2. Delete an existing student\n3. Update a student information\n4. Show information of all the students\n5.Quit\n'
    print(menu)
    select = int(input('Please select an action from the menu: '))
    menu_select(select,menu)
    print('Good-bye')
    return

def menu_select(item,menu):
    while item != 5:
        if item == 1:
            add_new()
        elif item == 2:
            delete()
        elif item == 3:
            update()
        elif item == 4:
            print('Here are all thestudents\' information:\n',student)
        else:
            print('Please select a valid item.')
        print(menu)
        item = int(input('Please select an action from the menu: '))
    return
        
def add_new():
    name = input('Enter the new student\'s name: ')
    scores = []
    for i in range(1,4):
        test = int(input('Enter test score: '))
        scores.append(test)
    student[name] = scores
    print('You have successfully added {}'.format(name))
    print('\n')
    return

def delete():
    name = input('Enter student name: ')
    del student[name]
    print('You successfully deleted {}'.format(name))
    print('\n')
    return

def update():
    name = input('Enter the name you want to update: ')
    scores = student[name]
    index = int(input('Enter whitch test score you want to change: '))
    new_score = int(input('Enter the new score: '))
    scores[index-1] = new_score
    print('{} scores are now {}'.format(name,scores))
    return
main()
