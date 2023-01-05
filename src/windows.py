import os
import time

def log_activity():
    # Get the current time
    current_time = time.time()

    # Get the active window title
    active_window_title = get_active_window_title()

    # Write the log entry to the log file
    log_file_path = 'C:\\ulogme\\log.txt'
    with open(log_file_path, 'a') as log_file:
        log_file.write(f'{current_time},{active_window_title}\n')

def get_active_window_title():
    # Import the required module
    import pywintypes
    import win32gui

    # Get the handle of the active window
    hwnd = win32gui.GetForegroundWindow()

    # Get the length of the window title
    length = win32gui.GetWindowTextLength(hwnd)

    # Get the window title
    title = win32gui.GetWindowText(hwnd)

    return title

if __name__ == '__main__':
    # Create the log directory if it doesn't exist
    log_directory = 'C:\\ulogme'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Log activity every 60 seconds
    while True:
        log_activity()
        time.sleep(60)
