import sys
import threading
import socket

# Get host & port from command line arguments
# py client.py 127.0.0.1 12345
host = sys.argv[1]
port = int(sys.argv[2])

displayName = input('Nhập tên hiển thị: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(displayName.encode('utf-8'))
            else:
                print(message)
        except:
            client.close()
            break


def client_send():
    while True:
        user_input  = input("")
        message = f'{displayName}: {user_input}'

        if(user_input == "exit_chat"):
            # khi thoát cũng gửi một message để thông báo server   
            client.send(message.encode('utf-8'))
            print('Bạn dã rời khỏi cuộc trò chuyện!')
            client.close()
            break
        
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()