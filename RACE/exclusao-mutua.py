import threading
import time
import random

# Variável compartilhada entre as threads
shared_variable = 0
lock = threading.Lock()
turn = random.choice([1, 2])

# Função que solicita e imprime o valor da variável compartilhada
def get_initial_value():
    global shared_variable
    shared_variable = int(input("Digite o valor inicial da variável compartilhada: "))
    print(f"Valor inicial da variável compartilhada: {shared_variable}\n")

# Função que simula uma seção crítica para a Thread 1
def thread1_critical_section():
    global shared_variable, turn
    with lock:
        print("Thread 1 está usando a variável compartilhada.")
        print("Thread 2 está em bloqueio na espera.")
        new_value = int(input("Thread 1 - Digite o novo valor da variável compartilhada: "))
        shared_variable = new_value
        print(f"Thread 1 definiu o novo valor da variável compartilhada: {shared_variable}\n")
        turn = 2
        print("Thread 1 liberou a variável compartilhada.\n")

# Função que simula uma seção crítica para a Thread 2
def thread2_critical_section():
    global shared_variable, turn
    while turn != 2:
        print("Thread 2 está em bloqueio na espera.")
        time.sleep(1)
    with lock:
        print("Thread 2 está usando a variável compartilhada.")
        print("Thread 1 está em bloqueio na espera.")
        new_value = int(input("Thread 2 - Digite o novo valor da variável compartilhada: "))
        shared_variable = new_value
        print(f"Thread 2 definiu o novo valor da variável compartilhada: {shared_variable}\n")
        print("Thread 2 liberou a variável compartilhada.\n")

# Função que cria e inicia as threads
def run_threads():
    get_initial_value()

    thread1 = threading.Thread(target=thread1_critical_section)
    thread2 = threading.Thread(target=thread2_critical_section)

    if turn == 1:
        thread1.start()
        thread1.join()
        thread2.start()
        thread2.join()
    else:
        thread2.start()
        thread2.join()
        thread1.start()
        thread1.join()

    print("Valor final da variável compartilhada:", shared_variable)

if __name__ == "__main__":
    run_threads()
