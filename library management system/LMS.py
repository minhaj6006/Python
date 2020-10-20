
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
                   "TLR": "The Lord of the Rings",
                   "TH1": "The Hobbit",
                   ""
}
print('*************************************')
print('*     Library Management System     *')
print('*************************************')
ask_name = input('Register your self by name: ')
ask_email = input('enter your emai: ')
name_data=[ask_name] #store user name
emai_data=[ask_email] #store user email
p_books=[]


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
    choose_option = input ('Select your option: ')