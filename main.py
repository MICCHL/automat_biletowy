import tkinter

import interface


def main():
    try:
        root = tkinter.Tk()
        root.geometry("389x515")

        root.resizable(width=False, height=False)

        interface.Machine(root)
        root.mainloop()
    except Exception:
        print("Błąd w module main!!\nTworzenie okna głównego ")


if __name__ == "__main__":
    main()
