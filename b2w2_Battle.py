# --------IMPORTS--------------------------------------------------------------------------------------------------------------#
from random import randint
import os
import pygame
# -----------------------------------------------------------------------------------------------------------------------------#
_ = os.system('cls')
# --------PKMN STATS-----------------------------------------------------------------------------------------------------------#
PKMN_haxorus_HP = int(randint(136, 183))
PKMN_haxorus_ATK = int(randint(136, 188))
PKMN_haxorus_DEF = int(randint(95, 136))
PKMN_haxorus_SpATK = int(randint(58, 93))
PKMN_haxorus_SpDEF = int(randint(77, 114))
PKMN_haxorus_SPD = int(randint(91, 133))
PKMN_haxorus_Lv = int(50)
PKMN_haxorus_Type = ["Dragon"]
PKMN_haxorus_Moves = ["dragon pulse", "dragon claw", "giga impact", "earthquake"]

PKMN_whiteKyurem_HP = int(randint(1085, 1132))
PKMN_whiteKyurem_ATK = int(randint(62, 99))
PKMN_whiteKyurem_DEF = int(randint(85, 156))
PKMN_whiteKyurem_SpATK = int(randint(107, 126))
PKMN_whiteKyurem_SpDEF = int(randint(94, 167))
PKMN_whiteKyurem_SPD = int(randint(90, 161))
PKMN_whiteKyurem_Lv = int(50)
PKMN_whiteKyurem_Type = ["Dragon", "Ice"]
PKMN_whiteKyurem_Moves = ["Dragon Pulse", "Fusion Flare", "Blizzard", "Ice Beam"]

PKMN_blackKyurem_HP = int(randint(1085, 1132))
PKMN_blackKyurem_ATK = int(randint(107, 126))
PKMN_blackKyurem_DEF = int(randint(94, 267))
PKMN_blackKyurem_SpATK = int(randint(62, 99))
PKMN_blackKyurem_SpDEF = int(randint(85, 156))
PKMN_blackKyurem_SPD = int(randint(90, 161))
PKMN_blackKyurem_Lv = int(50)
PKMN_blackKyurem_Type = ["Dragon", "Ice"]
PKMN_blackKyurem_Moves = ["Dragon Pulse", "Fusion Bolt", "Blizzard", "Ice Beam"]

PKMN_zebstrika_HP = int(randint(135, 182))
PKMN_zebstrika_ATK = int(randint(94, 167))
PKMN_zebstrika_DEF = int(randint(73, 136))
PKMN_zebstrika_SpATK = int(randint(76, 145))
PKMN_zebstrika_SpDEF = int(randint(71, 136))
PKMN_zebstrika_SPD = int(randint(108, 184))
PKMN_zebstrika_Lv = int(50)
PKMN_zebstrika_Type = ["Electric"]
PKMN_zebstrika_Moves = ["wild charge", "flame charge", "giga impact", "discharge"]

PKMN_lucario_HP = int(randint(130, 177))
PKMN_lucario_ATK = int(randint(103, 178))
PKMN_lucario_DEF = int(randint(77, 144))
PKMN_lucario_SpATK = int(randint(108, 183))
PKMN_lucario_SpDEF = int(randint(77, 144))
PKMN_lucario_SPD = int(randint(85, 156))
PKMN_lucario_Lv = int(50)
PKMN_lucario_Type = ["Fighting", "Steel"]
PKMN_lucario_Moves = ["dragon pulse", "aura sphere", "swords dance", "earthquake"]

PKMN_hydreigon_HP = int(randint(152, 199))
PKMN_hydreigon_ATK = int(randint(99, 172))
PKMN_hydreigon_DEF = int(randint(95, 166))
PKMN_hydreigon_SpATK = int(randint(117, 194))
PKMN_hydreigon_SpDEF = int(randint(95, 166))
PKMN_hydreigon_SPD = int(randint(92, 165))
PKMN_hydreigon_Lv = int(50)
PKMN_hydreigon_Type = ["Dark", "Dragon"]
PKMN_hydreigon_Moves = ["dragon pulse", "thunder wave", "hyper beam", "dark pulse"]

PKMN_cofagrigus_HP = int(randint(118, 165))
PKMN_cofagrigus_ATK = int(randint(49, 112))
PKMN_cofagrigus_DEF = int(randint(155, 236))
PKMN_cofagrigus_SpATK = int(randint(90, 161))
PKMN_cofagrigus_SpDEF = int(randint(119, 192))
PKMN_cofagrigus_SPD = int(randint(31, 90))
PKMN_cofagrigus_Lv = int(50)
PKMN_cofagrigus_Type = ["Ghost"]
PKMN_cofagrigus_Moves = ["shadow ball", "calm mind", "iron defense", "dark pulse"]

PKMN_krookodile_HP = int(randint(155, 202))
PKMN_krookodile_ATK = int(randint(109, 185))
PKMN_krookodile_DEF = int(randint(77, 144))
PKMN_krookodile_SpATK = int(randint(63, 128))
PKMN_krookodile_SpDEF = int(randint(77, 144))
PKMN_krookodile_SPD = int(randint(87, 158))
PKMN_krookodile_Lv = int(50)
PKMN_krookodile_Type = ["Ground", "Dark"]
PKMN_krookodile_Moves = ["crunch", "dark pulse", "giga impact", "earthquake"]

# -----------------------------------------------------------------------------------------------------------------------------#

