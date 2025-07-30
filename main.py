team = []
players = [] #lista de jogadores
recruits = [] #lista de recrutas
events = [] #lista de eventos (partidas ou treinos)
equipments = [] #lista de equipamentos
injuried_players = [] #lista de jogadores lesionados

class Team:
    pass

class Poll:
    poll_id_counter = 0
    def __init__(self, title, description, opt1, opt2, opt3):
        Poll.poll_id_counter += 1
        self.title = title
        self.description = description
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3
        
class Post:
    post_id_counter = 0
    def __init__(self, title, content, date):
        Post.post_id_counter += 1
        self.title = title
        self.content = content
        self.date = date


class Account:
    def __init__(self, balance):
        self.balance  = balance

class Recruit:
    recruit_id_counter = 0
    def __init__(self, name, age, pros, cons, position, observation):
        Recruit.recruit_id_counter += 1
        self.name = name
        self.age = age
        self.pros = pros
        self.cons = cons
        self.position = position
        self.observation = observation
        

class Equipment:
    equipment_id_counter = 0
    def __init__(self, name, type, quantity, status, observation):
        Equipment.equipment_id_counter += 1
        self.name = name
        self.type = type
        self.quantity = quantity
        self.status = status
        self.observation = observation
        

class Stats:
    def __init__(self, score, games_played, yellow_cards, red_cards):
        self.score = score
        self.games_played = games_played
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


#Classe para os jogadores
class Player:
    id_inicial = 0 #contador para que não tenham IDs repetidos

    def __init__(self, name, age, position, stats, health):
        Player.id_inicial += 1
        self.id = Player.id_inicial #ID único do jogador
        self.name = name #nome do jogador
        self.age = age #nome do jogador
        self.position = position #posição do jogador
        self.stats = stats #estatística do jogador (nesse caso, aproveitamento)
        self.health = health #estado de saúde do jogador

#Classe para os eventos
class Match:
    match_id_counter = 0 #contador para identificar as partidas

    def __init__(self, date, time, location, opponent):
        Match.match_id_counter += 1
        self.id = Match.match_id_counter #ID da partida
        self.date = date #data do evento
        self.time = time
        self.location = location #local da partida
        self.opponent = opponent #oponente (se houver)
        self.result = None  #resultado (se houver)

class Training:
    training_id_counter = 0 #contador para identificar os eventos

    def __init__(self, date, time, location, focus):
        Training.training_id_counter += 1
        self.id = Training.training_id_counter #ID da partida
        self.date = date #data do evento
        self.time = time
        self.location = location #local da partida
        self.focus = focus #objetivo do treino (se houiver)

def team_management():
    pass

def schedule_event():
    pass

def performance_tracking():
    pass

def health_monitoring():
    pass

def manage_equipments():
    pass

def manage_player_recruitment():
    pass

def manage_finances():
    pass

def media_and_social():
    pass

