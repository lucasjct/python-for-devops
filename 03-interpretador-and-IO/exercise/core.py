import psutil 


def monitoring_info():
    mem = get_mem_info()
    cpu = get_cpu_info()
    disk = get_disk_info()

    print(f"CPU: {cpu} %, MEM: {mem} %, DISK: {disk} %")

    

def get_cpu_info():
    return(psutil.cpu_percent(interval=1))


def get_mem_info():
    return(psutil.virtual_memory().percent)

def get_disk_info():
    return(psutil.disk_usage("/").percent)
