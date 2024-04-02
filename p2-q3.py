# محمدرضا محمدی دوویشانی

#قسمت اول
import time
def calculate_magic_number(start , end):
    diff = end - start
    random = int(time.time()*1000)
    random %= diff
    random += start
    return random
start =int(input('please enter your min range: '))
end =int(input('please enter your max range: '))

print (calculate_magic_number(start , end))





#قسمت دوم  

import random
import time

def exam_numbers():
    correct = 0
    incorrect = 0

    st_time = time.time()

    mylist = ['0000','0001','0010','0011' , '0100', '0101', '0110', '0111', '1000','1001','1010','1011','1100','1101','1110','1111']
    for i in range(50):
        ch = random.choice(mylist)
        print(ch)
        if ch == '0000' :
            n = int(input('enter decimal of this: '))
            if n== 0:
                correct +=1
            else:
                incorrect +=1

        elif ch == '0001' :
            n = int(input('enter decimal of this: '))
            if n== 1:
                correct +=1
            else:
                incorrect +=1

        elif ch == '0010' :
            n = int(input('enter decimal of this: '))
            if n== 2:
                correct +=1
            else:
                incorrect +=1
            
        elif ch == '0011' :
            n = int(input('enter decimal of this: '))
            if n== 3:
                correct +=1
            else:
                incorrect +=1

        elif ch == '0100' :
            n = int(input('enter decimal of this: '))
            if n== 4:
                correct +=1
            else:
                incorrect +=1

        elif ch == '0101' :
            n = int(input('enter decimal of this: '))
            if n== 5:
                correct +=1
            else:
                incorrect +=1

        elif ch == '0110' :
            n = int(input('enter decimal of this: '))
            if n== 6:
                correct +=1
            else:
                incorrect +=1

        elif ch == '0111' :
            n = int(input('enter decimal of this: '))
            if n== 7:
                correct +=1
            else:
                incorrect +=1

        elif ch == '1000' :
            n = int(input('enter decimal of this: '))
            if n== 8:
                correct +=1
            else:
                incorrect +=1

        elif ch == '1001' :
            n = int(input('enter decimal of this: '))
            if n== 9:
                correct +=1
            else:
                incorrect +=1

        elif ch == '1010' :
            n = int(input('enter decimal of this: '))
            if n== 10:
                correct +=1
            else:
                incorrect +=1

        elif ch == '1011' :
            n = int(input('enter decimal of this: '))
            if n== 11:
                correct +=1
            else:
                incorrect +=1

        elif ch == '1100' :
            n = int(input('enter decimal of this: '))
            if n== 12:
                correct +=1
            else:
                incorrect +=1

        elif ch == '1101' :
            n = int(input('enter decimal of this: '))
            if n== 13:
                correct +=1
            else:
                incorrect +=1

        elif ch == '1110' :
            n = int(input('enter decimal of this: '))
            if n== 14:
                correct +=1
            else:
                incorrect +=1
        
        elif ch == '1111' :
            n = int(input('enter decimal of this: '))
            if n== 15:
                correct +=1
            else:
                incorrect +=1
                
        end_time = time.time()
        total_time = end_time - st_time

        if total_time > 20:
            print("Time is up!!!!")
            break

    print(f'the number of corrects is {correct} and the number of incorrects is {incorrect}')




#قسمت سوم

import string

def check_pass(users_list):
    names_list =[]
    for user_name , password in users_list:
        if len(password) >= 8 and any(item.islower() for item in password) and any(item.isupper() for item in password) and any(item.punctuation() for item in password):
            names_list.append(user_name)
    print(names_list)










