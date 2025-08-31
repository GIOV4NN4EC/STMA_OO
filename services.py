from models import Player, Stats, Match, Training, Recruit, Equipment, Post, Poll
import data

def add_player():
    name = input("NAME: ")
    age = input("AGE: ")
    position = input("POSITION: ")

    print("\nPLAYER STATS:")
    try:
        score = int(input("GOALS SCORED: "))
        games_played = int(input("GAMES PLAYED: "))
    except ValueError:
        print("INVALID VALUES. USE INTEGERS")
        return

    stats = Stats(score, games_played)
    health = input("PLAYER HEALTH STATUS: ")

    new_player = Player(Player.id_inicial, name, age, position, stats, health)
    data.players.append(new_player)
    print("PLAYER REGISTERED SUCCESSFULLY!")


def list_players():
    if not data.players:
        print("NO PLAYERS REGISTERED IN THE SYSTEM.")
        return

    print("\nPLAYERS LIST:")
    for player in data.players:
        print(f"ID: {player.id} | NAME: {player.name} | AGE: {player.age} | POSITION: {player.position} | HEALTH STATUS: {player.health}")
        print("-" * 90)


def edit_player():
    try:
        search_id = int(input("ENTER PLAYER ID TO EDIT: "))
    except ValueError:
        print("INVALID ID.")
        return

    for player in data.players:
        if player.id == search_id:
            print(f"\nEDITING PLAYER {player.name} (ID {player.id})")

            new_name = input(f"NEW NAME (OR ENTER TO KEEP '{player.name}'): ")
            new_position = input(f"NEW POSITION (OR ENTER TO KEEP '{player.position}'): ")

            if new_name.strip():
                player.name = new_name
            if new_position.strip():
                player.position = new_position

            print("\nEDIT STATS:")
            try:
                new_score = input(f"GOALS (CURRENT: {player.stats.score}): ")
                new_games = input(f"GAMES (CURRENT: {player.stats.games_played}): ")

                if new_score.strip():
                    player.stats.score = int(new_score)
                if new_games.strip():
                    player.stats.games_played = int(new_games)

            except ValueError:
                print("INVALID VALUE FOR STATS.")

            print("PLAYER UPDATED SUCCESSFULLY!")
            return
    print("PLAYER NOT FOUND!")


def remove_player():
    try:
        search_id = int(input("ENTER PLAYER ID TO REMOVE: "))
    except ValueError:
        print("INVALID ID.")
        return

    for player in data.players:
        if player.id == search_id:
            data.players.remove(player)
            print("PLAYER REMOVED SUCCESSFULLY!")
            return
    print("PLAYER NOT FOUND!")


def schedule_match():
    date = input("ENTER MATCH DATE: ")
    time = input("ENTER MATCH TIME: ")
    opponent = input("ENTER OPPONENT NAME: ")
    location = input("ENTER MATCH LOCATION: ")
    new_match = Match(date, time, opponent, location)
    data.events.append(new_match)


def schedule_training():
    date = input("ENTER TRAINING DATE: ")
    time = input("ENTER TRAINING TIME: ")
    location = input("ENTER TRAINING LOCATION: ")
    focus = input("ENTER TRAINING OBJECTIVE: ")
    new_training = Training(date, time, location, focus)
    data.events.append(new_training)


def list_events():
    if not data.events:
        print("NO EVENTS REGISTERED.")
        return

    print("\nEVENTS LIST:")
    for event in data.events:
        print(event.details())
        print("-" * 90)


def delete_event():
    if not data.events:
        print("NO EVENTS REGISTERED.")
        return

    list_events()
    try:
        id_remove = int(input("\nENTER EVENT ID TO REMOVE: "))
    except ValueError:
        print("INVALID ID.")
        return

    for event in data.events:
        if event.id == id_remove:
            data.events.remove(event)
            print("EVENT REMOVED SUCCESSFULLY!")
            return
    print("EVENT NOT FOUND!")


