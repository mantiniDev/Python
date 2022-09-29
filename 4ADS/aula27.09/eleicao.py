candidatos = dict()
candidatos = {'Antonio': 0,'Jose': 0, 'Maria': 0, 'Nulo': 0, 'Branco': 0}
total = 0
import os

while True:
    os.system('CLS')
    print(f'[1] Antonio\n'
          f'[2] José\n'
          f'[3] Maria\n'
          f'[4] Branco\n'
          f'[5] Nulo\n')
    print('Urna com Votos Validos = 0\n')
    
    votoValido = int(input('Qual o seu voto: \n(digite 0 para terminar)\n'))
    
    if votoValido != 0:
         total += 1
    
    if votoValido not in range(5):
        candidatos['Nulo'] += 1
    elif votoValido == 1:
        candidatos['Antonio']+= 1
    elif votoValido == 2:
        candidatos['Jose']+= 1
    elif votoValido == 3:
        candidatos['Maria']+= 1
    elif votoValido == 4:
        candidatos['Branco']+= 1 
    elif votoValido == 0:
        print('Votações encerradas!!')    
        break
os.system('CLS')
print('#'* 28)
print('#'*2,'Resultado das Eleições','#'*2 )
print('#'* 28)
print('\nContagem dos Votos Validos: ')
print(f'Candidato Antonio obteve {candidatos["Antonio"]} votos!\n'
      f'Candidato José obteve {candidatos["Jose"]} votos!\n'
      f'Candidata Maria obteve {candidatos["Maria"]} votos!\n'
      f'Votos em Branco = {candidatos["Branco"]}\n'
      f'Votos Nulos = {candidatos["Nulo"]}\n\n'
      f'Eleitores que compareceram às urnas = {total}')

if candidatos["Antonio"] == candidatos["Jose"] or candidatos["Antonio"] == candidatos["Maria"] or candidatos["Jose"] == candidatos["Maria"]:
    print('VOTAÇÃO EM SEGUNDO TURNO')
elif candidatos["Antonio"]> candidatos["Jose"] and candidatos["Antonio"] > candidatos["Maria"]:
    print('CANDIDATO ELEITO: ANTONIO!')
elif jose > candidatos["Antonio"] and candidatos["Jose"] > candidatos["Maria"]:
    print('CANDIDATO ELEITO: JOSÉ!')
elif maria > candidatos["Antonio"] and candidatos["Maria"] > candidatos["Jose"]:
    print('CANDIDATO ELEITO: MARIA!')
