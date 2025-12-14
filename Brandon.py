import sys

space = " "

def help():
    print("Welcome to Brandon! A fun bot right in your terminal!")
    print(space)
    print("Here are the commands you can use:")
    print(space)
    print("help - shows this message")
    print(space)
    print("about - shows info about the bot")
    print(space)
    print("exit - exits the bot")
    print(space)
    print("PacerTest - runs the FitnessGram Pacer Test script")

def about():
    print("Brandon v0.2")
    print("Made by byteme")
    print("A fun bot right in your terminal.")

def pacerTest():
    print("The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues.")
    print("The 20 meter pacer test will begin in 30 seconds.")
    print("Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep]")
    print("A single lap should be completed each time you hear this sound. [ding]")
    print("Remember to run in a straight line, and run as long as possible.")
    print("The second time you fail to complete a lap before the sound, your test is over.")
    print("The test will begin on the word start. On your mark, get ready, start.")

def main():
    print("Hi! I'm Brandon, your personal command bot!")
    print("Type 'help' to see what I can do.")
    
    while True:
        cmd = input("Enter a command: ").strip().lower()
        if cmd in commands:
            commands[cmd]()  # ✅ call the function
        else:
            print("Unknown command! Type 'help' to see available commands.")

# Command registry
commands = {
    "help": help,
    "about": about,
    "exit": lambda: sys.exit("Brandon is shutting down..."),
    "pacertest": pacerTest  # lowercase key for user-friendliness
}

# Start the bot
if __name__ == "__main__":
    main()

