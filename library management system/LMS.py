# import smtplib
# content = "bla bla bla"
# user_name = input('Register your self by your name: ')
# mail = smtplib.SMTP("smtp.gmail.com",587)
# mail.login("librarykarachi@gmail.com","0000Qwerty")
# mail.sendmail("librarykarachi@gmail.com","minhaj6006@gmail.com", content)
# mail.close()
############################################################################
available_books = {"HP1" : "Harry Potter",
                   "TTS" : "The Twilight Saga",
                   "TLR" : "The Lord of the Rings",
                   "TH1" : "The Hobbit",
                   "TTT" : "The Top Ten",
                   "TGG" : "The Great Gatsby",
                   "LWF" : "Long Walk to Freedom",
                   "SJ1" : "Steve Jobs"}

book_index_mapping = {1: "HP1",
                      2: "TTS",
                      3: "TLR",
                      4: "TH1",
                      5: "TTT",
                      6: "TGG",
                      7: "LWF",
                      8: "SJ1",}

print('*************************************')
print('*     Library Management System     *')
print('*************************************')
ask_email = input('Register your self by email: ')
emai_data=[ask_email] #store user email
select_books=[]


b=True
while (b):
    print('\n************ Main Menu ************')
    print('-----------------------------------')
    print('1. Select Book. \n2. Drop Book. \n3. .\n4. Exit Program.')
    print('-----------------------------------')
    option1 = '1'
    option2 = '2'
    option3 = '3'
    option4 = '4'
    choose_option = input('Select your option: ')

# option 1 Select Book
    if choose_option == option1:
        if(len(select_books) == 3):
            print('\n----------------------------')
            print('Only 3 books allowed to pick')
            print('----------------------------')
            break
        else:
            count = 0
            for i in available_books: # this loop using for add numbering
                count += 1
                print(f"{count}" + " " + available_books[i])

# option 4 exit
    elif choose_option == option4: # this point exit program
        print('\n---------------------------')
        print('Thank you for using our LMS\n')
        break