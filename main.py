# This contains the logic of conducting the UCL draw.

from random import randint

class Club:
	#global name, country, leaguePosition
	def __init__(self, name, country, leaguePosition):
		self.name = name
		self.country = country
		self.leaguePosition = leaguePosition

	def getName(self):
		return self.name

	def getCountry(self):
		return self.country

	def getLeaguePosition(self):
		return self.leaguePosition

	def __str__(self):
		return self.name

qualifiedClubs = list()

groupA = list()
groupB = list()
groupC = list()
groupD = list()
groupE = list()
groupF = list()
groupG = list()
groupH = list()

def main():
	file = open("teams.csv", "r")
	for line in file:
		l = line.rstrip('\n')
		l = l.split(",")
		qualifiedClubs.append(Club(l[0],l[1],l[2]))
	allocate()

def allocate():
	leagueLeaders = list()
	otherTeams = list()
	for i in qualifiedClubs:
		if (i.getLeaguePosition() == "1\r"):
			#print("Checked the league leaders")
			leagueLeaders.append(i)
		else:
			otherTeams.append(i)
	# Allocating the league leaders

	counter = 1
	indices_done=[]
	add=0
	#print(len(leagueLeaders))
	while add != len(leagueLeaders):
		r = randint(0, len(leagueLeaders)-1)
		#print("Random %s",r)
		boole=0
		tmp=0
		while(boole==0):
			if r not in indices_done:
				tmp = leagueLeaders[r]
				indices_done.append(r)
				boole=1
			r = randint(0, len(leagueLeaders)-1)
		#print("jije",tmp.getName())
		add+=1
		if counter == 1:
			#print("Choosing the first club", tmp.getName())
			groupA.append(tmp)
			counter += 1
		elif counter == 2:
			#print("Choosing the second club", tmp.getName())
			groupB.append(tmp)
			counter += 1
		elif counter == 3:
			groupC.append(tmp)
			counter += 1
		elif counter == 4:
			groupD.append(tmp)
			counter += 1
		elif counter == 5:
			groupE.append(tmp)
			counter += 1
		elif counter == 6:
			groupF.append(tmp)
			counter += 1
		elif counter == 7:
			groupG.append(tmp)
			counter += 1
		elif counter == 8:
			groupH.append(tmp)
			counter += 1
	
	# Allocating the rest of the teams
	count = 1
	add=0
	indices_done=[]
	#print(len(otherTeams))
	#print("ur mom a ho",otherTeams)
	while add!=len(otherTeams):
		r = randint(0, len(otherTeams)-1)
		boole=0
		tmp=0
		while(boole==0):
			if r not in indices_done:
				tmp = otherTeams[r]
				indices_done.append(r)
				boole=1
			r = randint(0, len(otherTeams)-1)
		#print("thug1", tmp.getName())
		add+=1
		if count >= 1 and count <= 3 and checkCountryConflict('A',tmp) == True:
			groupA.append(tmp)
			count += 1
		elif count >= 4 and count <= 6 and checkCountryConflict('B',tmp) == True:
			groupB.append(tmp)
			count += 1
		elif count >= 7 and count <= 9 and checkCountryConflict('C',tmp) == True:
			groupC.append(tmp)
			count += 1
		elif count >= 10 and count <= 12 and checkCountryConflict('D',tmp) == True:
			groupD.append(tmp)
			count += 1
		elif count >= 13 and count <= 15 and checkCountryConflict('E',tmp) == True:
			groupE.append(tmp)
			count += 1
		elif count >= 16 and count <= 18 and checkCountryConflict('F',tmp) == True:
			groupF.append(tmp)
			count += 1
		elif count >= 19 and count <= 21 and checkCountryConflict('G',tmp) == True:
			groupG.append(tmp)
			count += 1
		elif count >= 22 and count <= 24 and checkCountryConflict('H',tmp) == True:
			groupH.append(tmp)
			count += 1
		else:
			otherTeams.append(tmp)
	printGroup()

def checkCountryConflict(groupID, team):
	if groupID == 'A':
		for i in groupA:
			if i.getCountry() == team.getCountry():
				return False
		return True
	elif groupID == 'B':
		for i in groupB:
			if i.getCountry() == team.getCountry():
				return False
		return True
	elif groupID == 'C':
		for i in groupC:
			if i.getCountry() == team.getCountry():
				return False
		return True
	elif groupID == 'D':
		for i in groupD:
			if i.getCountry() == team.getCountry():
				return False
		return True
	elif groupID == 'E':
		for i in groupE:
			if i.getCountry() == team.getCountry():
				return False
		return True
	elif groupID == 'F':
		for i in groupF:
			if i.getCountry() == team.getCountry():
				return False
		return True
	elif groupID == 'G':
		for i in groupG:
			if i.getCountry() == team.getCountry():
				return False
		return True
	elif groupID == 'H':
		for i in groupH:
			if i.getCountry() == team.getCountry():
				return False
		return True

def printGroup():
	print("Group A\n")
	for i in groupA:
		print(i.getName())
	print("\n")
	print("Group B")
	print("\n")
	for i in groupB:
		print(i.getName())
	print("\n")
	print("Group C")
	print("\n")
	for i in groupC:
		print(i.getName())
	print("\n")
	print("Group D")
	print("\n")
	for i in groupD:
		print(i.getName())
	print("\n")
	print("Group E")
	print("\n")
	for i in groupE:
		print(i.getName())
	print("\n")
	print("Group F")
	print("\n")
	for i in groupF:
		print(i.getName())
	print("\n")
	print("Group G")
	print("\n")
	for i in groupG:
		print(i.getName())
	print("\n")
	print("Group H")
	print("\n")
	for i in groupH:
		print(i.getName())
	print("\n")

if __name__ == '__main__':
	main()