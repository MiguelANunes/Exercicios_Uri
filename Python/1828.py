# Uri 1828
def Won(sel_sheldon, sel_raj):
	vitoria = {'papel':['pedra','Spock'], 'pedra':['tesoura','lagarto'], 'tesoura':['papel','lagarto'], 'lagarto':['papel','Spock'],'Spock':['pedra','tesoura']}
	if sel_raj in vitoria[sel_sheldon]:
		return True
	else:
		return False

def Draw(sel_sheldon, sel_raj):
	if sel_sheldon == sel_raj:
		return True
	else:
		return False


casos = int(input())

for i in range(casos):

	sheldon, raj = input().split()

	if Won(sheldon,raj):
		print("Caso #{}: Bazinga!".format(i+1))
	elif Draw(sheldon,raj):
		print("Caso #{}: De novo!".format(i+1))
	else :
		print("Caso #{}: Raj trapaceou!".format(i+1))
