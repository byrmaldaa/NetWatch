import tkinter as tk
from tkinter import ttk
from .core import get_local_ip, get_public_ip, ping_host, dns_lookup, check_port


BG = "#101820"
PANEL = "#1d2b34"
BTN = "#00a896"
BTN_DARK = "#028090"
TEXT_BG = "#f8f9fa"
WHITE = "#ffffff"


class NetWatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NetWatch")
        self.root.geometry("820x560")
        self.root.configure(bg=BG)

        title = tk.Label(root, text="NetWatch", bg=BG, fg=WHITE, font=("Arial", 28, "bold"))
        title.pack(pady=15)

        subtitle = tk.Label(root, text="Linux network utility", bg=BG, fg="#b8d8d8", font=("Arial", 12))
        subtitle.pack(pady=0)

        panel = tk.Frame(root, bg=PANEL)
        panel.pack(fill="x", padx=20, pady=15)

        self.host_entry = tk.Entry(panel, font=("Arial", 12))
        self.host_entry.insert(0, "google.com")
        self.host_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.port_entry = tk.Entry(panel, font=("Arial", 12), width=8)
        self.port_entry.insert(0, "80")
        self.port_entry.grid(row=0, column=1, padx=10, pady=10)

        panel.columnconfigure(0, weight=1)

        buttons = tk.Frame(root, bg=BG)
        buttons.pack(fill="x", padx=20)

        self.make_button(buttons, "Локальный IP", lambda: self.show(get_local_ip())).grid(row=0, column=0, padx=5, pady=5)
        self.make_button(buttons, "Публичный IP", lambda: self.show(get_public_ip())).grid(row=0, column=1, padx=5, pady=5)
        self.make_button(buttons, "Ping", lambda: self.show(ping_host(self.host_entry.get()))).grid(row=0, column=2, padx=5, pady=5)
        self.make_button(buttons, "DNS lookup", lambda: self.show(dns_lookup(self.host_entry.get()))).grid(row=0, column=3, padx=5, pady=5)
        self.make_button(buttons, "Проверить порт", lambda: self.show(check_port(self.host_entry.get(), self.port_entry.get()))).grid(row=0, column=4, padx=5, pady=5)
        self.make_button(buttons, "Выход", root.destroy, color="#d62828").grid(row=0, column=5, padx=5, pady=5)

        self.output = tk.Text(root, bg=TEXT_BG, fg="#111111", font=("Consolas", 11), wrap="word")
        self.output.pack(fill="both", expand=True, padx=20, pady=15)
        self.show("NetWatch запущен. Введите домен или IP и выберите действие.")

    def make_button(self, parent, text, command, color=BTN):
        return tk.Button(parent, text=text, command=command, bg=color, fg=WHITE,
                         activebackground=BTN_DARK, activeforeground=WHITE,
                         font=("Arial", 10, "bold"), relief="flat", padx=10, pady=8)

    def show(self, text):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, str(text))


def main():
    root = tk.Tk()
    NetWatchApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
