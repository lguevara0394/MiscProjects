def chatbot():
    print("Hello, What is your name?")
    name = input()
    print(f"Nice to meet you, {name}!")
    print("How old are you?")
    age = input()
    bot_age = 3
    age_difference = age - bot_age
    print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")
    print("What is your favorite color?")
    color = input()
    print(f"Oh, {color} is a beautiful color!")
