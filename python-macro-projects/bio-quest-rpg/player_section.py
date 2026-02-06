class Player:
    def __init__(self):
        self.banner_CC = "=" * 24
        self.banner_UP = "=" * 20
        self.banner_PP = "=" * 21
        self.name = ""
        self.age = 0
        self.gender = ""

    def has_character(self):
        return self.name != ""

    def create_character(self):
        print(self.banner_CC)
        print("|🧍 Character Creation |")
        print(self.banner_CC)
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")
        print("\nCharacter created successfully!\n")

    def update_character(self):
        if not self.has_character():
            print("\nNo character to update.\n")
            return
        
        print(self.banner_UP)
        print("|🧍 Update Profile |")
        print(self.banner_UP)
        self.name = input("Enter new name: ")
        self.age = int(input("Enter new age: "))
        self.gender = input("Enter new gender: ")
        print("\nCharacter updated successfully!\n")

    def delete_character(self):
        if not self.has_character():
            print("\nNo character to delete.\n")
            return

        confirm = input("Delete character? (yes/no): ").lower()
        if confirm in ("yes", "y"):
            self.name = ""
            self.age = 0
            self.gender = ""
            print("\nCharacter deleted.\n")

    def show_profile(self):
        if not self.has_character():
            print("\nNo character found.\n")
            return
        
        print(self.banner_PP) 
        print("| 👤 Player Profile |")
        print(self.banner_PP)
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Gender : {self.gender}")
