import random

class Club:
	def __init__(self, name, country, leaguePosition):
		self.name=name
		self.country=country
		self.leaguePosition=leaguePosition

qualifiedClubs = list()
groups = {'A':list(),'B':list(),'C':list(),'D':list(),'E':list(),'F':list(),'G':list(),'H':list()}

def main():
	file = open("teams.csv", "r")
	for line in file:
		l = line.rstrip("\n")
		l = l.split(",")
		#print(l)
		qualifiedClubs.append(Club(l[0],l[1],l[2]))
	allocate()

def allocate():
	leagueLeaders = list()
	otherTeams = list()
	for i in qualifiedClubs:
		if (i.leaguePosition == "1"):
			#print("Checked the league leaders")
			leagueLeaders.append(i)
		else:
			otherTeams.append(i)

	counter = 1
	while len(leagueLeaders) != 0:
		tmp = random.choice(leagueLeaders)
		# print(tmp.name)
		putGroup(tmp, counter)
		counter += 1
		i = leagueLeaders.index(tmp)
		# print("Removing %s at index %d", tmp.name, i)
		del leagueLeaders[i]
	count = 1
	while len(otherTeams) != 0:
		team = random.choice(otherTeams)
		groupID = findGroupID(count)
		#print("Random Team: ",team.name)
		key = groups.keys()
		checkCountryConflict(groupID, team)
		count += 1
		i = otherTeams.index(team)
		del otherTeams[i]

	printGroups()

def findGroupID(count):
	if count <= 3:
		return 'A'
	elif count >= 4 and count <= 6:
		return 'B'
	elif count >= 7 and count <= 9:
		return 'C'
	elif count >= 10 and count <= 12:
		return 'D'
	elif count >= 13 and count <= 15:
		return 'E'
	elif count >= 16 and count <= 18:
		return 'F'
	elif count >= 19 and count <= 21:
		return 'G'
	elif count >= 22 and count <= 24:
		return 'H'

def putGroup(team, counter):
	if counter == 1:
		groups['A'].append(team)
	elif counter == 2:
		groups['B'].append(team)
	elif counter == 3:
		groups['C'].append(team)
	elif counter == 4:
		groups['D'].append(team)
	elif counter == 5:
		groups['E'].append(team)
	elif counter == 6:
		groups['F'].append(team)
	elif counter == 7:
		groups['G'].append(team)
	elif counter == 8:
		groups['H'].append(team)

def checkCountryConflict(groupID, team):
	for i in list(groups.keys()):
		if groupID == i:
			for j in groups[i]:
				if j.country != team.country:
					groups[i].append(team)
					break
			break


def printGroups():
	for i in groups.keys():
		print("Group ",i, "\n")
		for j in groups[i]:
			print(j.name)
		print('\n')

if __name__=='__main__':
	main()