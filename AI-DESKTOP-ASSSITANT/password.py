import threading


def password():
    def check_password():
        for i in range(3):
            a = input("Enter Password to open Jarvis: ")
            with open("password.txt", "r") as pw_file:
                pw = pw_file.read().strip()
            if a == pw:
                print("WELCOME SIR! PLEASE SPEAK [WAKE UP] TO LOAD ME UP")
                return True
            elif i == 2 and a != pw:
                exit()
            elif a != pw:
                print("Try Again")
        return False

    # Create a new thread to run the password checking function
    password_thread = threading.Thread(target=check_password)
    password_thread.start()