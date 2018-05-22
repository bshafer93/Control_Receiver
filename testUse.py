from Control_Receiver import DenonAVR

import time


MyAV = DenonAVR("192.168.0.57",23)
MyAV.VolumeSet(00)
time.sleep(2)
MyAV.VolumeSet(45)