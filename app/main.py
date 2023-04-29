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
print("************************************************************************************************************")

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

pokemon_choice = int(input(
  "You can choose your first pokemon by selecting:  1 - Pikachu | 2 - Bulbasaur | 3 - Charmander. Type the number of your choice: \n"
))

selected_pokemon = ""

if pokemon_choice == 1:
  selected_pokemon = pokemons[0]
elif pokemon_choice == 2:
  selected_pokemon = pokemons[1]
else:
  selected_pokemon = pokemons[2]

print("************************************************************************************************************")
print(f"Great! The pokemon selected was \n {selected_pokemon}")
print("************************************************************************************************************")

selected_pokemon_status = [{
  "pokemon": selected_pokemon["Name"],
  "status": {
    "agility": int(selected_pokemon["agility"]),
    "strength": int(selected_pokemon["strength"]),
    "magic": int(selected_pokemon["magic"]),
    "life": int(selected_pokemon["life"])
  }
}]

options = [0, 1, 2]
random_enemy = random.choice(options)

selected_enemy_pokemon = [{
  "pokemon": enemy_pokemons[random_enemy]["Name"],
  "status": {
    "agility": int(enemy_pokemons[random_enemy]["agility"]),
    "strength": int(enemy_pokemons[random_enemy]["strength"]),
    "magic": int(enemy_pokemons[random_enemy]["magic"]),
    "life": int(enemy_pokemons[random_enemy]["life"])
  }
}]

print(f"Your enemy will be: \n {selected_enemy_pokemon}")
print("************************************************************************************************************")

player_turn = True

while selected_pokemon_status[0]["status"]["life"] > 0 and selected_enemy_pokemon[0]["status"]["life"] > 0:
  if player_turn == True:
    print("************************************************************************************************************")

    print("It's your turn, what would you like to do?")
    choice = int(input("1 - Attack | 2 - Defend | 3 - Use Special Power"))
    
    if choice == 1:
      dice = random.randint(1, 10)
      if dice > 5:
        print("You hit the enemy!")
        selected_enemy_pokemon[0]["status"]["life"] -= selected_pokemon_status[0]["status"]["strength"]
        print(f"Enemy life: {selected_enemy_pokemon[0]['status']['life']}")
        player_turn = False
        print("************************************************************************************************************")

      else:
        print("You missed the enemy!")
        print("************************************************************************************************************")
        player_turn = False

    elif choice == 2:
      print("You are defending!")
      print(f"Your life: {selected_pokemon_status[0]['status']['life']}")
      player_turn = False
      print("************************************************************************************************************")
    elif choice == 3:
      print("You are using your special power!")
      dice = random.randint(1, 10)
      if dice > 5:
        print("You hit the enemy!")
        selected_enemy_pokemon[0]["status"]["life"] -= selected_pokemon_status[0]["status"]["magic"]
        print(f"Enemy life: {selected_enemy_pokemon[0]['status']['life']}")
        player_turn = False
        print("************************************************************************************************************")
      else:
        print("You missed the enemy!")
        print(f"Your life: {selected_pokemon_status[0]['status']['life']}")
        player_turn = False
        print("************************************************************************************************************")
    else:
      print("Invalid choice. Please choose again.")
      print("************************************************************************************************************")
  else:
    print("It's the enemy's turn!")
    enemy_choice = int(random.choice(options))
    if enemy_choice + 1 == 1:
      print("The enemy is attacking!")
      dice = random.randint(1, 10)
      if dice > 5:
        print("The enemy hit you!")
        selected_pokemon_status[0]["status"]["life"] -= selected_enemy_pokemon[0]["status"]["strength"]
        print(f"Your life: {selected_pokemon_status[0]['status']['life']}")
        player_turn = True
        print("************************************************************************************************************")
      else:
        print("The enemy missed you!")
        player_turn = True
        print("************************************************************************************************************")
    elif enemy_choice + 1 == 2: 
      print("The enemy is defending!")
      print(f"Enemy life: {selected_enemy_pokemon[0]['status']['life']}")
      player_turn = True
      print("************************************************************************************************************")
    else: 
      print("The enemy is using his special power!")
      dice = random.randint(1, 10)
      if dice > 5:
        print("The enemy hit you!")
        selected_pokemon_status[0]["status"]["life"] -= selected_enemy_pokemon[0]["status"]["magic"]
        print(f"Your life: {selected_pokemon_status[0]['status']['life']}")
        player_turn = True
        print("************************************************************************************************************")
      else:
        print("The enemy missed you!")
        print(f"Enemy life: {selected_enemy_pokemon[0]['status']['life']}")
        player_turn = True
        print("************************************************************************************************************")
      
      
if selected_pokemon_status[0]["status"]["life"] <= 0:
  print(f"{user_name}, you lost the game!")

elif selected_enemy_pokemon[0]["status"]["life"] <= 0:
  print(''' 
  
              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
          jgs  _/_______\_
              /___________\

  ''')
  print(f"{user_name}, you won the game!")  
