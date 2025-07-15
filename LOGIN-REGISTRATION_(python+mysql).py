# LOGIN / REGISTRATION
import re
import mysql.connector as sql
db = sql.connect(host = 'localhost',
                 user = 'root',
                 password = 'Gaurav@07',
                 database = 'project')
cur = db.cursor()

#===LOGIN===
def login():
    print('\nLOGIN\n')

    try:

        email = input('Enter your email - ').lower()
        if not re.match(r'^\w+@\w+\.\w+$', email):
            print('\nInvalid email!\n')
            return

        password = input('Enter your password - ')
        cur.execute('select password from user_info2 where email=%s',(email,))
        found = cur.fetchone()
        if found is None:
            print('\nEmail not found!\n')
        elif found[0] == password:
            print('\nLOGIN SUCCESSFUL!\n')
            cur.execute('select name from user_info2 where email=%s',(email,))
            done = cur.fetchone()
            print(f'Welcome back, {done[0]}!\n')
        else:
            print('\nWrong password!\n')

    except Exception as ex:
        print(f'\nError\nstr{ex}\n')

# ===REGISTRATION===
def register():
    print('\nREGISTER\n')

    try:

        name = input('Name - ').title()

        while True:
            email = input('Email - ').lower()
            # EMAIL VALIDATION
            if re.match(r'^\w+@\w+\.\w+$', email):
                # DUPLICATE CHECK
                cur.execute('select * from user_info2 where email=%s',(email,))
                exist_email = cur.fetchone()
                if exist_email:
                    print('\nThis email already exist!\n')
                    return
                break
            else:
                print('\nInvalid email!\n')

        while True:
            try:
                mobile = input('Mobile - ')
                if int(5999999999) < int(mobile) < int(9999999999):
                    cur.execute('select * from user_info2 where mobile=%s', (mobile,))
                    exist_mobile = cur.fetchone()
                    if exist_mobile:
                        print('\nThis mobile number already exist!\n')
                        return
                    break
                else:
                    print('\nInvalid mobile!\n')

            except Exception as ex:
                print(f'\nError!\n{str(ex)}\n')


        while True:
            password1 = input('Password - ')
            password2 = input('Re-type password - ')
            if password1 == password2:
                break
            else:
                print('\nPassword mismatched!\n')

        while True:
            try:
                cur.execute('create table if not exists user_info2 (ID int primary key auto_increment, NAME varchar(20), EMAIL varchar(30) unique, MOBILE varchar(10), PASSWORD varchar(20))')
                cur.execute('insert into user_info2 (NAME,EMAIL,MOBILE,PASSWORD) values (%s,%s,%s,%s)',(name, email, mobile, password1))
                print('\nREGISTRATION SUCCESSFUL!\n')
                cur.execute('select name from user_info2 where email=%s',(email,))
                done = cur.fetchone()
                print(f'Thank you, {done[0]}!\n')
                break
            except Exception as ex:
                print(f'\nCould not save!\n{str(ex)}\n')

    except Exception as ex:
        print(f'\nError!\n{str(ex)}\n')

# ===MAIN MENU===
print('\nWELCOME TO XYZ PAGE\n')

while True:
    print("\n---MENU---\n1. LOGIN\n2. REGISTER\n3. EXIT\nEnter your choice (in number) - ")

    try:

        choice = int(input())

        if choice == 1:
            login()

        elif choice == 2:
            register()

        elif choice == 3:
            print('\nGoodbye for now!\n')
            break

        else:
            print('\nUnavailable choice! Try again.')

    except:
        print('\nINVALID CHOICE! TRY AGAIN.\n')

db.commit()
cur.close()
db.close()