def register_result():
    if not data.events:
        print("NO MATCHES REGISTERED.")
        return

    list_events()
    try:
        match_id = int(input("ENTER MATCH ID TO REGISTER RESULT: "))
    except ValueError:
        print("INVALID ID.")
        return

    for event in data.events:
        if isinstance(event, Match) and event.id == match_id:
            result = input("ENTER MATCH RESULT (EX: WIN 2x1, LOSS 0x3): ")
            if result:
                event.result = result
                print("RESULT REGISTERED SUCCESSFULLY.")
            else:
                print("NO CHANGES MADE.")
            return
    print("MATCH NOT FOUND.")


def performance_tracking():
    if not data.players:
        print("NO PLAYERS REGISTERED.")
        return

    print("\nPLAYERS PERFORMANCE REPORT:")
    for player in data.players:
        aproveitamento = float(player.stats.score / player.stats.games_played) if player.stats.games_played > 0 else 0
        print(f"ID: {player.id} | NAME: {player.name} | GOALS PER GAME AVERAGE: {aproveitamento:.2f}")
        print("-" * 90)
def add_player():
    name = input("NAME: ")
    age = input("AGE: ")
    position = input("POSITION: ")

    print("\nPLAYER STATS:")
    try:
        score = int(input("GOALS SCORED: "))
        games_played = int(input("GAMES PLAYED: "))
    except ValueError:
        print("INVALID VALUES. USE INTEGERS")
        return

    stats = Stats(score, games_played)
    health = input("PLAYER HEALTH STATUS: ")

    new_player = Player(Player.id_inicial, name, age, position, stats, health)
    data.players.append(new_player)
    print("PLAYER REGISTERED SUCCESSFULLY!")


def list_players():
    if not data.players:
        print("NO PLAYERS REGISTERED IN THE SYSTEM.")
        return

    print("\nPLAYERS LIST:")
    for player in data.players:
        print(f"ID: {player.id} | NAME: {player.name} | AGE: {player.age} | POSITION: {player.position} | HEALTH STATUS: {player.health}")
        print("-" * 90)


def edit_player():
    try:
        search_id = int(input("ENTER PLAYER ID TO EDIT: "))
    except ValueError:
        print("INVALID ID.")
        return

    for player in data.players:
        if player.id == search_id:
            print(f"\nEDITING PLAYER {player.name} (ID {player.id})")

            new_name = input(f"NEW NAME (OR ENTER TO KEEP '{player.name}'): ")
            new_position = input(f"NEW POSITION (OR ENTER TO KEEP '{player.position}'): ")

            if new_name.strip():
                player.name = new_name
            if new_position.strip():
                player.position = new_position

            print("\nEDIT STATS:")
            try:
                new_score = input(f"GOALS (CURRENT: {player.stats.score}): ")
                new_games = input(f"GAMES (CURRENT: {player.stats.games_played}): ")

                if new_score.strip():
                    player.stats.score = int(new_score)
                if new_games.strip():
                    player.stats.games_played = int(new_games)

            except ValueError:
                print("INVALID VALUE FOR STATS.")

            print("PLAYER UPDATED SUCCESSFULLY!")
            return
    print("PLAYER NOT FOUND!")


def remove_player():
    try:
        search_id = int(input("ENTER PLAYER ID TO REMOVE: "))
    except ValueError:
        print("INVALID ID.")
        return

    for player in data.players:
        if player.id == search_id:
            data.players.remove(player)
            print("PLAYER REMOVED SUCCESSFULLY!")
            return
    print("PLAYER NOT FOUND!")


def schedule_match():
    date = input("ENTER MATCH DATE: ")
    time = input("ENTER MATCH TIME: ")
    opponent = input("ENTER OPPONENT NAME: ")
    location = input("ENTER MATCH LOCATION: ")
    new_match = Match(date, time, opponent, location)
    data.events.append(new_match)


def schedule_training():
    date = input("ENTER TRAINING DATE: ")
    time = input("ENTER TRAINING TIME: ")
    location = input("ENTER TRAINING LOCATION: ")
    focus = input("ENTER TRAINING OBJECTIVE: ")
    new_training = Training(date, time, location, focus)
    data.events.append(new_training)


def list_events():
    if not data.events:
        print("NO EVENTS REGISTERED.")
        return

    print("\nEVENTS LIST:")
    for event in data.events:
        print(event.details())
        print("-" * 90)


