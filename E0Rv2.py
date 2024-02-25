import os, sys
os.system("git pull")
try:
    __import__("E0Rv2").menu()
except Exception as e:
    exit(str(e))
