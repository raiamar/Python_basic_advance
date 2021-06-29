'''
class Games:
    def __init__(self, name, players):
        self.game_name = name
        self.num_of_player = players

    def a_message(self):
        print(f"Playing {self.game_name} is fun!!")

class Football(Games):
    def __init__(self, name, players):
        super().__init__(name, players)


    def num_of_players(self):
        print(f"In {self.game_name} there are {self.num_of_player} players in each team")

class Basketball(Games):
    def __init__(self,name, players):
        super().__init__(name, players)

    def num_of_players(self):
        print(f"In {self.game_name} there are {self.num_of_player} players in each team")


first_game = Football("Football", 11)
second_game = Basketball("Basketball", 5)
first_game.a_message()
first_game.num_of_players()
second_game.a_message()
second_game.num_of_players()
'''

#overloading
class Product:
    def __inti__(self, name, price):
        self.name = name
        self.price = price 

    #def __eq__(self, object):
        #return self.price == object.prices

p1 = Product("Pant", 2000)
p2 = Product("T-shirt", 2000)
print(p1 == p2)