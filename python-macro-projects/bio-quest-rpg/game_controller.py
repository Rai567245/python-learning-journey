from home_section import HomeSection
from login_section import LoginSection
from player_section import Player

class BioQuestGame:
    def __init__(self):
        self.home = HomeSection()
        self.login_system = LoginSection("Rai011906", "567245")
        self.player = Player()
        self.banner = "=" * 23

    def start_game(self):
        self.home.display_header()

        if not self.home.verification():
            print("Verification failed. Exiting...")
            return

        if not self.login_system.login():
            print("Login failed. Exiting...")
            return

        self.player.create_character()
        self.main_menu()

    def main_menu(self):
        while True:
            print(f"\n{self.banner}")
            print("| Bio-Quest Main Menu |")
            print(self.banner)
            print("1. Start Bio Quest")
            print("2. View Player Profile")
            print("3. Update Character")
            print("4. Delete Character")
            print("5. Exit Game")

            choice = input("\nChoose an option: ")

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
        print("\n🧬 Bio Quest Started!\n")
        # Add your quest logic here