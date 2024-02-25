import os, sys
os.system("git pull")
try:
    __import__("Error-v3").b0ss()
except Exception as e:
    exit(str(e))
