from Control_Receiver import DenonAVR




MyAV = DenonAVR("192.168.0.57",23)
MyAV.VolumeUp()
MyAV.VolumeDown()
MyAV.VolumeSet(15)
MyAV.VolumeStatus()