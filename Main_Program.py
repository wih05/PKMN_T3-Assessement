#---------- IMPORTS ----------#
import os
import easygui
import pygame
#-----------------------------#
_ = os.system('cls')
#---------- MAIN ----------#
def main():
    pygame.mixer.init()
    choice = "info"
    while choice == "info":
        pygame.mixer.music.load('MainMenu_music.mp3')
        pygame.mixer.music.play(loops=-1) # plays music
        choice = easygui.choicebox("Which game would you like to play?", "Game selection", ["b2w2", "info", "quit"]) # shows a choice box with the result being sent to the choice variable.
        pygame.mixer.music.fadeout(1500)
        if choice == "b2w2":
            os.system('b2w2_Battle.py')
        elif choice == "info":
            pygame.mixer.music.load('InfoMenu_music.mp3')
            pygame.mixer.music.play(loops=-1)
            easygui.msgbox('''Essentially PKMN is a popular franchise in which you train up fictional animals known as pokemon, during your adventures in the game you get to fight many strong trainers and pokemon in order to reach the final goal. some of these challenging trainers and pokemon include "Gym Leaders", "Elite Four", "Champion", and "Legendary" Pokemon, these fights are usually quite challenging however normally can only be fought a few times.          
My goal for this program is to bring about the legendary pokemon fights from different games in a harder yet still vanilla feel.'''
, "Background Info", "NEXT")
            easygui.msgbox('''To start off with in the battle you have 3 options to do:
Fight:
    You can attack the opponent's pokemon using moves that your pokemon know
Pokemon:
    You can switch out your active pokemon, however this will leave the pokemon being switched in vulnrable to attack.
Run:
    You can run from the battle.
            
The order of a turn is as follows:
1. chose what to do.
2. if chosen, run or switch out your pokemon
3. the pokemon with the highest speed attacks first
4. if no pokemon died the pokemon with the slowest speed attacks'''
, "Instructions", "NEXT")
            easygui.msgbox("Program Created by William Hannah\nMusic taken from the pokemon franchise\nGame base and pokemon credit to the Pokemon company", "Credits", "END")
            pygame.mixer.music.fadeout(1500)
        elif choice == "quit":
            input("Press Enter to quit...")
#--------------------------#

#---------- PROGRAM ----------#
main()
#-----------------------------#
