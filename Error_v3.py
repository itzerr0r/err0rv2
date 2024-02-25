import os, sys
os.system("git pull")
try:
    __import__("Error-v3").Error_v3()
except Exception as e:
    exit(str(e))
