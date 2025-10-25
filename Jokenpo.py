'''Crie um programa que faça o computador jogar 'jokenpo' com você
'''

import os

def limpTela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpTela()

import random

opcoes = ["Pedra", "Papel", "Tesoura"]  

# Pontuações
player_score = 0
ia_score = 0

# Loop principal: continua até alguém chegar a 3 pontos

while player_score < 3 and ia_score < 3:
    
    # Pedir entrada do jogador e validar (com loop para entrada inválida)
    while True:       
        try:
            player_input = int(input("Escolha o seu: 1 - Pedra | 2 - Papel | 3 - Tesoura\n "))
            if 1 <= player_input <= 3:
                player = opcoes[player_input - 1]  # Mapeia para string
                break  # Sai do loop se válido
            else:
                print("Digite um número entre 1 e 3!")
        except ValueError:
            print("Digite um número válido!")
    
    # Escolha da IA
    ia = random.choice(["Pedra", "Papel", "Tesoura"])
    limpTela()  
    # Mostrar escolhas
    print(f"Você escolheu: {player}")
    print(f"IA escolheu: {ia}")
    
    # Lógica de vitória
    if player == "Pedra" and ia == "Tesoura" or player == "Tesoura" and ia == "Papel" or player == "Papel" and ia == "Pedra":
        print("Você venceu esta rodada!")
        player_score += 1  # +1 ponto (mude para +=3 se quiser)
    elif ia == "Pedra" and player == "Tesoura" or ia == "Tesoura" and player == "Papel" or ia == "Papel" and player == "Pedra":
        print("Você perdeu esta rodada!")
        ia_score += 1
    else:
        print("Empate!")
    
    # Mostrar pontuações atuais
    print(f"Pontuação: Você {player_score} x {ia_score} IA")
    print("-" * 30)  # Separador para rodadas
 

# Declarar vencedor final
if player_score == 3:
    print("Parabéns! Você venceu o jogo!")
else:
    print("A IA venceu o jogo! Tente novamente.")