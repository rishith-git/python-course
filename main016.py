#Program to define shut down

def shutdown():
    answer = input("Do you want to shut down? (yes/no): ").strip().lower()
    if answer == "yes":
        print("Shutting down the system")
    else:
        print("Aborting shutdown")

shutdown()