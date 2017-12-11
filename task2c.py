from task2a import Pokemon
from task2b import Trainer


def fight(trainer1, trainer2):
    pkmn_trainer1 = trainer1.get_pokemons()
    pkmn_trainer2 = trainer2.get_pokemons()
    while pkmn_trainer1 != [] and pkmn_trainer2 != []:
        pkmn_trainer1[0].attack(pkmn_trainer2[0])
        if pkmn_trainer2[0].get_strength() <= 0:
            trainer2.release_pokemon(1)
        if pkmn_trainer1 == [] and pkmn_trainer2 == []:
            print("You cannot fight!")
            return
        elif pkmn_trainer1 == []:
            print("{0:s} has no pokemon left. {1:s} won!".format(trainer1.get_name(), trainer2.get_name()))
            return
        elif pkmn_trainer2 == []:
            print("{0:s} has no pokemon left. {1:s} won!".format(trainer2.get_name(), trainer1.get_name()))
            return
        fight(trainer2, trainer1)


ash = Trainer("Ash")
ash.catch_pokemon(Pokemon("Pidgey"))
ash.catch_pokemon(Pokemon("Onix"))
ash.catch_pokemon(Pokemon("Azumarill"))
ash.catch_pokemon(Pokemon("Eevee"))
ash.catch_pokemon(Pokemon("Primeape"))
ash.catch_pokemon(Pokemon("Phanpy"))
ash.catch_pokemon(Pokemon("Rattata"))

misty = Trainer("Misty")
misty.catch_pokemon(Pokemon("Pidgey"))
misty.catch_pokemon(Pokemon("Onix"))
misty.catch_pokemon(Pokemon("Azumarill"))
misty.catch_pokemon(Pokemon("Eevee"))
misty.catch_pokemon(Pokemon("Primeape"))
misty.catch_pokemon(Pokemon("Phanpy"))
misty.catch_pokemon(Pokemon("Rattata"))

ash.print_pokemon_stats()
misty.print_pokemon_stats()
fight(ash, misty)
