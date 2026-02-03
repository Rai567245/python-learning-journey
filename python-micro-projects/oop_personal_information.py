# This program demonstrates a simple personal information display with input validation.
class PersonalInformation:
    def __init__(self):
        self.banner = "=" * 40

    def display_header(self): 
        print(self.banner)
        print("|      Personal Information      |")
        print(self.banner)

    def gather_information(self):
        self.display_header()
        while True:
            self.name = input("Name: ").strip()
            if self.name:
                break
            print("Name cannot be empty. Please try again.")

        while True:
            self.sex = input("Sex (Male/Female): ").strip().lower()
            if self.sex in ["male", "female"]:
                self.sex = self.sex.capitalize()
                break
            print("Invalid input. Please enter Male or Female.")

        valid_eye_colors = ["green", "brown", "black"]
        while True:
            self.eye_color = input("Eye color (Green/Brown/Black): ").strip().lower()
            if self.eye_color in valid_eye_colors:
                self.eye_color = self.eye_color.capitalize()
                break
            print("Invalid eye color. Please choose Green, Brown, or Black.")
        
        while True:
            self.cat_apply = input("Check all that apply (Over 6 feet tall / Over 200 pounds / None): ").strip().lower()

            if self.cat_apply in ["over 6 feet tall", "over 200 pounds", "none"]:
                self.cat_apply = self.cat_apply.capitalize()
                break
            print("Invalid option. Please type one of the given choices.")

        while True:
            self.athletic_ability = input("Describe your athletic ability: ").strip()
            if self.athletic_ability:
                break
            print("This field cannot be empty. Please describe your ability.")

    def display_information(self):
        self.display_header()
        print(f"Name: {self.name}")
        print(f"Sex: {self.sex}")
        print(f"Eye Color: {self.eye_color}")
        print(f"Check all that apply: {self.cat_apply}")
        print(f"Athletic Ability: {self.athletic_ability}")

def main():
    personal_info = PersonalInformation()
    personal_info.gather_information()
    personal_info.display_information()

main()
