import random

print('''

                 ."-,.__
                 `.     `.  ,
              .--'  .._,'"-' `.
             .    .'         `'
             `.   /          ,'
               `  '--.   ,-"'
                `"`   |  \
                   -. \, |
                    `--Y.'      ___.
                         \     L._, \
               _.,        `.   <  <\                _
             ,' '           `, `.   | \            ( `
          ../, `.            `  |    .\`.           \ \_
         ,' ,..  .           _.,'    ||\l            )  '".
        , ,'   \           ,'.-.`-._,'  |           .  _._`.
      ,' /      \ \        `' ' `--/   | \          / /   ..\
    .'  /        \ .         |\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \
 / .           \"`_/. `-_ \_,.  ,'    +-' `-'  _,        ..,-.    \`.
  '         .-f    ,'   `    '.       \__.---'     _   .'   '     \ \
' /          `.'    l     .' /          \..      ,_|/   `.  ,'`     L`
|'      _.-""` `.    \ _,'  `            \ `.___`.'"`-.  , |   |    | \
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
 |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'    \-.._,.'/'
          .     /        .               .       \    .''
        .`.    |         `.             /         :_,'.'
          \ `...\   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /"'          |  "'   '_
               /_|.-'\ ,".             '.'`__'-( \
                 / ,"'"\,'               `/  `-.|"


             _                              
            | |                             
 _ __   ___ | | _____ _ __ ___   ___  _ __  
| '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
| |_) | (_) |   <  __/ | | | | | (_) | | | |
| .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|
| |                                         
|_| Game created to learn Python
      ''')
print("********************************************************")

user_name = input("What's your name hunter? \n")

print(f"Welcome {user_name}")

pokemons = [{
  "Name": "Pikachu",
  "agility": 5,
  "strength": 3,
  "magic": 4,
  "life": 12
}, {
  "Name": "Bulbasaur",
  "agility": 3,
  "strength": 5,
  "magic": 4,
  "life": 16
}, {
  "Name": "Charmander",
  "agility": 4,
  "strength": 3,
  "magic": 5,
  "life": 12
}]

enemy_pokemons = [
  {
    "Name": "Rattata",
    "agility": 4,
    "strength": 2,
    "magic": 3,
    "life": 10
  },
  {
    "Name": "Zubat",
    "agility": 5,
    "strength": 2,
    "magic": 3,
    "life": 10
  },
  {
    "Name": "Mankey",
    "agility": 4,
    "strength": 4,
    "magic": 2,
    "life": 16
  },
]

pokemon_choice = input(
  "You can choose your first pokemon by selecting:  1 - Pikachu | 2 - Bulbasaur | 3 - Charmander. Type the number of your choice: \n"
)

selected_pokemon = ""

if pokemon_choice == 1:
  selected_pokemon = pokemons[0]
elif pokemon_choice == 2:
  selected_pokemon = pokemons[1]
else:
  selected_pokemon = pokemons[2]

print("************************************")
print(f"Great! The pokemon selected was \n {selected_pokemon}")
print("************************************")

selected_pokemon_status = [{
  "pokemon": selected_pokemon["Name"],
  "status": {
    "agility": selected_pokemon["agility"],
    "strength": selected_pokemon["strength"],
    "magic": selected_pokemon["magic"],
    "life": selected_pokemon["life"]
  }
}]

options = [0, 1, 2]
random_enemy = random.choice(options)

selected_enemy_pokemon = [{
  "pokemon": enemy_pokemons[random_enemy]["Name"],
  "status": {
    "agility": enemy_pokemons[random_enemy]["agility"],
    "strength": enemy_pokemons[random_enemy]["strength"],
    "magic": enemy_pokemons[random_enemy]["magic"],
    "life": enemy_pokemons[random_enemy]["life"]
  }
}]

print("************************************")

print(f"Your enemy will be: \n {selected_enemy_pokemon}")
print("************************************")
