current_movies1={
    'Forrest Gump':'11:00',
    'Starwars': '12:30',
    'James Bond': '15:00',
    'Indiana Jones':'17:00'
}

print("We are showing the following movies:")
for key in current_movies1:
    print(key)

movie1=input("What movie would you like the showtime for?\n")
showtime1=current_movies1.get(movie1)
if showtime1:
    print(movie1,'is playing at',showtime1)
else:
    print('This movie is not in the current list')


current_movies2={
    'Forrest Gump':['11:00','13:45', '17:00', '20:00'],
    'Starwars': ['12:30', '14:30', '16:40', '19:30', '21:30'],
    'James Bond': ['15:00', '16:40', '20:00', '22:30'],
    'Indiana Jones':['17:00', '19:45', '21:45']
}
print(current_movies2)
print('Showtime of the movie ',movie1,'\t',current_movies2[movie1])

for name,time in current_movies2.items():
    print(name, '-',time)