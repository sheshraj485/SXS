import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from SXS64 import login

        login()

elif bit == "32bit":

        from SXS32 import login

        login()
