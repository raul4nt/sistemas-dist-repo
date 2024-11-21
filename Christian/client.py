import socket
import datetime
import random

# IP do servidor (pode ser localhost)
server_ip = '127.0.0.1'
server_port = 6667

# Nome e endereço IP do cliente
client_name = 'Cliente001'
client_ip = socket.gethostbyname(socket.gethostname())

# Cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor no IP e porta especificados
server_address = (server_ip, server_port)
client_socket.connect(server_address)

# Envia o nome e o endereço IP do cliente para o servidor
client_data = f"{client_name},{client_ip}"
client_socket.sendall(client_data.encode())

# Recebe a hora do servidor
server_time = client_socket.recv(1024).decode()

# Gera uma hora aleatória no cliente
random_time = datetime.datetime.now() - datetime.timedelta(seconds=random.randint(1, 3600))

# Exibe a hora aleatória do cliente
print(f"Hora do cliente: {random_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Exibe a mensagem de conexão estabelecida
print("Conexão estabelecida com o servidor")

# Exibe a nova hora vinda do servidor
print(f"Nova hora vinda do servidor: {server_time}")

# Fecha a conexão com o servidor
client_socket.close()
