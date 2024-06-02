"'I recently worked on a fun little Python project, and I'm excited to share it with you. It's a simple program that engages in a friendly conversation with the user.
First, the program greets the user and asks for their name. Once the user provides their name, it responds with a warm welcome. Then, it inquires about the user's age. After the user inputs their age, the program calculates the difference between the user's age and its own (which it claims to be 3 years old). It playfully informs the user how many years older they are compared to itself.
But the program doesn't stop there! It also asks the user about their favorite color. Once the user shares their color preference, the program compliments their choice, adding a personal touch to the interaction.
While this project may seem straightforward, it allowed me to practice fundamental Python concepts such as taking user input, performing arithmetic operations, and formatting strings for output. It was a great opportunity to combine basic programming elements with a touch of conversational charm."'


name = input("Hello! What is your name? ")
print(f"Nice to meet you, {name}!")
age_input = input("How old are you? ")
age = int(age_input)
bot_age = 3
age_difference = age - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")
color = input("What's your favorite color?")
print(f"Oh, {color} is a beautiful color!")
