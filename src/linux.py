"""
To Run
nohup python ulogme.py &

To View
tail -f ~/.ulogme/screen.log
"""

import os
import time
import logging
import subprocess

log_dir = os.path.join(os.environ['HOME'], '.ulogme')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=os.path.join(log_dir, 'screen.log'),
                    filemode='a')

def log_screen_time():
    # Get the current window name
    window_name = subprocess.check_output(['xdotool', 'getwindowfocus', 'getwindowname']).strip().decode('utf-8')

    # Log the screen time
    logging.info(f'{window_name}')

if __name__ == '__main__':
    # Run the script as a daemon process
    while True:
        log_screen_time()
        time.sleep(60)