def delete_event():
    if not data.events:
        print("NO EVENTS REGISTERED.")
        return

    list_events()
    try:
        id_remove = int(input("\nENTER EVENT ID TO REMOVE: "))
    except ValueError:
        print("INVALID ID.")
        return

    for event in data.events:
        if event.id == id_remove:
            data.events.remove(event)
            print("EVENT REMOVED SUCCESSFULLY!")
            return
    print("EVENT NOT FOUND!")


def register_result():
    if not data.events:
        print("NO MATCHES REGISTERED.")
        return

    list_events()
    try:
        match_id = int(input("ENTER MATCH ID TO REGISTER RESULT: "))
    except ValueError:
        print("INVALID ID.")
        return

    for event in data.events:
        if isinstance(event, Match) and event.id == match_id:
            result = input("ENTER MATCH RESULT (EX: WIN 2x1, LOSS 0x3): ")
            if result:
                event.result = result
                print("RESULT REGISTERED SUCCESSFULLY.")
            else:
                print("NO CHANGES MADE.")
            return
    print("MATCH NOT FOUND.")


def performance_tracking():
    if not data.players:
        print("NO PLAYERS REGISTERED.")
        return

    print("\nPLAYERS PERFORMANCE REPORT:")
    for player in data.players:
        aproveitamento = float(player.stats.score / player.stats.games_played) if player.stats.games_played > 0 else 0
        print(f"ID: {player.id} | NAME: {player.name} | GOALS PER GAME AVERAGE: {aproveitamento:.2f}")
        print("-" * 90)

def list_recruits():
    for recruit in data.recruits:
                print(f"NAME: {recruit.name} | AGE: {recruit.age} | POSITION: {recruit.position} | STRENGTHS: {recruit.pros} | WEAKNESSES: {recruit.cons} | OBS: {recruit.observation}")
                print("-"*90)

def add_recruit():
    name = input("NAME: ")
    age = input("AGE: ")
    pros = input("STRENGTHS: ")
    cons = input("WEAKNESSES: ")
    position = input("POSITION: ")
    observation = input("OBSERVATION: ")
    recruit = Recruit(name, age, pros, cons, position, observation)
    data.recruits.append(recruit)

def add_equipment():
    name = input("NAME: ")
    type = input("TYPE: ")
    quantity = input("QUANTITY: ")
    status = input("STATUS: ")
    observation = input("OBSERVATIONS: ")
    new_equipment = Equipment(name, type, quantity, status, observation)
    data.equipments.append(new_equipment)

def list_equipments():
    for equipment in data.equipments:
                print(f"NAME: {equipment.name} | TYPE: {equipment.type} | QUANTITY: {equipment.quantity} | STATUS: {equipment.status} | OBSERVATION: {equipment.observation}")
                print("-"*90)

def list_injuried_players():
    print("\n| INJURIED PLAYERS LIST |")
    print("-"*30)
    for player in data.players:
        if player.health != 'healthy':
            print(f" #{player.id} - {player.name} ({player.health})")
    print("-"*30)

def register_income():
    value = float(input("INCOME VALUE: "))
    data.account.balance += value

def register_expense():
    value = float(input("EXPENSE VALUE: "))
    data.account.balance -= value

def create_poll():
    title = input("POLL TITLE: ")
    desc = input("DESCRIPTION: ")
    opt1 = input("OPTION 1: ")
    opt2 = input("OPTION 2: ")
    opt3 = input("OPTION 3: ")
    data.polls.append(Poll(title, desc, opt1, opt2, opt3))

def create_post():
    title = input("POST TITLE: ")
    content = input("CONTENT: ")
    date = input("DATE: ")
    data.posts.append(Post(title, content, date))

def list_polls():
    for p in data.polls:
        print("-"*90)
        print(f"POLL: {p.title} | {p.description} \n[1] {p.opt1} [2] {p.opt2} [3] {p.opt3}")
        print("-"*90)

def list_posts():
    for post in data.posts:
        print("-"*90)
        print(f"POST: {post.title} | {post.date}\n{post.content}\n")
        print("-"*90)