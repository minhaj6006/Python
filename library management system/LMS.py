import smtplib
content = "bla bla bla"
print('*************************************')
print('*     Library Management System     *')
print('*************************************')
# user_name = input('Register your self by your name: ')
# data=[]
mail = smtplib.SMTP("smtp.gmail.com",465)
mail.login("librarykarachi@gmail.com","0000Qwerty")
mail.sendmail("librarykarachi@gmail.com","minhaj6006@gmail.com", content)
mail.close()