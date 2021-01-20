from vidstream import StreamingServer
import threading

client = StreamingServer('IP', PORT) #change IP with your IP and port to your port
t = threading.Thread(target=client.start_server)
t.start()

while input("") != 'STOP':
    continue

client.stop_server()
