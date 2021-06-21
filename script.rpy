# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    play music "<from 5 loop 5>preambule.opus" 
    #preamble by airtone (c) copyright 2020 Licensed under a Creative Commons Attribution (3.0) license. http://dig.ccmixter.org/files/airtone/61579 

    scene bg_start

    show screen screen_map

    "Bienvenue explorateur."
    "Navigue comme tu le souhaites en cliquant sur la carte en haut à gauche."
    "Bon voyage !"

    scene bg_start

    $ renpy.pause(hard=True) # In order to not jump to the next action


label scene1:

    scene bg1 with dissolve

    show screen screen_map

    "La forêt."
    "Je n'en ai jamais vues de si belles..."
    "Je me sens comme absorbé par son étoffe verdoyante."

    scene bg1

    $ renpy.pause(hard=True) # In order to not jump to the next action


label scene2:

    scene bg2 with dissolve

    show screen screen_map

    "Des fois j'ai la sensation d'être au bord du gouffre,"
    "que je dois faire des sauts de géant pour me sortir des situations difficiles."
    "Et pourtant, quand je prends le temps d'étudier la situation,"
    "je sais que je peux le faire."

    scene bg2

    $ renpy.pause(hard=True) # In order to not jump to the next action



label scene3:

    scene bg3 with dissolve

    show screen screen_map

    "Les plaines de l'île de mon enfance."
    "J'adore venir ici, elles me rappellent ces soirées où, avec papa, nous courrions comme des fous sans se soucier de ce que le monde pouvait penser de nous."
    "Ici, nous étions seuls au monde."

    scene bg3

    $ renpy.pause(hard=True) # In order to not jump to the next action


label fin:

    return