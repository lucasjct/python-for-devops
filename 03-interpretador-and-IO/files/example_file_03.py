import  psutil
import time
def main():
    get_memory_info()
    
       


def get_memory_info():
    while True: 
        time.sleep(2)
        print(psutil.virtual_memory())


if __name__ == "__main__":
    main()