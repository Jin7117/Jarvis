import platform
import psutil
import socket
from datetime import datetime
import requests


# -------------------------
# TIME FUNCTION
# -------------------------
def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


# -------------------------
# SYSTEM INFO FUNCTION
# -------------------------
def get_system_info():
    return {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }


# -------------------------
# CPU INFO FUNCTION
# -------------------------
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_cpu_info():
    return {
        "Cores (Physical)": psutil.cpu_count(logical=False),
        "Cores (Logical)": psutil.cpu_count(logical=True),
        "Frequency": psutil.cpu_freq().current if psutil.cpu_freq() else "N/A"
    }


# -------------------------
# MEMORY INFO FUNCTION
# -------------------------
def get_memory_info():
    memory = psutil.virtual_memory()
    return {
        "Total (GB)": round(memory.total / (1024 ** 3), 2),
        "Available (GB)": round(memory.available / (1024 ** 3), 2),
        "Used (GB)": round(memory.used / (1024 ** 3), 2),
        "Usage (%)": memory.percent
    }


# -------------------------
# DISK INFO FUNCTION
# -------------------------
def get_disk_info():
    disk = psutil.disk_usage('/')
    return {
        "Total (GB)": round(disk.total / (1024 ** 3), 2),
        "Used (GB)": round(disk.used / (1024 ** 3), 2),
        "Free (GB)": round(disk.free / (1024 ** 3), 2),
        "Usage (%)": disk.percent
    }


# -------------------------
# BATTERY INFO FUNCTION
# -------------------------
def get_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        return {
            "Percentage": battery.percent,
            "Charging": battery.power_plugged
        }
    return "No battery detected"


# -------------------------
# NETWORK INFO FUNCTION
# -------------------------
def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except:
        return "Unable to fetch IP"


def get_network_usage():
    net = psutil.net_io_counters()
    return {
        "Bytes Sent (MB)": round(net.bytes_sent / (1024 ** 2), 2),
        "Bytes Received (MB)": round(net.bytes_recv / (1024 ** 2), 2)
    }


# -------------------------
# RUNNING PROCESSES
# -------------------------
def get_top_processes(limit=5):
    processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        processes.append(proc.info)

    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)
    
    return processes[:limit]


# -------------------------
# UPTIME FUNCTION
# -------------------------
def get_system_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    uptime = now - boot_time
    return str(uptime).split('.')[0]


# -------------------------
# DISK PARTITIONS
# -------------------------
def get_partitions():
    partitions = psutil.disk_partitions()
    result = []

    for partition in partitions:
        result.append({
            "Device": partition.device,
            "Mountpoint": partition.mountpoint,
            "File System": partition.fstype
        })

    return result



def is_connected_to_internet(timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except:
        return False
    
def check_internet_http():
    try:
        response = requests.get("https://www.google.com", timeout=3)
        return response.status_code == 200
    except:
        return False
    
def is_online():
    if is_connected_to_internet() or check_internet_http() :
      return True
    else:
      return False