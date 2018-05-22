from Control_Receiver import DenonAVR

import time


MyAV = DenonAVR("192.168.0.57",23)
MyAV.ChangeInputBluRay()
time.sleep(5)
MyAV.ChangeInputCBL()
time.sleep(5)
MyAV.ChangeInputGame()
MyAV.InputStatus()