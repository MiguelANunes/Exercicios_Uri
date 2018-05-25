diaUmDia = input().split(" ")
diaUmHorario = input().split(" : ") # Isso foi muito esperto
diaDoisDia = input().split(" ")		# Não tinha pensado em splitar nos espaços e :
diaDoisHorario = input().split(" : ")

(dias, horas, minutos, segundos) = 0

tempoTotal =  (int(diaDoisDia[1])*86400)
tempoTotal += (int(diaDoisHorario[0])*3600)
tempoTotal += (int(diaDoisHorario[1])*60)
tempoTotal += (int(diaDoisHorario[2]))
tempoTotal -= (int(diaUmDia[1])*86400)
tempoTotal -= (int(diaUmHorario[0])*3600)
tempoTotal -= (int(diaUmHorario[1])*60)
tempoTotal -= (int(diaUmHorario[2]))

while(tempoTotal >= 86400):
  dias += 1
  tempoTotal -= 86400

while(tempoTotal >= 3600):
  horas += 1
  tempoTotal -= 3600

while(tempoTotal >= 60):
  minutos += 1
  tempoTotal -= 60

print("{:d} dia(s)\n{:d} hora(s)\n{:d} minuto(s)\n{:d} segundo(s)".format(dias, horas, minutos, tempoTotal))
