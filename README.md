# NetWatch

NetWatch — простая GUI-утилита для Linux, которая помогает проверять сетевую информацию через удобный интерфейс.

## Что умеет программа

- показывает локальный IP;
- показывает публичный IP;
- выполняет ping сайта или IP;
- делает DNS lookup домена;
- проверяет открыт ли порт;
- имеет кнопку выхода из программы.

## Установка зависимостей

Сначала заходим в root:

```bash
su
```

Устанавливаем зависимости:

```bash
apt update
apt install python3 python3-tk git iputils-ping -y
```

Выходим из root:

```bash
exit
```

## Скачивание проекта

```bash
git clone https://github.com/byrmaldaa/NetWatch
```

Переходим в папку:

```bash
cd NetWatch
```

Выдаем права на запуск:

```bash
chmod +x NetWatch
```

## Запуск

```bash
./NetWatch
```

## Структура проекта

```text
NetWatch/
├── NetWatch
├── netwatch_gui.py
├── netwatch/
│   ├── core.py
│   ├── gui.py
│   └── __init__.py
├── tests/
│   └── test_core.py
└── README.md
```

## Используемые технологии

- Python 3
- Tkinter
- socket
- subprocess
- urllib
- Linux ping

## Автор

Учебный проект Linux GUI utility.
