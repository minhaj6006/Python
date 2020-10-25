from pathlib import Path
import time
import smtplib

available_books = ["Harry Potter", 'The Twilight Saga',"The Lord of the Rings","The Hobbit","The Top Ten","The Great Gatsby", "Long Walk to Freedom", "Long Walk to Freedom",]
a_books = [line.rstrip('\n') for line in (available_books)]

print('*************************************')
print('*     Library Management System     *')
print('*************************************')
ask_name = input('\nRegister your self by name: ')
ask_email = input('enter your email: ')
name_data = [ask_name] # store user naem
email_data = [ask_email] # store user email
fromaddr = 'librarykarachi@gmail.com'
toaddrs  = ('{0}'.format(email_data[0]))
msg = 'Please return the book as soon as posibale'
username = 'librarykarachi@gmail.com'
password = '0000Qwerty'
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(username , password)
store_time = []
select_books = []

if Path('{0}.txt'.format(name_data[0])).is_file(): # checking file exist
    file = open('{0}.txt'.format(name_data[0]),"r")
    i = 1
    f = open(name_data[0] + ".txt" ) # this point text file convert into list
    print('\n--------------------')
    print('Welcome Back ' + ask_name)
    print('--------------------\n')
    for line in f.readlines():
        if i % 2 == 0:
            store_time.append(line.rstrip('\n'))
        else:
            select_books.append(line)
        i += 1

else:
    file = open('{0}.txt'.format(name_data[0]),"w")
    print('\n---------------')
    print('Welcome  ' + ask_name)
    print('---------------\n')

b=True
while (b):

    for i in store_time:
        if float(i) + 60 > time.time():
            print("Still have time to return")
            timeexceed = False
        else:
            print("time exceeded")
            timeexceed = True
            server.sendmail(fromaddr, toaddrs, msg)

    print('************ Main Menu ************')
    print('-----------------------------------')
    print('1. Checkout Book. \n2. Return Book. \n3. Show Rented Books. \n4. Exit Program.')
    print('-----------------------------------')
    option1 = '1'
    option2 = '2'
    option3 = '3'
    option4 = '4'
    choose_option = input('Select your option: ')

# option 1 Checkout Book
    if choose_option == option1:
        if(len(select_books) == 3):
            print('\n----------------------------')
            print('Only 3 books allowed to pick')
            print('----------------------------')
            break
        else:
            file = open('{0}.txt'.format(name_data[0]),"a")
            count = 0
            print('\n    Available Books ')
            print('-----------------------')
            for i in a_books: # this loop using for add numbering
                count += 1
                print(' '.join([str(count),i]) )
            print('-----------------------\n')

            b_select = int(input('Select the book: '))

            if (b_select == 1 and a_books[0] not in select_books):
                file.write(str("%s\n" % a_books[0]))
                select_books.append(a_books[0])
                print('rent' + a_books[0])
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% store_time[0]))
            elif (b_select == 1 and a_books[0] in select_books):
                print('\nYou are already rented this book')
            if (b_select == 2 and a_books[1] not in select_books):
                file.write(str("%s\n" % a_books[1]))
                select_books.append(a_books[1])
                print('rent' + a_books[1])
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% store_time[1]))
            elif (b_select == 2 and a_books[1] in select_books):
                print('\nYou are already rented this book')
            if (b_select == 3 and a_books[2] not in select_books):
                file.write(str("%s\n" % a_books[2]))
                select_books.append(a_books[2])
                print('rent' + a_books[2])
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% store_time[2]))
            elif (b_select == 3 and a_books[2] in select_books):
                print('\nYou are already rented this book')
            if (b_select == 4 and a_books[3] not in select_books):
                file.write(str("%s\n" % a_books[3]))
                select_books.append(a_books[3])
                print('rent' + a_books[3])
                rent = time.time()
                s_rent=[rent]
                store_time.append('{0}'.format(s_rent[3]))
                file.write(str('%s\n'% store_time[3]))
            elif (b_select == 4 and a_books[3] in select_books):
                print('\nYou are already rented this book')
            if (b_select == 5 and a_books[4] not in select_books):
                file.write(str("%s\n" % a_books[4]))
                select_books.append(a_books[4])
                print('rent' + a_books[4])
                rent = time.time()
                s_rent=[rent]
                store_time.append('{0}'.format(s_rent[4]))
                file.write(str('%s\n'% store_time[4]))
            elif (b_select == 5 and a_books[4] in select_books):
                print('\nYou are already rented this book')
            if (b_select == 6 and a_books[5] not in select_books):
                file.write(str("%s\n" % a_books[5]))
                select_books.append(a_books[5])
                print('rent' + a_books[5])
                rent = time.time()
                s_rent=[rent]
                store_time.append('{0}'.format(s_rent[5]))
                file.write(str('%s\n'% store_time[5]))
            elif (b_select == 6 and a_books[5] in select_books):
                print('\nYou are already rented this book')
            if (b_select == 7 and a_books[6] not in select_books):
                file.write(str("%s\n" % a_books[6]))
                select_books.append(a_books[6])
                print('rent' + a_books[6])
                rent = time.time()
                s_rent=[rent]
                store_time.append('{0}'.format(s_rent[6]))
                file.write(str('%s\n'% store_time[6]))
            elif (b_select == 7 and a_books[6] in select_books):
                print('\nYou are already rented this book')
            if (b_select == 8 and a_books[7] not in select_books):
                file.write(str("%s\n" % a_books[7]))
                select_books.append(a_books[7])
                print('rent' + a_books[7])
                rent = time.time()
                s_rent=[rent]
                store_time.append('{0}'.format(s_rent[7]))
                file.write(str('%s\n'% store_time[7]))
            elif (b_select == 8 and a_books[7] in select_books):
                print('\nYou are already rented this book')

# option 2 Return Book
    elif choose_option == option2:
        if not select_books:
            print('---------------------------------------')
            print('Checkout the book before select option 2')
            print('---------------------------------------')
        else:
            file = open('{0}.txt'.format(name_data[0]),"r")
            print('\nYou are registered in these courses:')
            print('------------------------------------')
            j = 0
            for i in select_books: # this loop using for add numbering
                j += 1
                print(' '.join([str(j),i]) )

# option3 Show rent book
    elif choose_option == option3:
        if not select_books:
            print('----------------------------------------')
            print('Checkout the Book before select option 3')
            print('----------------------------------------')
        else:
            s_books = [line.rstrip('\n') for line in (select_books)]
            count = 0
            print('\nYou rented these books.')
            print('-----------------------')
            for i in s_books: # this loop using for add numbering
                #print(' '.join([str(count + 1),i]) )

                print('{}. {:25s} '.format(count+1,i), end="")
                print('{:25s} '.format(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(float(store_time[count])))), end="")
                print('{:20s} '.format(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(float(store_time[count])+ 60)) ))
                count += 1


            print('-----------------------')
            r = (int(input("\npress 1 to return Main Menu and press 0 to exit: ")))
            if r == 1:
                continue
            elif r == 0:
                break

# option 4 exit
    elif choose_option == option4: # this point exit program
        print('\n---------------------------')
        print('Thank you for using our LMS\n')
        file.close()
        server.quit()
        break