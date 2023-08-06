#server.py 
import sys
import threading
import socket

# Get host & port from command line arguments
# py server.py 127.0.0.1 12345
host = sys.argv[1]
port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
displayNames = []

#
def broadcast(message):
    for client in clients:
        client.send(message)

# Xử lý nhắn tin
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            msg = str(message.decode('utf-8'))
           
            # nếu user đó thoát
            if(msg.split(': ')[1] == 'exit_chat'):
                index = clients.index(client)
                clients.remove(client)
                client.close()
                displayName = displayNames[index]
                print(f'Client {displayName} disconnected.')
                broadcast(f'{displayName} đã rời khỏi cuộc trò chuyện!'.encode('utf-8'))
                displayNames.remove(displayName)
                break

            # broadcast message
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            displayName = displayNames[index]
            broadcast(f'{displayName} đã rời khỏi cuộc trò chuyện!'.encode('utf-8'))
            displayNames.remove(displayName)
            break


def listen():
    print('Server is listening on host {} and port {}.'.format(host, port))
    
    while True:
        # Listen client connections
        client, address = server.accept()
        print(f'Connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        
        displayName = client.recv(1024)
        displayNames.append(displayName)
        clients.append(client)

        # Thông báo cho server, user, và users khác
        newClientMsg = f'Client {displayName} connected.'
        print(newClientMsg.encode('utf-8'))
        broadcast(f'{displayName} đã tham gia cuộc trò chuyện!'.encode('utf-8'))
        client.send('Bạn đã tham gia cuộc trò chuyện!'.encode('utf-8'))

        # Mỗi user một thread
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    listen()