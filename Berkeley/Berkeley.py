import random

# Função para converter horário em segundos
def horario_para_segundos(horario):
    horas, minutos, segundos = map(int, horario.split(':'))
    return horas * 3600 + minutos * 60 + segundos

# Função para converter segundos em horário
def segundos_para_horario(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

# Função para gerar horários aleatórios entre 9:24:30 e 9:26:00
def gerar_horario():
    horas = random.randint(9, 9)  # Randomly selects between 9 and 9 (inclusive)
    minutos = random.randint(24, 26)  # Randomly selects between 24 and 26 (inclusive)
    segundos = random.randint(0, 30)  # Randomly selects between 0 and 30 (inclusive)
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

# Função para exibir os horários dos computadores
def exibir_horarios(computadores):
    for i, horario in enumerate(computadores):
        nome_computador = f"{i+1:02d}"  # Formata o nome do computador com dois dígitos
        print(f"Computador {nome_computador} - Horário: {horario}")

# Função para sincronização de relógios baseado no algoritmo de Berkeley
def sincronizar_relogios(computadores):
    tempos_em_segundos = [horario_para_segundos(horario) for horario in computadores]
    media = round(sum(tempos_em_segundos) / len(tempos_em_segundos))
    for i in range(len(tempos_em_segundos)):
        tempos_em_segundos[i] += media - tempos_em_segundos[i]
        computadores[i] = segundos_para_horario(tempos_em_segundos[i])
    return computadores

# Inicialização das variáveis dos 10 computadores
computadores = [gerar_horario() for _ in range(10)]

# Exibição dos horários iniciais
exibir_horarios(computadores)

# Pergunta ao usuário se deseja sincronizar os relógios
resposta = input("Deseja sincronizar os relógios? (s/n): ")

if resposta.lower() == 's':
    computadores = sincronizar_relogios(computadores)
    print("\nRelógios sincronizados:")
    exibir_horarios(computadores)
else:
    print("Programa encerrado sem sincronização de relógios.")
