import random
from task2a import Pokemon


class Trainer(object):
    def __init__(self, name):
        self.__name = name
        self.__pokemon_lst = []

    def get_name(self):
        return self.__name

    def get_pokemons(self):
        return self.__pokemon_lst

    def catch_pokemon(self, pokemon):
        int1 = random.randint(1, 100)
        if int1 % pokemon.get_catchrate() == 0:
            if len(self.__pokemon_lst) < 6:
                self.__pokemon_lst.append(pokemon)
                print("%s has caught %s!" % (Trainer.get_name(self), pokemon.get_kind()))
            else:
                print("%s already has six Pokemon!" % Trainer.get_name(self))
        else:
            print("The Pokemon fled!")

    def print_pokemon_stats(self):
        if len(Trainer.get_pokemons(self)) > 0:
            print("%s's Pokemon are:" % Trainer.get_name(self))
            index = 1
            for pok in Trainer.get_pokemons(self):
                print("%s at spot #%d with strength: %s" % (pok.get_kind(), index, pok.get_strength()))
                index += 1
        else:
            print("%s hasn't caught any Pokemon!" % Trainer.get_name(self))

    def release_pokemon(self, remove_index):
        if remove_index <= len(Trainer.get_pokemons(self)):
            self.__pokemon_lst.remove(self.__pokemon_lst[remove_index-1])
        else:
            pass
