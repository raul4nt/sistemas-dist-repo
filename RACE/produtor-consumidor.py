import threading
import time
import random

BUFFER_SIZE = 10
buffer = []
lock = threading.Lock()
not_full = threading.Condition(lock)
not_empty = threading.Condition(lock)

class Producer(threading.Thread):
    def run(self):
        global buffer
        while True:
            prod = 1
            with not_full:
                while len(buffer) == BUFFER_SIZE:
                    print("Buffer cheio. Aguardando espaço...")
                    not_full.wait()
                buffer.append(prod)
                print(f'Produzido: {prod}')
                print(f'Espaço livre no buffer: {BUFFER_SIZE - len(buffer)}\n')
                not_empty.notify()
            time.sleep(random.uniform(2.5, 3.5))

class Consumer(threading.Thread):
    def run(self):
        global buffer
        while True:
            with not_empty:
                while not buffer:
                    print("Buffer vazio. Aguardando itens...")
                    not_empty.wait()
                prod = buffer.pop(0)
                cons = random.randint(1, 4)
                if cons > prod:
                    cons = prod
                print(f'Consumido: {cons}')
                print(f'Espaço livre no buffer: {BUFFER_SIZE - len(buffer)}\n')
                not_full.notify()
            time.sleep(random.uniform(1, 2))

if __name__ == '__main__':
    producer = Producer()
    consumer = Consumer()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()