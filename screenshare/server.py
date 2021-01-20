from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('IP', PORT) #change IP with your IP and PORT to your port

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'STOP':
    continue

sender.stop_stream()
