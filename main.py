import socket
from rich import print

def get_open_ports():
    open_ports = []  # Lista para armazenar as portas abertas
    for port in range(1, 65536):  # Percorre todas as portas possíveis de 1 a 65535
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um socket TCP/IP
        sock.settimeout(1)  # Define um timeout de 1 segundo para a conexão
        result = sock.connect_ex(('localhost', port))  # Tenta estabelecer uma conexão com a porta
        if result == 0:  # Se a conexão for bem-sucedida, significa que a porta está aberta
            open_ports.append(port)  # Adiciona a porta à lista de portas abertas
        sock.close()  # Fecha o socket
    return open_ports  # Retorna a lista de portas abertas

open_ports = get_open_ports()  # Obtém as portas abertas
if open_ports:
    print("[bold green]Portas abertas:[/bold green]")  # Exibe cabeçalho para portas abertas se houver alguma
    for port in open_ports:  # Percorre a lista de portas abertas
        print(f"- {port}")  # Exibe cada porta aberta
else:
    print("[bold red]Nenhuma porta aberta encontrada.[/bold red]")  # Exibe mensagem se não houver portas abertas
