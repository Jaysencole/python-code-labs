groceries = {'chicken': 1.59,'beef': 1.99, 'chesse': 1.00,'milk': 2.50 }


AGE = {'Dad': 36,'stepmom': 36,'Jaysen': 16}
Jaysen_age = AGE['Jaysen'] 
#print(Jaysen_age)
Dad_age = AGE ['Dad']
#print(Dad_age)
stepmom_age = AGE ['stepmom']
#print(stepmom_age)


AGE['Jaysen'] = 25
#print(AGE)


Shoes = {'jordan 13': 1,'yeezy': 8,'foamposite': 10,'Air max': 5, 'SB Dunk': 20}
Shoes['SB Dunk'] -=2
#print(Shoes)
Shoes['yeezy'] +=1
#print (Shoes)
Shoes ['SB Dunk'] +=7
#print (Shoes)
Shoes['Air max'] +=7
#print (Shoes)
Shoes['foamposite'] +=7
#print (Shoes)
Shoes['yeezy'] +=7
#print (Shoes)
Shoes['jordan 13' ] +=7
#print (Shoes)
Shoes['jordan 13'] -=3
#print (Shoes)
Shoes['yeezy'] -=3
#print (Shoes)
Shoes['foamposite'] -=3
#print (Shoes)
Shoes['Air max'] -=3
#print (Shoes)
Shoes['SB Dunk'] -=3
#print (Shoes)





AGE['Older sister'] = 20
#print(AGE)
AGE['little sister'] = 15
#print(AGE)
AGE['little brother'] = 5
#print(AGE)
del AGE['Dad']
#print (AGE)
del AGE['stepmom']
#print (AGE)

list_of_cities = ['oakland','altanta','new york city','seattle','memphis','miami','boston','LA','Denver','NO']
#print(list_of_cities)
list_of_basketball_players = ['Michael Jordan','Lebron James','Kobe bryant','shaq','bill ruessll','stephen curry','larry bird','magic johnson','allen iverson','wilt chamberlain']
#print(list_of_basketball_players)
#print (list_of_cities[3])
#print (list_of_cities[0])
#print (list_of_cities[-3])
#print (list_of_cities[0:5])
list_of_Goat = ['Michael Jordan','Lebron James','Kobe Bryant','Bill Ruessll']
#print (list_of_Goat)
list_of_cities[0] = "San Francisco"
list_of_cities[2] = "Brooklyn"
list_of_cities[5] = "Tampa"
list_of_cities[7] = "Hollywood"
#print(list_of_cities)
list_of_cities.append("oakland")
list_of_cities.extend(["new york","LA"])
list_of_cities.insert(7,"miami")
#print(list_of_cities)
del list_of_cities[3]
list_of_cities.pop(5)
list_of_cities.remove("San Francisco")
print (list_of_cities)