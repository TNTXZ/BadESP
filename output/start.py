import socket,time,os
import threading
import winsound
path = os.getcwd()
print(path)
def music():
    winsound.PlaySound(r'audio.wav的路径',winsound.SND_FILENAME)
a = threading.Thread(target=music, name="music", args=(), kwargs={})
a.start()
time.sleep(1.5)
for i in range(1,3285):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('掌控板IP（显示在掌控板上）',掌控板端口))
    with open(str(i)+'.pbm','rb') as f:
        f.readline()
        f.readline()
        data = f.read()
    s.send(data)
    s.close()
    print('发包成功：'+str(i))
    time.sleep(1/30)
s.close()

