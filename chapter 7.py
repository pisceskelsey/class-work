people = input("How many people are in your party?" )
people = int(people)
if(people > 8):
    print("There may be some delays.")
else:
    print("Your table is ready.")

number = input("Give me a number. ")
number = int(number)
if number % 10 == 0:
    print("\nThe number " + str(number) + " is a multiple of 10.")
else:
    print("\nThe number " + str(number) + " is not a multiple of 10.")
    
prompt = "\nPlease enter requested pizza toppings:"
prompt +="\n(Enter 'quit' when done.)"

while True:
    toppings = input(prompt)
    
    if toppings == 'quit':
        break
    else:
        print("We will put " + toppings.title() + " on your pizza.")
        
age = input("How old are you? ")
age = int(age)

if age >= 3:
    print("Your ticket is free!")
elseif: 
    print("Your ticket is $10.")
else:
    print("Your ticket is $12.")

message = "Please input your age."    
active == True
while active: 
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
        
x = 1
while x <= 5:
    print(x)

sandwich_orders = ['ham,' 'cheese,' 'tuna,' 'chicken']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print("I made you a " + sandwich.title() + " for lunch.")
    
while sandwich_orders:
    finished_sandwiches = sandwich_orders.pop()
    
    print("Making sandwich: " + finished_sandwiches.title())
    finished_sandwiches.append(sandwich_orders)
    
sandwich_orders = ['ham,' 'cheese,' 'pastrami,' 'tuna,' 'pastrami,' 'chicken,' 'pastrami']
        print("The deli has run out of pastrami.")
        
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
    print(sandwich_orders)
    
polling_active == True
place = input("\nWhere would you like to visit? ")
dream_vacation = input("\nIf you could only go one place, where would you go? ")

    vacations[place] == dream_vacation
    
    polling_active == False
    
print(\n--- Poll Results ---")
for place, dream_vacation in vacations.items():
    print("I would go to " + place.title() " or go to " + dream_vacation.title() + "!")
    
def make_shirt(shirt_size, shirt_message):
make_shirt('Medium,' 'I love python!')
make_shirt('Large,' 'I love python!')
make_shirt('Small,' 'Tastes like chicken!')

def describe_city(city, country):
    describe_city('Atlanta,' 'United States')
    print("I live in " + city.title() + " in " + country.title() + "!")
    describe_city('Seattle,' 'United States')
    describe_city('San Francisco,' 'United States')
    describe_city('Vancouver,' 'Canada')

def city_place(city_name, city_country):
    place = {'city': city_name, 'country': city_country}
    return place
    
    home = city_place('seattle', 'United states')
    print(home)
    
def make_album(artist_name, album_title, album_tracks)
    album = {'artist': artist_name, 'title': album_title, 'tracks': album_tracks}
    return album
    
    gorillaz = make_album('Gorillaz', 'Demon Days', '12')
    beatles = make_album('The Beatles', 'Hard Days Night', '6')
    fleetwood = make_album('Fleetwood Mac', 'Rumors', '13')
    print(gorillaz)
    print(fleetwood)
    print(beatles)

while True:
        print("\nTell me an album you like: ")
        ar_name = input("Artist Name: ")
        al_name = input("Album Name: ")
        
        if ar_name == 'q'
            break
        if al_name == 'q'
            break
            
magicians = ['David Copperfield', 'David Blane', 'Houdini']
show_magicians(magicians)
great_magicians = []
while magicians:
    make_great = magicians.pop()
    great_magicians.append(make_great)
    print(great_magicians)
    print("Presenting the Great " + great_magicians.title() + "!")
    
def make_sandwich(*toppings):
    print(toppings)
    
    make_sandwich('ham', 'turkey', 'pastrami', 'blt')
    print("\nWe are building your sandwich with:")
    for topping in toppings:
        print("- " + topping)
        