import psutil
import os
import sys
import select

print("Press 'q' to quit\n")

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    os.system('clear')

    print("--- SYSTEM MONITOR ---")
    print(f"CPU: {cpu}%")
    print(f"RAM: {memory.percent}%")
    print(f"DISK: {disk.percent}%")

    print("\nPress 'q' to quit")

    # Check if key is pressed
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        key = sys.stdin.read(1)
        if key == 'q':
            print("Exiting... 👋")
            break