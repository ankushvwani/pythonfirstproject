bot_name: str = 'calci'
print(f"Hello, I\'m {bot_name}! How can I assist you today?")

while True:
    user_input: str = input("You: ").lower()

    if user_input in [ 'hi', 'hello'  ]:
        print(f"{bot_name}:  Hi there! How can I help you?")
    elif user_input in [ 'see you ', 'bye' ]:
        print(f"{bot_name}:  Goodbye! Have a nice day!")
    elif user_input in [ '+', 'add' ]:
        print(f"{bot_name}:  Sure! Let\'s do some addition! Please enter numbers.")
        try:
            num1:float = float(input("First number: "))
            num2:float = float(input("Second number: "))
            print(f"{bot_name}:  The sum is {num1 + num2}.")
        except ValueError:
            print(f"{bot_name}:  Oops! That doesn't look like a number. Try again.")
    elif user_input in [ '-', 'subtract' ]:
        print(f"{bot_name}:  Sure! Let\'s do some subtraction! Please enter numbers.")
        try:
            num1:float = float(input("First number: "))
            num2:float = float(input("Second number: "))
            print(f"{bot_name}:  The sum is {num1 - num2}.")
        except ValueError:
            print(f"{bot_name}:  Oops! That doesn't look like a number. Try again.")
    elif user_input in [ 'exit' ]:
        break;
    else:
        print(f"{bot_name}:  I\'m sorry! I don\'t understand that. Please try again. ")
