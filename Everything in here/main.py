import subprocess
import time
import os

def openPikminScript():
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, 'TkinterStuff.py')
    try:
        subprocess.Popen(['python', path])
    except Exception as e:
        print(f'Error: {e}')

count = 0
while count < 5000:
    time.sleep(1)
    openPikminScript()
    count += 1
