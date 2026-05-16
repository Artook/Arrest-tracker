#Calculate arrest by race
arrests_by_race = {
"White":1387,
"Black":423,
"Hispanic":305,
"Muslim":2,
"Asian":22,
"Other":2
}

#Calculate sum of arrests
total_arrests=sum(arrests_by_race.values())

#Calculate and total arrests and percentages
print("Arrests by Race")
print("_"*40)
print(f" {'Race':<15} {'Arrests':<10} {'Percentage':<10}")
print("_"*40)

#Print out arrest and percentage
for race,arrests in arrests_by_race.items():
	percentage=(arrests/total_arrests)*100
	print(f"{race:<15} {arrests:<10} {percentage:6.2f}%")
	
#Calculate and create table
print("_"*40)
print(f"{'Total':<15} {'total_arrests':<10} {100.00:>6.2f}%")
