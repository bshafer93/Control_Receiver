import socket

class DenonAVR:
    AV_IP = "192.168.0.57"
    AV_PORT = 23

    def TurnOn(self):
        self.Send_Cmd("PWON")
    
    def TurnOff(self):
        self.Send_Cmd("PWSTANDBY")

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




