import os

try:
  import denonavr
except ImportError:
  print "Trying to Install required module: requests\n"
  os.system('python -m pip install requests')
# -- above lines try to install requests module if not present
# -- if all went well, import required module again ( for global access)
import denonavr