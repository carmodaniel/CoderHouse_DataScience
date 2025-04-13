# Solicita as quantidades de partidas vencidas, empatadas e perdidas ao usuário
partidas_ganhou = int(input("Digite o número de partidas vencidas: "))
empate_jogo = int(input("Digite o número de partidas empatadas: "))
partida_perdida = int(input("Digite o número de partidas perdidas: "))

# Calcula a pontuação total
pontuacao_total = (partidas_ganhou * 3) + (empate_jogo * 1) + (partida_perdida * 0)

# Calcula a média final
media_final = pontuacao_total / 20

# Exibe o resultado
print("A média final de pontos do time é: ", media_final)