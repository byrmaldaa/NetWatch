import socket
import subprocess
import urllib.request


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "Не удалось определить локальный IP"


def get_public_ip():
    try:
        with urllib.request.urlopen("https://api.ipify.org", timeout=5) as response:
            return response.read().decode("utf-8")
    except Exception:
        return "Не удалось определить публичный IP"


def ping_host(host):
    host = host.strip()
    if not host:
        return "Введите адрес для ping"
    try:
        result = subprocess.run(
            ["ping", "-c", "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=10,
        )
        return result.stdout
    except Exception as error:
        return f"Ошибка ping: {error}"


def dns_lookup(host):
    host = host.strip()
    if not host:
        return "Введите домен"
    try:
        ip = socket.gethostbyname(host)
        return f"Домен: {host}\nIP адрес: {ip}"
    except Exception as error:
        return f"Ошибка DNS lookup: {error}"


def check_port(host, port):
    host = host.strip()
    try:
        port = int(port)
    except Exception:
        return "Порт должен быть числом"
    if not host:
        return "Введите host"
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return f"Порт {port} на {host} открыт"
        return f"Порт {port} на {host} закрыт"
    except Exception as error:
        return f"Ошибка проверки порта: {error}"
