pkmn_trainer2[0].attack(pkmn_trainer1[0])
        if pkmn_trainer1[0].get_strength() <= 0:
            trainer1.release_pokemon(1)
        if pkmn_trainer1 == [] and pkmn_trainer2 == []:
            print("You cannot fight!")
            return
        elif pkmn_trainer1 == []:
            print("{0:s} has no pokemon left. {1:s} won!".format(trainer1.get_name(), trainer2.get_name()))
            return
        elif pkmn_trainer2 == []:
            print("{0:s} has no pokemon left. {1:s} won!".format(trainer2.get_name(), trainer1.get_name()))
            return