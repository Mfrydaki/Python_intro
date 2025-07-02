cities = [ "london" , "amsterdam", "berlin", "Athens"]

#filter city names longer than 5 characters (using filter and lamba)

long_cities = filter(lambda city: len(city) > 5, cities)

cap_lenght_cities = list(map(lambda city : city.title(), long_cities))
print(cap_lenght_cities)


#All in one
clc = list(map(lambda city : city.title(), filter(lambda city: len(city)> 5, cities)))
print(clc)

#list compr
cap_title_cities_com = [city.title() for city in cities if len(city) > 5]
print(cap_title_cities_com)

