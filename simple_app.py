def greet(name):
 return f"Greetings, {name}! This is your first GitHub project, enjoy!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)