started = False

while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started... Ready to go!")

    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped.")

    elif command == "help":
        print("""
start - Start the car
stop  - Stop the car
quit  - Exit the game
""")

    elif command == "quit":
        break

    else:
        print("Invalid command. Type 'help' for available commands.")