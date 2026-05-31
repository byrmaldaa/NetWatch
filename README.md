# NetWatch

NetWatch — полезная GUI-утилита для Linux, написанная на Python.

Программа позволяет:

* узнавать локальный IP;
* узнавать публичный IP;
* выполнять ping хоста;
* проверять DNS lookup;
* проверять открытые порты;
* работать через удобный графический интерфейс.

---

# Установка

Войти в root:

```bash id="n3wd0l"
su
```

Установить зависимости:

```bash id="x3m8hn"
apt update
apt install python3 python3-tk iputils-ping git -y
```

Выйти из root:

```bash id="n80fmx"
exit
```

---

# Скачивание проекта

```bash id="3y87i6"
git clone https://github.com/byrmaldaa/NetWatch
```

Перейти в папку проекта:

```bash id="n3cvlw"
cd NetWatch
```

---

# Запуск программы

Запуск GUI:

```bash id="91b2jz"
python3 netwatch_gui.py
```

---

# Возможности программы

## Local IP

Показывает локальный IP адрес устройства.

## Public IP

Показывает внешний IP адрес.

## Ping Host

Позволяет проверить доступность сайта или IP адреса.

## DNS Lookup

Показывает DNS информацию о домене.

## Port Check

Проверяет открыт ли указанный порт.

## Exit

Кнопка выхода из программы.

---

# Структура проекта

```text id="i74x5y"
NetWatch/
├── netwatch/
├── netwatch_gui.py
├── README.md
└── tests/
```

---

# Используемые технологии

* Python 3
* Tkinter
* socket
* subprocess
* Linux network utilities

---

# Автор

Никита Лазарец 
