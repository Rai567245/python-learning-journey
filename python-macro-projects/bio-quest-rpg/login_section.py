class LoginSection:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.banner = "=" * 30
        self.max_attempts = 3

    def login(self):
        attempts = 0

        while attempts < self.max_attempts:
            print(self.banner)
            print("| 🔒 Bio-Quest Login Section |")
            print(self.banner)

            input_username = input("Username: ")
            input_password = input("Password: ")

            if input_username == self.username and input_password == self.password:
                print("\nLogin Successful! 🎉\n")
                return True

            attempts += 1
            print(f"\nInvalid login! Attempts left: {self.max_attempts - attempts}\n")

        print("Too many failed attempts. Access denied.")
        return False
