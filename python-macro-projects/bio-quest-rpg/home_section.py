class HomeSection:
    def __init__(self):
        self.banner = "=" * 36

    def display_header(self):
        print(self.banner)
        print("| Welcome to 🧬 Bio-Quest RPG Game |")
        print(self.banner)

    def verification(self):
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice not in ("yes", "y"):
            print("\nThank you! Exiting the game.")
            return False
        print("\nGreat! Let's proceed.\n")
        return True
