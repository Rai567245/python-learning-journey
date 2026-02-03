# Bio-Quest RPG System
# A simple OOP-based interactive program for learning Python classes

# ---------------- HOME SECTION ----------------
class HomeSection:
    def __init__(self):
        self.banner = "=" * 36

    def display_header(self):
        print(self.banner)
        print("| Welcome to 🧬 Bio-Quest RPG Game |")
        print(self.banner)

    def verification(self):
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != "yes" and choice != "y":
            print("\nThank you! Exiting the game.")
            return False
        print("\nGreat! Let's proceed.\n")
        return True

# ---------------- LOGIN SECTION ----------------
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
            else:
                attempts += 1
                print(f"\nInvalid login! Attempts left: {self.max_attempts - attempts}\n")

        print("Too many failed attempts. Access denied.")
        return False

# ---------------- PLAYER SECTION ----------------
class Player:
    def __init__(self):
        self.banner_CC = "=" * 22
        self.banner_PP = "=" * 21
        self.banner_UP = "=" * 23
        self.name = ""
        self.age = 0
        self.gender = ""

    def has_character(self):
        return self.name != ""

    def create_character(self):
        print(self.banner_CC)
        print("| 🧍 Character Creation |")
        print(self.banner_CC)
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")
        print("\nCharacter created successfully!\n")

    def update_character(self):
        if not self.has_character():
            print("\nNo character to update. Please create one first.\n")
            return

        print(self.banner_UP)
        print("| 🧍 Update Character |")
        print(self.banner_UP)
        self.name = input("Enter new name: ")
        self.age = int(input("Enter new age: "))
        self.gender = input("Enter new gender: ")
        print("\nCharacter updated successfully!\n")

    def delete_character(self):
        if not self.has_character():
            print("\nNo character to delete.\n")
            return

        confirm = input("Are you sure you want to delete your character? (yes/no): ").lower()
        if confirm == "yes" or confirm == "y":
            self.name = ""
            self.age = 0
            self.gender = ""
            print("\nCharacter deleted successfully!\n")
        else:
            print("\nCharacter deletion cancelled.\n")
    
    def show_profile(self):
        if not self.has_character():
            print("\nNo character found. Please create one first.\n")
            return

        print(self.banner_PP)
        print("| 👤 Player Profile |")
        print(self.banner_PP)
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Gender : {self.gender}\n")

# ---------------- GAME CONTROLLER ----------------
class BioQuestGame:
    def __init__(self):
        self.home = HomeSection()
        self.banner = "=" * 23
        #self.login_system = LoginSection("Rai011906", "567245")
        self.login_system = LoginSection("R", "5")
        self.player = Player()

    def start_game(self):
        self.home.display_header()

        if not self.home.verification():
            return

        if not self.login_system.login():
            return

        self.player.create_character()
        self.main_menu()

    def main_menu(self):
        while True:
            print(self.banner)
            print("| Bio-Quest Main Menu |")
            print(self.banner)
            print("1. Start Bio Quest")
            print("2. View Player Profile")
            print("3. Update Character")
            print("4. Delete Character")
            print("5. Exit Game")

            choice = input("\nChoose an option: ")
            print()

            if choice == "1":
                self.start_bio_quest()
            elif choice == "2":
                self.player.show_profile()
            elif choice == "3":
                self.player.update_character()
            elif choice == "4":
                self.player.delete_character()
            elif choice == "5":
                print("\nThank you for playing Bio-Quest RPG! 👋")
                break
            else:
                print("\nInvalid choice. Please try again.")

    def start_bio_quest(self):
        print("\n🧬 Bio Quest Started!")
        print("Exploring biological data and personal stats...\n")

# ---------------- RUN THE GAME ----------------
game = BioQuestGame()
game.start_game()
