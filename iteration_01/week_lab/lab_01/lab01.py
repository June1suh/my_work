""" - Create a program that asks the user for their...
        - name
        - age
        - if they are multilingual

    - Program should accomplish the set of criteria listed below
        1. Print a statement that greets the user by name and welcomes them to the program
        2. User data is stored inside of a dictionary
        3. If the user is under 13 state that the user cannot sit in the passenger seat of a car
            - if the user is under 18 then state that the user cannot vote
            - If the user is under 25 state that the user cannot rent a car
            - If the user is over 35 state that they are getting old...
        4. If the user is multilingual, ask the user how many languages they speak.
            - Use a loop to ask the user for each of the 'n' language that they speak and each language entered.
            - If the user is not multilingual, ask the user to enter a language that they wish to learn. Print this back to user.
        5. Ask if another user would like to enter their information as well. All dictionaries with user data should be appended
           to a list with info of all users. Only end program when user specifies that they are done.
        5. Program is considered complete if...
            - Program prints greeting with user name
            - Program prints out all statements appropriate for user age
            - Program prints languages spoken or language user wishes to learn for user
            - Program prints list of all user dictionaries when done"""

def user_info():
    users = []
    while True:
        user = {}
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        multilingual = input("Are you multilingual? (yes/no): ").strip().lower()

        user['name'] = name
        user['age'] = age
        user['multilingual'] = multilingual

        print(f"Hello {name}, welcome to the program!")

        if age < 13:
            print("You cannot sit in the passenger seat of a car.")
        if age < 18:
            print("You cannot vote.")
        if age < 25:
            print("You cannot rent a car.")
        if age > 35:
            print("You are getting old...")

        if multilingual == 'yes':
            num_languages = int(input("How many languages do you speak? "))
            languages = []
            for i in range(num_languages):
                language = input(f"Enter language {i+1}: ")
                languages.append(language)
            user['languages'] = languages
            print(f"You speak the following languages: {', '.join(languages)}")
        else:
            language_to_learn = input("Enter a language you wish to learn: ")
            user['language_to_learn'] = language_to_learn
            print(f"You wish to learn: {language_to_learn}")

        users.append(user)

        another_user = input("Would another user like to enter their information? (yes/no): ").strip().lower()
        if another_user != 'yes':
            break

    print("All user information:")
    for u in users:
        print(u)

user_info()