import os
import sys
import tkinter as tk


class make_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tweeter")  # Title

        self.geometry("400x300")  # 画面サイズ
        self.resizable(0, 0)  # 画面サイズを固定


def main():
    window = make_window()
    window.mainloop()


if __name__ == '__main__':
    main()
