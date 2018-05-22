import socket

class DenonAVR:

    def __init__(self,AV_IP,AV_PORT):
        self.AV_IP = AV_IP
        self.AV_PORT = AV_PORT

    def TurnOn(self):
        self.Send_Cmd("PWON")
    
    def TurnOff(self):
        self.Send_Cmd("PWSTANDBY")

    def PowerStatus(self):
        self.Send_Cmd("PW?")

    def VolumeUp(self):
        self.Send_Cmd("MVUP")

    def VolumeDown(self):
        self.Send_Cmd("MVDOWN")

    def VolumeSet(self,Amount):
        self.Send_Cmd("MV"+ str(Amount))

    def VolumeStatus(self):
        self.Send_Cmd("MV?")

    def Send_Cmd(self,cmd):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((self.AV_IP, self.AV_PORT))
        full_cmd = bytes(cmd + "\r")
        sock.sendall(full_cmd)
        self.Receive_Data(sock)

    def Receive_Data(self,sock):
        data = sock.recv(4096)
        print ("received message:", data)
        sock.close()




