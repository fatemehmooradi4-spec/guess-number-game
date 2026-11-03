import random

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0

    ranks = [
        "Awli (Nemouneh)",
        "Kheyli Khoob",
        "Khoob",
        "Ghabool",
        "Ba Shans Bordin!"
    ]

    print("\n" + "=" * 40)
    print("Be bazi Hads Adad khosh amadid!")
    print("Yek adad bein 1 ta 100 entekhab shode ast.")
    print("Shoma hadeaksar 5 forsat darid.")
    print("=" * 40)

    while attempts < max_attempts:
        print(f"\nTalash {attempts + 1} az {max_attempts}")
        print(f"Jaan-haye baghimandeh: {max_attempts - attempts}")

        user_input = input("Hads khod ra vared konid: ").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("Khata! Lotfan faghat adad sahih vared konid.")
            continue

        if guess < 1 or guess > 100:
            print("Khata! Adad bayad bein 1 ta 100 bashad.")
            continue

        attempts += 1

        if guess == secret_number:
            print("\nAfarin! Adad ra dorost hads zadid.")
            print(f"Tedad talash-haye shoma: {attempts}")
            print(f"Rotbeh shoma: {ranks[attempts - 1]}")
            return

        if guess > secret_number:
            print("Rahnama: Koochiktar vared kon.")
        else:
            print("Rahnama: Bozorgtar vared kon.")

        diff = abs(guess - secret_number)
        if diff <= 5:
            print("Vazeiat: Kheyli nazdiki!")
        elif diff <= 15:
            print("Vazeiat: Nazdiki, vali hanooz faseleh dari!")
        else:
            print("Vazeiat: Kheyli doori!")

    print("\nForsat-haye shoma tamam shod va bakhtid!")
    print(f"Adade makhfi in dor: {secret_number}")

def main():
    while True:
        play_game()
        while True:
            choice = input("\nAya mikhahid dobareh bazi konid? (bale/kheyr): ").strip().lower()
            if choice in ["bale", "yes", "y"]:
                break
            elif choice in ["kheyr", "no", "n"]:
                print("Mamnoon, khodafez!")
                return
            else:
                print("Lotfan faghat bale ya kheyr vared konid.")

if __name__ == "__main__":
    main()
