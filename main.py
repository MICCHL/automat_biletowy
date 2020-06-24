import interface
import tkinter


def main():
    try:
        root = tkinter.Tk()
        root.geometry("389x515")

        root.resizable(width=False, height=False)

        app = interface.Maschine(root)
        root.mainloop()
    except:
       print("Błąd w module main!!\nTworzenie okna głównego ")


if __name__ == "__main__":
    main()
