#P2 INFO - PYTHON

#CALCULO DE VELOCIDADE MEDIA

d= int(input('insira a distancia percorrida em quilometros\n'))
t= int(input('insira o tempo do percurso em horas\n'))
vm= d/t
print ('a velocidade média é', vm, 'km/h')
if vm > 80:
  print ('você está acima do limite de velocidade')
else:
  print ('velocidade no limite permitido')
