import socket

def tcp_server():
    server_ip = input("Digite o IP do servidor TCP: ")
    server_port = int(input("Digite a porta do servidor TCP: "))

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print("Servidor TCP aguardando conexão...")

    client_socket, client_address = server_socket.accept()
    print("Conexão recebida de:", client_address)

    message = client_socket.recv(1024).decode()
    print("Mensagem recebida:", message)

    response = input("Digite a resposta a ser enviada: ")
    client_socket.send(response.encode())

    client_socket.close()
    server_socket.close()

def udp_server():
    server_ip = input("Digite o IP do servidor UDP: ")
    server_port = int(input("Digite a porta do servidor UDP: "))

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    print("Servidor UDP aguardando mensagem...")

    message, client_address = server_socket.recvfrom(1024)
    print("Mensagem recebida de", client_address, ":", message.decode())

    response = input("Digite a resposta a ser enviada: ")
    server_socket.sendto(response.encode(), client_address)

    server_socket.close()

def chat_server():
    print("Servidor de chat ainda não implementado.")

def icmp_server():
    print("Servidor ICMP ainda não implementado.")

def traceroute_server():
    print("Servidor Traceroute ainda não implementado.")

def main():
    while True:
        print("\nEscolha a ação:")
        print("a) TCP")
        print("b) UDP")
        print("c) Chat")
        print("d) ICMP")
        print("e) Traceroute")
        print("x) Sair")

        choice = input("Opção: ")

        if choice == 'a':
            tcp_server()
        elif choice == 'b':
            udp_server()
        elif choice == 'c':
            chat_server()
        elif choice == 'd':
            icmp_server()
        elif choice == 'e':
            traceroute_server()
        elif choice == 'x':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