# --------CLASSES--------------------------------------------------------------------------------------------------------------#
class Krookodile:
    def __init__(self, Name, HP, ATK, DEF, SpATK, SpDEF, SPD, Lv, Type, Moves):
        # these values set up the PKMN's stats and other required values (this is the same for all PKMN)
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SpATK = SpATK
        self.SpDEF = SpDEF
        self.SPD = SPD
        self.Lv = Lv
        self.Type = Type
        self.Moves = Moves
        self.CurrentHP = HP
        self.Move1_PP = 15
        self.Move2_PP = 15
        self.Move3_PP = 5
        self.Move4_PP = 10
        self.Status = "None"

    # The function below is to use an attacking move (it is the same for all moves with slight variation)
    def Move1(self):
        print(f'{self.Name} used {self.Moves[0]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 80
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Dark" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Ghost" in EnemyPKMN[EnemyActive].Type or "Psychic" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Fight" in EnemyPKMN[EnemyActive].Type or "Steel" in EnemyPKMN[EnemyActive].Type or "Dark" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK / EnemyPKMN[EnemyActive].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move1_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move1_PP -= 1
        if self.Move1_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move2(self):
        print(f'{self.Name} used {self.Moves[1]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 80
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Dark" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Ghost" in EnemyPKMN[EnemyActive].Type or "Psychic" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Fight" in EnemyPKMN[EnemyActive].Type or "Steel" in EnemyPKMN[EnemyActive].Type or "Dark" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / EnemyPKMN[EnemyActive].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move2_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move2_PP -= 1
        if self.Move2_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move3(self):
        global rest
        rest = "true" # makes the pkmn skip the next turn
        print(f'{self.Name} used {self.Moves[2]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 150
        Move_Accuracy = 90
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Normal" in self.Type:  # determining STAB value
            Stab = float(1.5)
            print("It's super effective!")
        elif "Fighting" in EnemyPKMN[EnemyActive].Type or "Rock" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        elif "Ghost" in EnemyPKMN[EnemyActive].Type:  # no effect
            Type = int(0)
            print("It had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK / EnemyPKMN[EnemyActive].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move3_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move3_PP -= 1
        if self.Move3_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move4(self):
        print(f'{self.Name} used {self.Moves[3]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 100
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Ground" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Fire" in EnemyPKMN[EnemyActive].Type or "Electric" in EnemyPKMN[EnemyActive].Type or "Poison" in EnemyPKMN[EnemyActive].Type or "Rock" in EnemyPKMN[EnemyActive].Type or "Steel" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Grass" in EnemyPKMN[EnemyActive].Type or "Bug" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        elif "Flying" in EnemyPKMN[EnemyActive].Type:  # no effect
            Type = int(0)
            print("It had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK / EnemyPKMN[EnemyActive].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move4_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move4_PP -= 1
        if self.Move4_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

class Lucario:
    def __init__(self, Name, HP, ATK, DEF, SpATK, SpDEF, SPD, Lv, Type, Moves):
        # these values set up the PKMN's stats and other required values (this is the same for all PKMN)
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SpATK = SpATK
        self.SpDEF = SpDEF
        self.SPD = SPD
        self.Lv = Lv
        self.Type = Type
        self.Moves = Moves
        self.CurrentHP = HP
        self.Move1_PP = 10
        self.Move2_PP = 20
        self.Move3_PP = 30
        self.Move4_PP = 10
        self.Status = "None"
        self.attackboost = 0

    # The function below is to use an attacking move (it is the same for all moves with slight variation)
    def Move1(self):
        print(f'{self.Name} used {self.Moves[0]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 90
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Dragon" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Dragon" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Steel" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / EnemyPKMN[EnemyActive].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move1_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move1_PP -= 1
        if self.Move1_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move2(self):
        print(f'{self.Name} used {self.Moves[1]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 90
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("it's a critical hit!")
        Weather = 1
        Targets = 1
        if "Fighting" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Normal" in EnemyPKMN[EnemyActive].Type or "Dark" in EnemyPKMN[EnemyActive].Type or "Ice" in EnemyPKMN[EnemyActive].Type or "Rock" in EnemyPKMN[EnemyActive].Type: # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Flying" in EnemyPKMN[EnemyActive].Type or "Poison" in EnemyPKMN[EnemyActive].Type or "Bug" in EnemyPKMN[EnemyActive].Type or "Psychic" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        elif "Ghost" in EnemyPKMN[EnemyActive].Type:
            Type = 0
            print("The move had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / EnemyPKMN[EnemyActive].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        if self.Move2_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move2_PP -= 1
        if self.Move2_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move3(self):
        print(f'{self.Name} used {self.Moves[2]}!')
        Damage = 0
        if self.Move3_PP != 0:
            if self.attackboost != 6:
                print(f"{self.Name}'s attack rose sharply!")
                self.ATK += PKMN_lucario_ATK
                self.attackboost += 2
            else:
                print(f"{self.Name}'s attack cannot go any higher")
        self.Move3_PP -= 1
        if self.Move3_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move4(self):
        print(f'{self.Name} used {self.Moves[3]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 100
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Ground" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Fire" in EnemyPKMN[EnemyActive].Type or "Electric" in EnemyPKMN[EnemyActive].Type or "Poison" in EnemyPKMN[EnemyActive].Type or "Rock" in EnemyPKMN[EnemyActive].Type or "Steel" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Grass" in EnemyPKMN[EnemyActive].Type or "Bug" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        elif "Flying" in EnemyPKMN[EnemyActive].Type:  # no effect
            Type = int(0)
            print("It had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK / EnemyPKMN[EnemyActive].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move4_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move4_PP -= 1
        if self.Move4_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

class Haxorus:
    def __init__(self, Name, HP, ATK, DEF, SpATK, SpDEF, SPD, Lv, Type, Moves):
        # these values set up the PKMN's stats and other required values (this is the same for all PKMN)
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SpATK = SpATK
        self.SpDEF = SpDEF
        self.SPD = SPD
        self.Lv = Lv
        self.Type = Type
        self.Moves = Moves
        self.CurrentHP = HP
        self.Move1_PP = 10
        self.Move2_PP = 15
        self.Move3_PP = 5
        self.Move4_PP = 10
        self.Status = "None"

    # The function below is to use an attacking move (it is the same for all moves with slight variation)
    def Move1(self):
        print(f'{self.Name} used {self.Moves[0]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 90
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Dragon" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Dragon" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Steel" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / EnemyPKMN[EnemyActive].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move1_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move1_PP -= 1
        if self.Move1_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move2(self):
        print(f'{self.Name} used {self.Moves[1]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 80
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("it's a critical hit!")
        Weather = 1
        Targets = 1
        if "Dragon" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Dragon" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Steel" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK / EnemyPKMN[EnemyActive].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move2_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move2_PP -= 1
        if self.Move2_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move3(self):
        global rest
        rest = "true" # makes the pkmn skip the next turn
        print(f'{self.Name} used {self.Moves[2]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 150
        Move_Accuracy = 90
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Normal" in self.Type:  # determining STAB value
            Stab = float(1.5)
            print("It's super effective!")
        elif "Fighting" in EnemyPKMN[EnemyActive].Type or "Rock" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        elif "Ghost" in EnemyPKMN[EnemyActive].Type:  # no effect
            Type = int(0)
            print("It had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK / EnemyPKMN[EnemyActive].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move3_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move3_PP -= 1
        if self.Move3_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move4(self):
        print(f'{self.Name} used {self.Moves[3]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 100
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Ground" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Fire" in EnemyPKMN[EnemyActive].Type or "Electric" in EnemyPKMN[EnemyActive].Type or "Poison" in EnemyPKMN[EnemyActive].Type or "Rock" in EnemyPKMN[EnemyActive].Type or "Steel" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Grass" in EnemyPKMN[EnemyActive].Type or "Bug" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        elif "Flying" in EnemyPKMN[EnemyActive].Type:  # no effect
            Type = int(0)
            print("It had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK / EnemyPKMN[EnemyActive].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move4_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move4_PP -= 1
        if self.Move4_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

class Hydreigon:
    def __init__(self, Name, HP, ATK, DEF, SpATK, SpDEF, SPD, Lv, Type, Moves):
        # these values set up the PKMN's stats and other required values (this is the same for all PKMN)
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SpATK = SpATK
        self.SpDEF = SpDEF
        self.SPD = SPD
        self.Lv = Lv
        self.Type = Type
        self.Moves = Moves
        self.CurrentHP = HP
        self.Move1_PP = 10
        self.Move2_PP = 20
        self.Move3_PP = 5
        self.Move4_PP = 15
        self.Status = "None"

    # The function below is to use an attacking move (it is the same for all moves with slight variation)
    def Move1(self):
        print(f'{self.Name} used {self.Moves[0]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 90
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Dragon" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Dragon" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Steel" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / EnemyPKMN[EnemyActive].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move1_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move1_PP -= 1
        if self.Move1_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move2(self):
        Damage = 0
        print(f'{self.Name} used {self.Moves[1]}!')
        if self.Move2_PP != 0:
            print(f"{EnemyPKMN[EnemyActive].Name} became paralysed")
            EnemyPKMN[EnemyActive].Status = "PAR"
        if self.Move2_PP <= 0:
            print("This move is out of PP")
        self.Move2_PP -= 1
        if self.Move2_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move3(self):
        global rest
        rest = "true" # makes the pkmn skip the next turn
        print(f'{self.Name} used {self.Moves[2]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 150
        Move_Accuracy = 90
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Normal" in self.Type:  # determining STAB value
            Stab = float(1.5)
            print("It's super effective!")
        elif "Fighting" in EnemyPKMN[EnemyActive].Type or "Rock" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        elif "Ghost" in EnemyPKMN[EnemyActive].Type:  # no effect
            Type = int(0)
            print("It had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / EnemyPKMN[EnemyActive].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move3_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move3_PP -= 1
        if self.Move3_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move4(self):
        print(f'{self.Name} used {self.Moves[3]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 80
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Dark" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Ghost" in EnemyPKMN[EnemyActive].Type or "Psychic" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Fight" in EnemyPKMN[EnemyActive].Type or "Steel" in EnemyPKMN[EnemyActive].Type or "Dark" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / EnemyPKMN[EnemyActive].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move4_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move4_PP -= 1
        if self.Move4_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

class Zebstrika:
    def __init__(self, Name, HP, ATK, DEF, SpATK, SpDEF, SPD, Lv, Type, Moves):
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SpATK = SpATK
        self.SpDEF = SpDEF
        self.SPD = SPD
        self.Lv = Lv
        self.Type = Type
        self.Moves = Moves
        self.CurrentHP = HP
        self.Move1_PP = 15
        self.Move2_PP = 20
        self.Move3_PP = 5
        self.Move4_PP = 80
        self.speed_scale = SPD/2 # or speed boost moves
        self.Status = "None"

    def Move1(self):
        print(f'{self.Name} used {self.Moves[0]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 90
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Electric" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Water" in EnemyPKMN[EnemyActive].Type or "Flying" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Electric" in EnemyPKMN[EnemyActive].Type or "Grass" in EnemyPKMN[EnemyActive].Type or "Dragon" in EnemyPKMN[EnemyActive].Type:
            Type = float(0.5)
            print("It's not very effective...")
        elif "Ground" in EnemyPKMN[EnemyActive].Type:
            Type = int(0)
            print("It had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK  / EnemyPKMN[EnemyActive].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move1_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move1_PP -= 1
        if self.Move1_PP == 0:
            print("This move has run out of PP")
        self.CurrentHP -= Damage/4
        print(f"{self.Name} took recoil damage")
        return Damage  # returns damage value

    def Move2(self):
        print(f'{self.Name} used {self.Moves[1]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 50
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("it's a critical hit!")
        Weather = 1
        Targets = 1
        if "Fire" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Grass" in EnemyPKMN[EnemyActive].Type or "Ice" in EnemyPKMN[EnemyActive].Type or "Bug" in EnemyPKMN[EnemyActive].Type or "Steel" in EnemyPKMN[EnemyActive]:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Fire" in EnemyPKMN[EnemyActive].Type or "Water" in EnemyPKMN[EnemyActive].Type or "Rock" in EnemyPKMN[EnemyActive].Type or "Dragon" in EnemyPKMN[EnemyActive].Type:
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK / EnemyPKMN[EnemyActive].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move2_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move2_PP -= 1
        if self.Move2_PP == 0:
            print("This move has run out of PP")
        print(f"{self.Name}'s speed rose!")
        self.SPD += self.speed_scale
        return Damage  # returns damage value

    def Move3(self):
        global rest
        rest = "true"
        print(f'{self.Name} used {self.Moves[2]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 150
        Move_Accuracy = 90
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Normal" in self.Type:  # determining STAB value
            Stab = float(1.5)
            print("It's super effective!")
        elif "Fighting" in EnemyPKMN[EnemyActive].Type or "Rock" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        elif "Ghost" in EnemyPKMN[EnemyActive].Type:  # no effect
            Type = int(0)
            print("It had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK / EnemyPKMN[EnemyActive].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move3_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move3_PP -= 1
        if self.Move3_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move4(self):
        print(f'{self.Name} used {self.Moves[3]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power =80
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Electric" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Water" in EnemyPKMN[EnemyActive].Type or "Flying" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Electric" in EnemyPKMN[EnemyActive].Type or "Grass" in EnemyPKMN[EnemyActive].Type or "Dragon" in EnemyPKMN[EnemyActive].Type:
            Type = float(0.5)
            print("It's not very effective...")
        elif "Ground" in EnemyPKMN[EnemyActive].Type:
            Type = int(0)
            print("It had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / EnemyPKMN[EnemyActive].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if AccuracyChance < AccuracyModified and self.Move4_PP != 0 and EnemyPKMN[EnemyActive].Type != "Ground":
            Paralyze_Chance = randint(1, 100)
            if Paralyze_Chance <= 30: # 30% chance of Paralysis
                EnemyPKMN[EnemyActive].Status = "PAR"
                print(f"{EnemyPKMN[EnemyActive].Name} became paralyzed!")
                EnemyPKMN[EnemyActive].SPD -= EnemyPKMN[EnemyActive].SPD*(75/100) # lowers speed to 25% (faithful to gen5 games)
        if self.Move4_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move4_PP -= 1
        if self.Move4_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

class Cofagrigus:
    def __init__(self, Name, HP, ATK, DEF, SpATK, SpDEF, SPD, Lv, Type, Moves):
        # these values set up the PKMN's stats and other required values (this is the same for all PKMN)
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SpATK = SpATK
        self.SpDEF = SpDEF
        self.SPD = SPD
        self.Lv = Lv
        self.Type = Type
        self.Moves = Moves
        self.CurrentHP = HP
        self.Move1_PP = 10
        self.Move2_PP = 20
        self.Move3_PP = 30
        self.Move4_PP = 10
        self.Status = "None"
        self.defenseboost = 0
        self.Spdefenseboost = 0

    # The function below is to use an attacking move (it is the same for all moves with slight variation)
    def Move1(self):
        print(f'{self.Name} used {self.Moves[0]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 80
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Ghost" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Ghost" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Dark" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / EnemyPKMN[EnemyActive].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move1_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move1_PP -= 1
        if self.Move1_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move2(self):
        print(f'{self.Name} used {self.Moves[1]}!')
        Damage = 0
        if self.Move2_PP != 0:
            if self.Spdefenseboost != 6:
                print(f"{self.Name}'s Sp Defense rose sharply!")
                self.SpDEF += PKMN_cofagrigus_SpDEF
                self.Spdefenseboost += 2
            else:
                print(f"{self.Name}'s Sp Defense cannot go any higher")
        self.Move2_PP -= 1
        if self.Move2_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move3(self):
        print(f'{self.Name} used {self.Moves[2]}!')
        Damage = 0
        if self.Move3_PP != 0:
            if self.defenseboost != 6:
                print(f"{self.Name}'s Defense rose sharply!")
                self.ATK += PKMN_cofagrigus_DEF
                self.defenseboost += 2
            else:
                print(f"{self.Name}'s Defense cannot go any higher")
        self.Move3_PP -= 1
        if self.Move3_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

    def Move4(self):
        print(f'{self.Name} used {self.Moves[3]}!')
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 80
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print("It's a critical hit!")
        Weather = 1
        Targets = 1
        if "Dark" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Ghost" in EnemyPKMN[EnemyActive].Type or "Psychic" in EnemyPKMN[EnemyActive].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Fight" in EnemyPKMN[EnemyActive].Type or "Steel" in EnemyPKMN[EnemyActive].Type or "Dark" in EnemyPKMN[EnemyActive].Type:  # determining if resistant
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / EnemyPKMN[EnemyActive].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move4_PP <= 0:
            Damage = 0
            print("This move is out of PP")
        self.Move4_PP -= 1
        if self.Move4_PP == 0:
            print("This move has run out of PP")
        return Damage  # returns damage value

class WhiteKyurem:
    def __init__(self, Name, HP, ATK, DEF, SpATK, SpDEF, SPD, Lv, Type, Moves):
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SpATK = SpATK
        self.SpDEF = SpDEF
        self.SPD = SPD
        self.Lv = Lv
        self.Type = Type
        self.CurrentHP = HP
        self.Moves = Moves
        self.Move1_PP = 10
        self.Move2_PP = 5
        self.Move3_PP = 5
        self.Move4_PP = 10
        self.Status = "None"

    def Move1(self):
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 85
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print(f"{EnemyPKMN[EnemyActive].Name} landed a critical hit!")
        Weather = 1
        Targets = 1
        if "Dragon" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Dragon" in PlayerPKMN[Active].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Steel" in PlayerPKMN[Active].Type:
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / PlayerPKMN[Active].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move1_PP <= 0:
            Damage = 0
        self.Move1_PP -= 1
        return Damage  # returns damage value

    def Move2(self):
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 100
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print(f"{EnemyPKMN[EnemyActive].Name} landed a critical hit!")
        Weather = 1
        Targets = 1
        if "Fire" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Grass" in PlayerPKMN[Active].Type or "Ice" in PlayerPKMN[Active].Type or "Bug" in PlayerPKMN[Active].Type or "Steel" in PlayerPKMN[Active].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Fire" in PlayerPKMN[Active].Type or "Water" in PlayerPKMN[Active].Type or "Rock" in PlayerPKMN[Active].Type or "Dragon" in PlayerPKMN[Active].Type:
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / PlayerPKMN[Active].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move2_PP <= 0:
            Damage = 0
        self.Move2_PP -= 1
        return Damage  # returns damage value

    def Move3(self):
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 110
        Move_Accuracy = 70
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print(f"{EnemyPKMN[EnemyActive].Name} landed a critical hit!")
        Weather = 1
        Targets = 1
        if "Ice" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Grass" in PlayerPKMN[Active].Type or "Ground" in PlayerPKMN[Active].Type or "Flying" in PlayerPKMN[Active].Type or "Dragon" in PlayerPKMN[Active].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Fire" in PlayerPKMN[Active].Type or "Water" in PlayerPKMN[Active].Type or "Icek" in PlayerPKMN[Active].Type or "Steel" in PlayerPKMN[Active].Type:
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / PlayerPKMN[Active].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move3_PP <= 0:
            Damage = 0
        self.Move3_PP -= 1
        return Damage  # returns damage value

    def Move4(self):
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 90
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print(f"{EnemyPKMN[EnemyActive].Name} landed a critical hit!")
        Weather = 1
        Targets = 1
        if "Ice" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Grass" in PlayerPKMN[Active].Type or "Ground" in PlayerPKMN[Active].Type or "Flying" in PlayerPKMN[Active].Type or "Dragon" in PlayerPKMN[Active].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Fire" in PlayerPKMN[Active].Type or "Water" in PlayerPKMN[Active].Type or "Icek" in PlayerPKMN[Active].Type or "Steel" in PlayerPKMN[Active].Type:
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / PlayerPKMN[Active].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move4_PP <= 0:
            Damage = 0
        self.Move4_PP -= 1
        return Damage  # returns damage value

class BlackKyurem:
    def __init__(self, Name, HP, ATK, DEF, SpATK, SpDEF, SPD, Lv, Type, Moves):
        self.Name = Name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SpATK = SpATK
        self.SpDEF = SpDEF
        self.SPD = SPD
        self.Lv = Lv
        self.Type = Type
        self.CurrentHP = HP
        self.Moves = Moves
        self.Move1_PP = 10
        self.Move2_PP = 5
        self.Move3_PP = 5
        self.Move4_PP = 10
        self.Status = "None"

    def Move1(self):
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 85
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print(f"{EnemyPKMN[EnemyActive].Name} landed a critical hit!")
        Weather = 1
        Targets = 1
        if "Dragon" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Dragon" in PlayerPKMN[Active].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Steel" in PlayerPKMN[Active].Type:
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / PlayerPKMN[Active].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move1_PP <= 0:
            Damage = 0
        self.Move1_PP -= 1
        return Damage  # returns damage value

    def Move2(self):
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 100
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print(f"{EnemyPKMN[EnemyActive].Name} landed a critical hit!")
        Weather = 1
        Targets = 1
        if "Electric" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Water" in PlayerPKMN[Active].Type or "Flying" in PlayerPKMN[Active].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Electric" in PlayerPKMN[Active].Type or "Grass" in PlayerPKMN[Active].Type or "Dragon" in PlayerPKMN[Active].Type:
            Type = float(0.5)
            print("It's not very effective...")
        elif "Ground" in PlayerPKMN[Active].Type:
            Type = int(0)
            print("It had no effect...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.ATK / PlayerPKMN[Active].DEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move2_PP <= 0:
            Damage = 0
        self.Move2_PP -= 1
        return Damage  # returns damage value

    def Move3(self):
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 110
        Move_Accuracy = 70
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print(f"{EnemyPKMN[EnemyActive].Name} landed a critical hit!")
        Weather = 1
        Targets = 1
        if "Ice" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Grass" in PlayerPKMN[Active].Type or "Ground" in PlayerPKMN[Active].Type or "Flying" in PlayerPKMN[Active].Type or "Dragon" in PlayerPKMN[Active].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Fire" in PlayerPKMN[Active].Type or "Water" in PlayerPKMN[Active].Type or "Icek" in PlayerPKMN[Active].Type or "Steel" in PlayerPKMN[Active].Type:
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / PlayerPKMN[Active].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move3_PP <= 0:
            Damage = 0
        self.Move3_PP -= 1
        return Damage  # returns damage value

    def Move4(self):
        random = float(randint(85, 100) / 100)  # random damage value
        Move_Power = 90
        Move_Accuracy = 100
        Critpossible = int(randint(1, 24))  # determines if its a crit
        Critical = 1
        Stab = 1
        Type = 1
        if Critpossible == 10:
            Critical = float(1.5)
            print(f"{EnemyPKMN[EnemyActive].Name} landed a critical hit!")
        Weather = 1
        Targets = 1
        if "Ice" in self.Type:  # determining STAB value
            Stab = float(1.5)
        if "Grass" in PlayerPKMN[Active].Type or "Ground" in PlayerPKMN[Active].Type or "Flying" in PlayerPKMN[Active].Type or "Dragon" in PlayerPKMN[Active].Type:  # determining if super effective
            Type = int(2)
            print("It's super effective!")
        elif "Fire" in PlayerPKMN[Active].Type or "Water" in PlayerPKMN[Active].Type or "Icek" in PlayerPKMN[Active].Type or "Steel" in PlayerPKMN[Active].Type:
            Type = float(0.5)
            print("It's not very effective...")
        Damage_p1 = 2 * self.Lv / 2 + 2  # start DMG formula
        Damage_p2 = Damage_p1 * Move_Power * self.SpATK / PlayerPKMN[Active].SpDEF
        Damage_p3 = Damage_p2 / 50 + 2
        Damage = int(Damage_p3 * Targets * Weather * Critical * random * Stab * Type)  # end DMG formula
        AccuracyModified = Move_Accuracy
        AccuracyChance = int(randint(1, 100))
        if AccuracyChance > AccuracyModified:  # determining accuracy
            Damage = 0
            print("The move missed")
        if self.Move4_PP <= 0:
            Damage = 0
        self.Move4_PP -= 1
        return Damage  # returns damage value
# -----------------------------------------------------------------------------------------------------------------------------#

# --------PLAYER PKMN SETUP----------------------------------------------------------------------------------------------------#
PlayerPKMN = [Haxorus("haxorus", PKMN_haxorus_HP, PKMN_haxorus_ATK, PKMN_haxorus_DEF,
                      PKMN_haxorus_SpATK, PKMN_haxorus_SpDEF,
                      PKMN_haxorus_SPD, PKMN_haxorus_Lv,
                      PKMN_haxorus_Type, PKMN_haxorus_Moves)  # Index 0   #PKMN 1
    ,
              Zebstrika("zebstrika", PKMN_zebstrika_HP, PKMN_zebstrika_ATK, PKMN_zebstrika_DEF,  # Index 1   #PKMN 2
                       PKMN_zebstrika_SpATK, PKMN_zebstrika_SpDEF,
                       PKMN_zebstrika_SPD, PKMN_zebstrika_Lv,
                       PKMN_zebstrika_Type, PKMN_zebstrika_Moves)
    ,
              Lucario("lucario", PKMN_lucario_HP, PKMN_lucario_ATK, PKMN_lucario_DEF,  # Index 2   #PKMN 3
                       PKMN_lucario_SpATK, PKMN_lucario_SpDEF,
                       PKMN_lucario_SPD, PKMN_lucario_Lv,
                       PKMN_lucario_Type, PKMN_lucario_Moves)
    ,
              Hydreigon("hydreigon", PKMN_hydreigon_HP, PKMN_hydreigon_ATK, PKMN_hydreigon_DEF,  # Index 3   #PKMN 4
                      PKMN_hydreigon_SpATK, PKMN_hydreigon_SpDEF,
                      PKMN_hydreigon_SPD, PKMN_hydreigon_Lv,
                      PKMN_hydreigon_Type, PKMN_hydreigon_Moves)
    ,
              Cofagrigus("cofagrigus", PKMN_cofagrigus_HP, PKMN_cofagrigus_ATK, PKMN_cofagrigus_DEF,  # Index 4   #PKMN 5
                      PKMN_cofagrigus_SpATK, PKMN_cofagrigus_SpDEF,
                      PKMN_cofagrigus_SPD, PKMN_cofagrigus_Lv,
                      PKMN_cofagrigus_Type, PKMN_cofagrigus_Moves)
    ,
              Krookodile("krookodile", PKMN_krookodile_HP, PKMN_krookodile_ATK, PKMN_krookodile_DEF,  # Index 5   #PKMN 6
                      PKMN_krookodile_SpATK, PKMN_krookodile_SpDEF,
                      PKMN_krookodile_SPD, PKMN_krookodile_Lv,
                      PKMN_krookodile_Type, PKMN_krookodile_Moves)
              ]

# -----------------------------------------------------------------------------------------------------------------------------#

# --------ENEMY PKMN SETUP-----------------------------------------------------------------------------------------------------#
EnemyPKMN = [WhiteKyurem("WhiteKyurem", PKMN_whiteKyurem_HP, PKMN_whiteKyurem_ATK, PKMN_whiteKyurem_DEF,
                         PKMN_whiteKyurem_SpATK, PKMN_whiteKyurem_SpDEF, PKMN_whiteKyurem_SPD,
                         PKMN_whiteKyurem_Lv, PKMN_whiteKyurem_Type, PKMN_whiteKyurem_Moves)
    ,
             BlackKyurem("BlackKyurem", PKMN_blackKyurem_HP, PKMN_blackKyurem_ATK, PKMN_blackKyurem_DEF,
                         PKMN_blackKyurem_SpATK, PKMN_blackKyurem_SpDEF, PKMN_blackKyurem_SPD,
                         PKMN_blackKyurem_Lv, PKMN_blackKyurem_Type, PKMN_blackKyurem_Moves)
             ]


# -----------------------------------------------------------------------------------------------------------------------------#


# -----------------------MAIN--------------------------------------------------------------------------------------------------#
def main():
    global Active
    global EnemyActive
    global rest
    # these few values initially set up the values.
    Active = 0
    EnemyActive = 0
    Deaths = 0
    enemydeaths = 0
    rest = "false"
    TurnNumber = 0
    moveChoice = "N/A"
    while True:  # makes it so battle continues untill a loss or win
        TurnNumber += 1
        DeathsThisTurn = 0
        print(f"#------------------------------  Turn: {TurnNumber}  ------------------------------#")
        if rest != "true":
            print(PlayerPKMN[Active].Name + "'s Health is:", PlayerPKMN[Active].CurrentHP)
            choice = input("Fight, Pokemon or Run? ").lower()
        else:
            print(f"{PlayerPKMN[Active].Name} must rest") # makes it so your turn doesn't happen
            choice = "N/A"
            moveChoice = "N/A"
            rest = "false" # unrests the PKMN

        if choice == "fight" or choice == "f":
            print("Which move?")  # Start your move
            print("Moves:")
            print(PlayerPKMN[Active].Moves)  # list of moves available
            moveChoice = input("").lower()


        elif choice == "pokemon" or choice == "pkmn" or choice == "p":
            while True:
                print("What pokemon would you like to swap to?")
                PKMNlist = []
                for i in range(len(PlayerPKMN)):
                    if PlayerPKMN[i].CurrentHP > 0:
                        PKMNlist.append(PlayerPKMN[i].Name)
                print(PKMNlist)
                PKMN_Switch = input().lower()
                for i in range(len(PlayerPKMN)):
                    if PKMN_Switch == PlayerPKMN[i].Name:  # Checks what PKMN they want
                        Active = i  # Swaps the PKMN
                if PlayerPKMN[Active].CurrentHP > 0:
                    break

        elif choice == "run" or choice == "r":
            print("You ran away")
            break

        if PlayerPKMN[Active].SPD > EnemyPKMN[EnemyActive].SPD:  # checks for PKMN with higher speed and higher speed goes first
            print("#----------  Your Turn  ----------#")
            if PlayerPKMN[Active].Status == "PAR":
                moveChance = randint(1, 4)
                if moveChance == 1:
                    moveChoice = "N/A"
                    print(f"{PlayerPKMN[Active]} is paralyzed and can't move!")
            if moveChoice == PlayerPKMN[Active].Moves[0]:
                Damage = PlayerPKMN[Active].Move1()
                EnemyPKMN[EnemyActive].CurrentHP = int(EnemyPKMN[EnemyActive].CurrentHP) - Damage  # sets new current HP
                if EnemyPKMN[EnemyActive].CurrentHP <= 0:
                    EnemyPKMN[EnemyActive].CurrentHP = 0
                print(
                    f"{EnemyPKMN[EnemyActive].Name}'s current health is: {int(EnemyPKMN[EnemyActive].CurrentHP / EnemyPKMN[EnemyActive].HP * 100)}%")  # End your move
            elif moveChoice == PlayerPKMN[Active].Moves[1]:
                Damage = PlayerPKMN[Active].Move2()
                EnemyPKMN[EnemyActive].CurrentHP = int(EnemyPKMN[EnemyActive].CurrentHP) - Damage  # sets new current HP
                if EnemyPKMN[EnemyActive].CurrentHP <= 0:
                    EnemyPKMN[EnemyActive].CurrentHP = 0
                print(
                    f"{EnemyPKMN[EnemyActive].Name}'s current health is: {int(EnemyPKMN[EnemyActive].CurrentHP / EnemyPKMN[EnemyActive].HP * 100)}%")  # End your move
            elif moveChoice == PlayerPKMN[Active].Moves[2]:
                Damage = PlayerPKMN[Active].Move3()
                EnemyPKMN[EnemyActive].CurrentHP = int(EnemyPKMN[EnemyActive].CurrentHP) - Damage  # sets new current HP
                if EnemyPKMN[EnemyActive].CurrentHP <= 0:
                    EnemyPKMN[EnemyActive].CurrentHP = 0
                print(
                    f"{EnemyPKMN[EnemyActive].Name}'s current health is: {int(EnemyPKMN[EnemyActive].CurrentHP / EnemyPKMN[EnemyActive].HP * 100)}%")  # End your move
            elif moveChoice == PlayerPKMN[Active].Moves[3]:
                Damage = PlayerPKMN[Active].Move4()
                EnemyPKMN[EnemyActive].CurrentHP = int(EnemyPKMN[EnemyActive].CurrentHP) - Damage  # sets new current HP
                if EnemyPKMN[EnemyActive].CurrentHP <= 0:
                    EnemyPKMN[EnemyActive].CurrentHP = 0
                print(
                    f"{EnemyPKMN[EnemyActive].Name}'s current health is: {int(EnemyPKMN[EnemyActive].CurrentHP / EnemyPKMN[EnemyActive].HP * 100)}%")  # End your move
        else:
            opponent_move = int(randint(1, 4))
            print("#----------  Enemy Turn  ----------#")
            if EnemyPKMN[EnemyActive].Status == "PAR":
                moveChance = randint(1, 4)
                if moveChance == 1: # 25% chance to be unnable to attack
                    opponent_move = 0
                    print(f"{EnemyPKMN[EnemyActive].Name} is paralised and can't move!")
            if opponent_move == 1:
                print(f"{EnemyPKMN[EnemyActive].Name} used {EnemyPKMN[EnemyActive].Moves[0]}")
                Damage = EnemyPKMN[EnemyActive].Move1()
                PlayerPKMN[Active].CurrentHP -= Damage  # sets new current HP
                if PlayerPKMN[Active].CurrentHP < 0:
                    PlayerPKMN[Active].CurrentHP = 0
                print(PlayerPKMN[Active].Name + "'s current health is:", PlayerPKMN[Active].CurrentHP)
            elif opponent_move == 2:
                print(f"{EnemyPKMN[EnemyActive].Name} used {EnemyPKMN[EnemyActive].Moves[1]}")
                Damage = EnemyPKMN[EnemyActive].Move2()
                PlayerPKMN[Active].CurrentHP -= Damage  # sets new current HP
                if PlayerPKMN[Active].CurrentHP < 0:
                    PlayerPKMN[Active].CurrentHP = 0
                print(PlayerPKMN[Active].Name + "'s current health is:", PlayerPKMN[Active].CurrentHP)
            elif opponent_move == 3:
                print(f"{EnemyPKMN[EnemyActive].Name} used {EnemyPKMN[EnemyActive].Moves[2]}")
                Damage = EnemyPKMN[EnemyActive].Move3()
                PlayerPKMN[Active].CurrentHP -= Damage  # sets new current HP
                if PlayerPKMN[Active].CurrentHP < 0:
                    PlayerPKMN[Active].CurrentHP = 0
                print(PlayerPKMN[Active].Name + "'s current health is:", PlayerPKMN[Active].CurrentHP)
            elif opponent_move == 4:
                print(f"{EnemyPKMN[EnemyActive].Name} used {EnemyPKMN[EnemyActive].Moves[3]}")
                Damage = EnemyPKMN[EnemyActive].Move4()
                PlayerPKMN[Active].CurrentHP -= Damage  # sets new current HP
                if PlayerPKMN[Active].CurrentHP < 0:
                    PlayerPKMN[Active].CurrentHP = 0
                print(PlayerPKMN[Active].Name + "'s current health is:",
                      PlayerPKMN[Active].CurrentHP)  # End opponent move

        if PlayerPKMN[Active].CurrentHP <= 0:
            print(PlayerPKMN[Active].Name + " has fainted")
            rest = "false"
            Deaths += 1
            DeathsThisTurn = 1
            if Deaths >= len(PlayerPKMN):
                print("You have no more Pokemon to fight with")
                print("You lose")
                break
            else:
                while PlayerPKMN[Active].CurrentHP == 0:
                    print("What pokemon would you like to swap to?")
                    PKMNlist = []
                    for i in range(len(PlayerPKMN)):
                        if PlayerPKMN[i].CurrentHP > 0:  # Only prints the PKMN with more than 0 hp
                            PKMNlist.append(PlayerPKMN[i].Name)
                    print(PKMNlist)
                    PKMN_Switch = input().lower()
                    for i in range(len(PlayerPKMN)):
                        if PKMN_Switch == PlayerPKMN[i].Name:  # Checks which PKMN they want
                            Active = i  # Swaps the PKMN
        if EnemyPKMN[EnemyActive].CurrentHP <= 0:  # "win" condition
             enemydeaths+= 1
             DeathsThisTurn = 1
             print(f"{EnemyPKMN[EnemyActive].Name} has fainted!")
             if enemydeaths >= len(EnemyPKMN):
                print("You won!")
                break
             else:
                EnemyActive += 1

        if DeathsThisTurn != 1: # makes sure PKMN hasn't died yet
            if PlayerPKMN[Active].SPD < EnemyPKMN[EnemyActive].SPD:
                print("#----------  Your Turn  ----------#")
                if PlayerPKMN[Active].Status == "PAR":
                    moveChance = randint(1, 4)
                    if moveChance == 1:
                        moveChoice = "N/A"
                        print(f"{PlayerPKMN[Active]} is paralyzed and can't move!")
                if moveChoice == PlayerPKMN[Active].Moves[0]:
                    Damage = PlayerPKMN[Active].Move1()
                    EnemyPKMN[EnemyActive].CurrentHP = int(
                        EnemyPKMN[EnemyActive].CurrentHP) - Damage  # sets new current HP
                    if EnemyPKMN[EnemyActive].CurrentHP <= 0:
                        EnemyPKMN[EnemyActive].CurrentHP = 0
                    print(
                        f"{EnemyPKMN[EnemyActive].Name}'s current health is: {int(EnemyPKMN[EnemyActive].CurrentHP / EnemyPKMN[EnemyActive].HP * 100)}%")  # End your move
                elif moveChoice == PlayerPKMN[Active].Moves[1]:
                    Damage = PlayerPKMN[Active].Move2()
                    EnemyPKMN[EnemyActive].CurrentHP = int(
                        EnemyPKMN[EnemyActive].CurrentHP) - Damage  # sets new current HP
                    if EnemyPKMN[EnemyActive].CurrentHP <= 0:
                        EnemyPKMN[EnemyActive].CurrentHP = 0
                    print(
                        f"{EnemyPKMN[EnemyActive].Name}'s current health is: {int(EnemyPKMN[EnemyActive].CurrentHP / EnemyPKMN[EnemyActive].HP * 100)}%")  # End your move
                elif moveChoice == PlayerPKMN[Active].Moves[2]:
                    Damage = PlayerPKMN[Active].Move3()
                    EnemyPKMN[EnemyActive].CurrentHP = int(
                        EnemyPKMN[EnemyActive].CurrentHP) - Damage  # sets new current HP
                    if EnemyPKMN[EnemyActive].CurrentHP <= 0:
                        EnemyPKMN[EnemyActive].CurrentHP = 0
                    print(
                        f"{EnemyPKMN[EnemyActive].Name}'s current health is: {int(EnemyPKMN[EnemyActive].CurrentHP / EnemyPKMN[EnemyActive].HP * 100)}%")  # End your move
                elif moveChoice == PlayerPKMN[Active].Moves[3]:
                    Damage = PlayerPKMN[Active].Move4()
                    EnemyPKMN[EnemyActive].CurrentHP = int(
                        EnemyPKMN[EnemyActive].CurrentHP) - Damage  # sets new current HP
                    if EnemyPKMN[EnemyActive].CurrentHP <= 0:
                        EnemyPKMN[EnemyActive].CurrentHP = 0
                    print(
                        f"{EnemyPKMN[EnemyActive].Name}'s current health is: {int(EnemyPKMN[EnemyActive].CurrentHP / EnemyPKMN[EnemyActive].HP * 100)}%")  # End your move
            else:
                opponent_move = int(randint(1, 4))  # Start opponent move
                print("#----------  Enemy Turn  ----------#")
                if EnemyPKMN[EnemyActive].Status == "PAR":
                    moveChance = randint(1, 4)
                    if moveChance == 1:
                        opponent_move = 0
                        print(f"{EnemyPKMN[EnemyActive].Name} is paralised and can't move!")
                if opponent_move == 1:
                    print(f"{EnemyPKMN[EnemyActive].Name} used {EnemyPKMN[EnemyActive].Moves[0]}")
                    Damage = EnemyPKMN[EnemyActive].Move1()
                    PlayerPKMN[Active].CurrentHP -= Damage  # sets new current HP
                    if PlayerPKMN[Active].CurrentHP < 0:
                        PlayerPKMN[Active].CurrentHP = 0
                    print(PlayerPKMN[Active].Name + "'s current health is:", PlayerPKMN[Active].CurrentHP)
                elif opponent_move == 2:
                    print(f"{EnemyPKMN[EnemyActive].Name} used {EnemyPKMN[EnemyActive].Moves[1]}")
                    Damage = EnemyPKMN[EnemyActive].Move2()
                    PlayerPKMN[Active].CurrentHP -= Damage  # sets new current HP
                    if PlayerPKMN[Active].CurrentHP < 0:
                        PlayerPKMN[Active].CurrentHP = 0
                    print(PlayerPKMN[Active].Name + "'s current health is:", PlayerPKMN[Active].CurrentHP)
                elif opponent_move == 3:
                    print(f"{EnemyPKMN[EnemyActive].Name} used {EnemyPKMN[EnemyActive].Moves[2]}")
                    Damage = EnemyPKMN[EnemyActive].Move3()
                    PlayerPKMN[Active].CurrentHP -= Damage  # sets new current HP
                    if PlayerPKMN[Active].CurrentHP < 0:
                        PlayerPKMN[Active].CurrentHP = 0
                    print(PlayerPKMN[Active].Name + "'s current health is:", PlayerPKMN[Active].CurrentHP)
                elif opponent_move == 4:
                    print(f"{EnemyPKMN[EnemyActive].Name} used {EnemyPKMN[EnemyActive].Moves[3]}")
                    Damage = EnemyPKMN[EnemyActive].Move4()
                    PlayerPKMN[Active].CurrentHP -= Damage  # sets new current HP
                    if PlayerPKMN[Active].CurrentHP < 0:
                        PlayerPKMN[Active].CurrentHP = 0
                    print(PlayerPKMN[Active].Name + "'s current health is:",
                          PlayerPKMN[Active].CurrentHP)  # End opponent move

        if PlayerPKMN[Active].CurrentHP <= 0:
            print(PlayerPKMN[Active].Name + " has fainted")
            Deaths += 1
            if Deaths >= len(PlayerPKMN):
                print("You have no more Pokemon to fight with")
                print("You lose")
                break
            else:
                while PlayerPKMN[Active].CurrentHP == 0:
                    print("What pokemon would you like to swap to?")
                    rest = "false"
                    PKMNlist = []
                    for i in range(len(PlayerPKMN)):
                        if PlayerPKMN[i].CurrentHP > 0:  # Only prints the PKMN with more than 0 hp
                            PKMNlist.append(PlayerPKMN[i].Name)
                    print(PKMNlist)
                    PKMN_Switch = input().lower()
                    for i in range(len(PlayerPKMN)):
                        if PKMN_Switch == PlayerPKMN[i].Name:  # Checks which PKMN they want
                            Active = i  # Swaps the PKMN
        if EnemyPKMN[EnemyActive].CurrentHP <= 0:  # "win" condition
            enemydeaths += 1
            print(f"{EnemyPKMN[EnemyActive].Name} has fainted!")
            if enemydeaths >= len(EnemyPKMN):
                print("You won!")
                break
            else:
                EnemyActive += 1
            # -----------------------------------------------------------------------------------------------------------------------------#


# --------------------------PROGRAM STARTUP------------------------------------------------------------------------------------#
run = input("Do you wish to start? Y/N? ").lower()
if run == "y":
    pygame.mixer.init() # initialises the music player
    pygame.mixer.music.load('b2b2_music.wav')
    pygame.mixer.music.play(loops=-1) # plays music infinitely
    main()
    pygame.mixer.music.fadeout(3000) # fades out for 3 seconds
    input("Press Enter to continue...")
    _ = os.system('cls')
os.system('Main_Program.py') # returs to main program

# -----------------------------------------------------------------------------------------------------------------------------#
