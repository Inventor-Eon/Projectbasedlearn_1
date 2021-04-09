weight=int(input())
unit=(input())
if unit.upper=="l":
	converted=weight*0.45
	print(converted)
else:
	converted=(weight//0.45)
	print(converted)