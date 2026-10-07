# SURVIVING CAMP

## Gabriel Amose

### Pelin tarina

Peli kertoo tarinan henkilöstä, joka kyllästyi kotona ja haluaa tehdä jotain. Siksi hän haluaa lähteä retkeilemään. Hänen tavoitteenaan on pitää hauskaa ja selviytyä.

### pelin toiminnat

Surviving camp peli on adevnture peli, missä valitset erillaisia vaihtoehtoja erillaisissa tilanteissa. Riippuu valinnasta, pääset erillaisiin loppuratkaisuihin. Tavoiteena on päästä pelistä läpi valitsemalla oikeeat vastaukset, mutta myöskin löytää kaikki loppuratkaisut.

### Kestävän kehityksen näkökulma

Surviving camp peli liittyy 15. Maanpäälinen elämä.


# Peliprojekti hakemistorakenne
```text
Ohjelman-rakenne/
|
├──main.py
├──classes/
|   ├──__init__.py
|   |   
|   ├──player.py
|   |   └──class Player
|   |       ├──name
|   |       ├──age
|   |       └──ending
|   ├──story.py
|   |    └──class Story
|   |        ├──selected_options
|   |        └──glass
|   └──endings.py
|        └──class Ending
|
├──functions/
|   ├──__init__.py
|   |   
|   ├──game.py
|   |   └──def game()
|   ├──menu.py
|   |    └──def main_menu()
|   |
├──functions/
    └──textfiles.json
```