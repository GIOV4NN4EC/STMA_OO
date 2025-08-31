import services as sv

def manage_player_recruitment():
    print("\nRECRUITS MANAGEMENT")
    while True:
        print("1. ADD RECRUIT")
        print("2. LIST RECRUITS")
        print("0. BACK")
        escolha = input("CHOOSE: ")

        if escolha == "1":
            sv.add_recruit()
        elif escolha == "2":
            sv.list_recruits()
        elif escolha == "0":
            break
        else:
            print("INVALID OPTION!")

def manage_players():
    while True:
        print("\nPLAYERS MANAGEMENT MENU")
        print("1. ADD PLAYER")
        print("2. LIST PLAYERS")
        print("3. EDIT PLAYER")
        print("4. REMOVE PLAYER")
        print("5. MANAGE RECRUITS")
        print("0. BACK")
        option = input("CHOOSE: ")

        if option == "1":
            sv.add_player()
        elif option == "2":
            sv.list_players()
        elif option == "3":
            sv.edit_player()
        elif option == "4":
            sv.remove_player()
        elif option == "5":
            sv.manage_player_recruitment()
        elif option == "0":
            break
        else:
            print("INVALID OPTION.")


def team_management():
    while True:
        print("\nTEAM MANAGEMENT MENU")
        print("1. MANAGE PLAYERS")
        print("2. PERFORMANCE TRACKING")
        print("3. HEALTH MONITORING")
        print("4. MANAGE RECRUITS")
        print("0. BACK")
        option = input("CHOOSE: ")
        if option == "1":
            manage_players()
        elif option == "2":
            sv.performance_tracking()
        elif option == "3":
            sv.health_monitoring()
        elif option == "4":
            sv.manage_player_recruitment()
        elif option == "0":
            break
        else:
            print("INVALID OPTION.")


def schedule_event():
    while True:
        print("\nEVENTS MANAGEMENT MENU")
        print("1. SCHEDULE MATCH")
        print("2. SCHEDULE TRAINING")
        print("3. LIST EVENTS")
        print("4. REMOVE EVENT")
        print("5. ADD MATCH RESULT")
        print("0. BACK")
        option = input("CHOOSE: ")

        if option == "1":
            sv.schedule_match()
        elif option == "2":
            sv.schedule_training()
        elif option == "3":
            sv.list_events()
        elif option == "4":
            sv.delete_event()
        elif option == "5":
            sv.register_result()
        elif option == "0":
            break
        else:
            print("INVALID OPTION.")

def health_monitoring():
    while True:
        print("1. LIST INJURIED PLAYERS")
        print("0. BACK")

        option = input("CHOOSE AN OPTION: ").strip()

        if option == "1":
            sv.list_injuried_players()
        elif option == "0":
            break
        else:
            print("INVALID OPTION.")


def manage_equipments():
    print("\nEQUIPMENT MANAGEMENT")
    while True:
        print("1. ADD EQUIPMENT")
        print("2. LIST EQUIPMENTS")
        print("0. BACK")
        escolha = input("CHOOSE: ")

        if escolha == "1":
            sv.add_equipment()
        elif escolha == "2":
            sv.list_equipments()
        elif escolha == "0":
            break
        else:
            print("INVALID OPTION!")

def manage_finances():
    print("\nFINANCIAL MANAGEMENT")
    while True:
        print(f"CURRENT BALANCE: $ {sv.account.balance:.2f}")
        print("1. REGISTER INCOME")
        print("2. REGISTER EXPENSE")
        print("0. BACK")
        option = input("CHOOSE: ")

        if option == "1":
            sv.register_income()
        elif option == "2":
            sv.register_expense()
        elif option == "0":
            break
        else:
            print("INVALID OPTION!")

def media_and_social():
    print("\nMEDIA AND PUBLIC RELATIONS")
    while True:
        print("1. CREATE POLL")
        print("2. CREATE POST")
        print("3. LIST POLLS")
        print("4. LIST POSTS")
        print("0. BACK")
        option = input("CHOOSE: ")

        if option == "1":
            sv.create_poll()
        elif option == "2":
            sv.create_post()
        elif option == "3":
            sv.list_polls()
        elif option == "4":
            sv.list_posts()
        elif option == "0":
            break
        else:
            print("INVALID OPTION!")

def main_menu():
    while True:
        print("\n-----SPORTS TEAM MANAGEMENT APP-----")
        print(" SELECT AN OPTION:")
        print("1. MANAGE TEAM AND PLAYERS")
        print("2. MANAGE MATCHES AND TRAININGS")
        print("3. MANAGE EQUIPMENT")
        print("4. MANAGE FINANCES")
        print("5. MEDIA AND SOCIAL")
        print("0. EXIT")

        option = input("")

        if option == "1":
            team_management()
        elif option == "2":
            schedule_event()
        elif option == "3":
            manage_equipments()
        elif option == "4":
            manage_finances()
        elif option == "5":
            media_and_social()
        elif option == "0":
            print("CLOSING SYSTEM.")
            break
        else:
            print("INVALID OPTION!")