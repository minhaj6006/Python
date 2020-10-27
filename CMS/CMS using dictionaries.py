courses = { 'P1': 'Physics',
            'C1': 'Chemistry',
            'M1': 'Mathematics',
            'E1': 'English',
            'U1': 'Urdu',
            'PS1': 'Pak Studies'}

courseIndexMapping = {1: 'P1',
                      2: 'C1',
                      3: 'M1',
                      4: 'E1',
                      5: 'U1',
                      6: 'PS1',}

selectedCourse={}

while(True):
    print('\n************ Main Menu ************')
    print('-----------------------------------')
    print('1. Register Courses. \n2. Drop Courses. \n3. List Registered Courses.\n4. Exit Registration Program.')
    print('-----------------------------------')
    option1 = '1'
    option2 = '2'
    option3 = '3'
    option4 = '4'

    user_input=int(input('Select your option: '))
    print('\n')
    if user_input not in (1,2,3,4):
        print('\nInvalid response, please enter the correct choice')
# optione 4 exit
    elif user_input == 4:
        break
# optione 1 Register Courses
    elif user_input == 1:

        if len(selectedCourse) == 4:
            print('You are allowed to register only in 4 courses')
        count = 0
        print('  Available Courses')
        print('---------------------')
        for i in courses.values():
            count += 1
            print('. '.join([str(count),i]))
        print('---------------------')
        select_course = int(input("* Please select course number to register or 0 to exit: "))
        if select_course == 0:
            break
        elif select_course not in (1,2,3,4,5):
            print('\nInvalid response, please enter the correct choice')
            continue