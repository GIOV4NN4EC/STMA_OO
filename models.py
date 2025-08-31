from abc import ABC, abstractmethod

# Classe para enquetes
class Poll:
    poll_id_counter = 0
    def __init__(self, title, description, opt1, opt2, opt3):
        Poll.poll_id_counter += 1
        self.__title = title
        self.__description = description
        self.__opt1 = opt1
        self.__opt2 = opt2
        self.__opt3 = opt3

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def opt1(self):
        return self.__opt1

    @property
    def opt2(self):
        return self.__opt2

    @property
    def opt3(self):
        return self.__opt3

# Classe para postagens
class Post:
    post_id_counter = 0
    def __init__(self, title, content, date):
        Post.post_id_counter += 1
        self.__title = title
        self.__content = content
        self.__date = date

    @property
    def title(self):
        return self.__title

    @property
    def content(self):
        return self.__content

    @property
    def date(self):
        return self.__date

# Classe para conta bancária
class Account:
    def __init__(self, balance):
        self.__balance  = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

# Classe para Recruta
class Recruit:
    recruit_id_counter = 0
    def __init__(self, name, age, pros, cons, position, observation):
        Recruit.recruit_id_counter += 1
        self.__name = name
        self.__age = age
        self.__pros = pros
        self.__cons = cons
        self.__position = position
        self.__observation = observation

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def pros(self):
        return self.__pros

    @property
    def cons(self):
        return self.__cons

    @property
    def position(self):
        return self.__position

    @property
    def observation(self):
        return self.__observation

# Classe para equipamentos
class Equipment:
    equipment_id_counter = 0
    def __init__(self, name, type, quantity, status, observation):
        Equipment.equipment_id_counter += 1
        self.__name = name
        self.__type = type
        self.__quantity = quantity
        self.__status = status
        self.__observation = observation

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def quantity(self):
        return self.__quantity

    @property
    def status(self):
        return self.__status

    @property
    def observation(self):
        return self.__observation

# Classe para estatísticas do jogador
class Stats:
    def __init__(self, score, games_played):
        self.__score = score
        self.__games_played = games_played

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def games_played(self):
        return self.__games_played

    @games_played.setter
    def games_played(self, value):
        self.__games_played = value

# Classe para jogador
class Player:
    id_inicial = 0

    def __init__(self, id, name, age, position, stats, health):
        Player.id_inicial += 1
        self.__id = Player.id_inicial
        self.__name = name
        self.__age = age
        self.__position = position
        self.__stats = stats
        self.__health = health

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def stats(self):
        return self.__stats

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

# Classe abstrata para eventos
class Event(ABC):
    event_id_counter = 0

    def __init__(self, date, time, location):
        Event.event_id_counter += 1
        self._id = Event.event_id_counter
        self._date = date
        self._time = time
        self._location = location

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def location(self):
        return self._location

    @abstractmethod
    def details(self):
        pass

# Subclasse para partidas
class Match(Event):
    def __init__(self, date, time, opponent, location):
        super().__init__(date, time, location)
        self.__opponent = opponent
        self.__result = None

    @property
    def opponent(self):
        return self.__opponent

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    def details(self):
        return (f"ID: {self.id} | MATCH vs {self.opponent} | "
                f"DATE: {self.date} | TIME: {self.time} | "
                f"LOCATION: {self.location} | RESULT: {self.result or 'NOT DEFINED'}")

# Subclasse para treinamentos
class Training(Event):
    def __init__(self, date, time, location, focus):
        super().__init__(date, time, location)
        self.__focus = focus

    @property
    def focus(self):
        return self.__focus

    def details(self):
        return (f"ID: {self.id} | TRAINING | DATE: {self.date} | TIME: {self.time} | "
                f"LOCATION: {self.location} | FOCUS: {self.focus}")
