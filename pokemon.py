class Pokemon:
   def __init__(self, name, level, type, max_health, health):
     self.name = name
     self.type = type
     self.level = level
     self.max_health = max_health
     self.health = health
     if health > 0:
       self.is_knock_out = True
     else:
       self.is_knock_out = False
    
   def __repr__(self):
     return "Name: {}\nLevel: {}\nType: {}\nHealth: {}".format(self.name,self.level,self.type,self.health)
            
   def lose_health(self, lost_health):
     self.health -= lost_health
     print(f'{self.name} lost {lost_health} health')
     if self.health <= 0:
       self.knock_out()
     
   def gain_health(self, gained_health):
     self.health += gained_health
     print(f'{self.name} gained {gained_health} health')
     self.is_knock_out = False
     
   def knock_out(self):
     print(f"{self.name} is \"knock out\"")
     self.is_knock_out = True
     
   def attack(self, op_pokemon):
     print(f'{self.name} is attacking {op_pokemon.name}')
     if self.type == "Fire":
       if op_pokemon.type == "Fire":
         op_pokemon.lose_health(self.level)
       if op_pokemon.type == "Water":
         print('It\'s not very effective')
         op_pokemon.lose_health(self.level/2)
       if op_pokemon.type == "Grass":
         print('It\'s super effective!')
         op_pokemon.lose_health(self.level*2)
     elif self.type == "Water":
       if op_pokemon.type == "Water":
         op_pokemon.lose_health(self.level)
       if op_pokemon.type == "Grass":
         print('It\'s not very effective')
         op_pokemon.lose_health(self.level/2)
       if op_pokemon.type == "Fire":
         print('It\'s super effective!')
         op_pokemon.lose_health(self.level*2)
     elif self.type == "Grass":
       if op_pokemon.type == "Grass":
         op_pokemon.lose_health(self.level)
       if op_pokemon.type == "Fire":
         print('It\'s not very effective')
         op_pokemon.lose_health(self.level/2)
       if op_pokemon.type == "Water":
         print('It\'s super effective!')
         op_pokemon.lose_health(self.level*2)
       
       
class Trainer:
   def __init__(self, name, potions, pokemons, cap_nummer): #cap_nummer is "currently actived Pokemon"
     self.name = name
     self.potions = potions
     self.pokemons = pokemons
     self.cap_nummer = cap_nummer
     self.ac_pokemon = pokemons[cap_nummer]
     
   def use_potion(self):
     print(f"{self.name} use potion on {self.ac_pokemon.name}")
     self.ac_pokemon.gain_health(50)
     self.potions -= 1
     
   def battle(self,op):
     print(f"{self.name} attack {op.name} with {self.ac_pokemon.name}")
     self.ac_pokemon.attack(op.ac_pokemon)
     
   def switch_pokemon(self,switched_pokemon):
     if self.pokemons[switched_pokemon].is_knock_out == True:
       print(f"{self.ac_pokemon.name} is \"knock out\"")
     else:
       print(f"Good work {self.ac_pokemon.name}! Go {self.pokemons[switch_pokemon].name}!")
       self.cap_nummer = switched_pokemon 
   
   def status(self):
     print("Name: {}\nPotions: {}.\nPokemon:".format(self.name, self.potions))
     for i in range(3):
       print(self.pokemons[i].name)
     print(f"Active Pokemon: {self.ac_pokemon.name}")
      
     
     
a = Pokemon("A", 100, "Water", 350, 350)
b = Pokemon("B", 100, "Fire", 350, 350)
c = Pokemon("C", 100, "Grass", 350, 350)
d = Pokemon("D", 100, "Water", 350, 350)
e = Pokemon("E", 100, "Fire", 350, 350)
f = Pokemon("F", 100, "Grass", 350, 350)

     
red = Trainer("Red", 5, [a, b, c], 1)
blue = Trainer("Blue", 5, [d, e, f], 2)


red.status()
blue.status()

red.battle(blue)
blue.use_potion()
red.battle(blue)
blue.switch_pokemon(0)
blue.battle(red)
blue.battle(red)

for i in range(3):
  print(red.pokemons[i])
for i in range(3):
  print(blue.pokemons[i])

     
     
  