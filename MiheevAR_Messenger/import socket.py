import socket
import threading

# Константы
HOST = '127.0.0.1'
PORT = 5050
BUFFER_SIZE = 1024

#Список подключенных клиентов
clients = []

 #Функция для обработки сообщений от клиента

def handle_client(client_soket, client_address):
    print (f"Новый клиент подключен: {client_address} c")
    
    
    while True:
       try:
           message = client_soket.recv(BUFFER_SIZE).decode('UTF-8')
           if not message:
               break
            print(f'Получено новое сообщение от {client_address}: {message}')
            
            #Пересылаем сообщение всем клиентам, кроме отправителя
            for client in clients:
                if client != client_soket:
                         client.sendall(message.encode( 'UTF-8'))
        except ConnectionResetError:
            break      
      # Удаляем клиента из списка
      clients.remove(client_soket)
      client_soket.close()
      print (f" Клиент {client_address} отключен")

 # Функция запуска сервера
def start_server():
    server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Сервер запущен на {HOST}: {PORT}")
    
    
    
while True:
    client_socket, client_address = server. accept()
    clients.append(client_socket)
    
# Создаем новый поток для обработки клиента
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
    
if __name__=="__main__":
    start_server()
