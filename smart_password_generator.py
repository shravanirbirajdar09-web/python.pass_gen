# SMART PASSWORD GENERATOR PROJECT
# Using Python

import random
import string
from datetime import datetime

# -----------------------------
# QUESTION BANK (80 QUESTIONS)
# -----------------------------

questions = [

"What is your first name?",
"What is your middle name?",
"What is your last name?",
"What is your nickname?",
"What is your birth year?",
"What is your birth month?",
"What is your birth date?",
"What is your lucky number?",
"What is your favorite number?",
"What is your favorite color?",

"What is your mother's first name?",
"What is your father's first name?",
"What is your mother's nickname?",
"What is your father's nickname?",
"What is your sibling's name?",
"What is your grandmother's name?",
"What is your grandfather's name?",
"What is your cousin's name?",
"What is your uncle's name?",
"What is your aunt's name?",

"What is the name of your school?",
"What is the name of your college?",
"What is your favorite subject?",
"What is your favorite teacher's name?",
"What was your classroom number?",
"What is your college ID number?",
"What is your roll number?",
"What is your favorite lab subject?",
"What was your school bus number?",
"What is your graduation year?",

"What is your best friend's name?",
"What is your childhood friend's name?",
"What is your friend's nickname?",
"What is your friend's lucky number?",
"What is your friend's birth year?",
"What is your friend's favorite color?",
"What is your friend's favorite sport?",
"What is your friend's favorite food?",
"What city does your friend live in?",
"What is your group name with friends?",

"What is your favorite food?",
"What is your favorite fruit?",
"What is your favorite vegetable?",
"What is your favorite movie?",
"What is your favorite actor?",
"What is your favorite actress?",
"What is your favorite singer?",
"What is your favorite sport?",
"What is your favorite team?",
"What is your favorite festival?",

"What city were you born in?",
"What city do you live in?",
"What is your favorite travel destination?",
"What is your favorite restaurant?",
"What is your favorite park?",
"What is your dream country to visit?",
"What is your hometown name?",
"What is your favorite holiday place?",
"What is your favorite beach?",
"What is your favorite mall?",

"What is your favorite hobby?",
"What game do you like the most?",
"What is your favorite mobile app?",
"What is your favorite social media platform?",
"What is your favorite book?",
"What is your favorite TV show?",
"What is your favorite cartoon?",
"What is your favorite video game?",
"What is your favorite weekend activity?",
"What is your dream job?",

"What is your favorite two digit number?",
"What is your favorite three digit number?",
"What is your favorite special symbol?",
"What year did you start school?",
"What year did you join college?",
"What is your vehicle number?",
"What is your house number?",
"What is your favorite password word?",
"What is your lucky symbol?",
"What is your dream company?"
]

# --------------------------------
# FUNCTION: SELECT RANDOM QUESTIONS
# --------------------------------

def ask_questions():

    selected = random.sample(questions,3)
    answers = []

    print("\nAnswer the following questions:\n")

    for q in selected:
        ans = input(q + " ")
        answers.append(ans)

    return answers

# --------------------------------
# FUNCTION: GENERATE PASSWORD
# --------------------------------

def generate_password(answers,length):

    base = ""

    for ans in answers:
        if len(ans) >= 2:
            base += ans[:2]
        else:
            base += ans

    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    password = base + upper + lower + digit + symbol

    while len(password) < length:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    password = ''.join(random.sample(password,len(password)))

    return password

# --------------------------------
# FUNCTION: CHECK PASSWORD STRENGTH
# --------------------------------

def check_strength(password):

    score = 0

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if len(password) >= 8:
        score += 1

    if score <= 2:
        return "Weak"

    elif score == 3 or score == 4:
        return "Medium"

    else:
        return "Strong"

# --------------------------------
# FUNCTION: SAVE PASSWORD LOCALLY
# --------------------------------

def save_local(password,strength):

    with open("generated_passwords.txt","a") as file:

        file.write(
            str(datetime.now()) +
            " | " +
            password +
            " | " +
            strength +
            "\n"
        )

# --------------------------------
# OPTIONAL: SAVE TO GOOGLE SHEETS
# --------------------------------

def save_google_sheet(password,strength):

    try:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json",scope)

        client = gspread.authorize(creds)

        sheet = client.open("PasswordGenerator").sheet1

        sheet.append_row([
        str(datetime.now()),
        password,
        strength
        ])

        print("Saved to Google Sheet")

    except:

        print("Google Sheet not configured. Skipped.")

# --------------------------------
# MAIN PROGRAM
# --------------------------------

def main():

    print("\nSMART PASSWORD GENERATOR")
    print("------------------------")

    try:

        length = int(input("Enter desired password length (minimum 8): "))

        if length < 8:
            length = 8

    except:

        length = 8

    answers = ask_questions()

    password = generate_password(answers,length)

    strength = check_strength(password)

    print("\nGenerated Password:",password)

    print("Password Strength:",strength)

    save_local(password,strength)

    save_google_sheet(password,strength)

    print("\nPassword saved successfully.")

# --------------------------------
# PROGRAM START
# --------------------------------

if __name__ == "__main__":

    main()