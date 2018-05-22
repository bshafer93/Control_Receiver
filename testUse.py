from Control_Receiver import DenonAVR

import time


MyAV = DenonAVR("192.168.0.57",23)
MyAV.ChangeInput("DVD")
time.sleep(5)
MyAV.ChangeInput("GAME")
