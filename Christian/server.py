import socket
import datetime

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço e a porta em que o servidor irá escutar
server_address = ('127.0.0.1', 6667)

# Faz o bind do socket com o endereço e a porta
server_socket.bind(server_address)

# Habilita o servidor para escutar conexões
server_socket.listen()

print("Aguardando conexões na porta 6667...")

while True:
    # Aceita a conexão do cliente
    client_socket, client_address = server_socket.accept()

    # Recebe o nome e o endereço IP do cliente
    client_data = client_socket.recv(1024).decode()
    client_name, client_ip = client_data.split(",")

    # Exibe mensagem de sucesso com a hora do servidor
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_socket.sendall(current_time.encode())

    # Fecha a conexão com o cliente
    client_socket.close()
