from interface import *
class Throwing_coins(Frame):
    def __init__(self, master):
        self.__coins = 0.0
        super(Throwing_coins, self).__init__(master)
        self.grid()
        self.create_widgets(master)
        self.center()

    def create_widgets(self, X):

        leftFrame = Frame(self)
        leftFrame.pack(side=LEFT, fill=Y)
        sideFrame = Frame(self)
        sideFrame.pack(side=RIGHT, fill=Y)

        self.label = Button(leftFrame,text="Zapłać:", height=4,width=15,background="grey")
        self.label.pack(fill=Y, anchor=W)

        self.key1 = Button(leftFrame, text="0.01 zł ", height=4,width=15,background="white", command=lambda: self.thr0w(0.01, X))
        self.key1.pack(fill=Y, anchor=W)

        self.key2 = Button(leftFrame, text="0.02 zł",height=4,width=15, background="white", command=lambda: self.thr0w(0.02, X))
        self.key2.pack(fill=Y, anchor=W)

        self.key3 = Button(leftFrame, text="0.05 zł",height=4,width=15, background="white", command=lambda: self.thr0w(0.05, X))
        self.key3.pack(fill=Y, anchor=W)

        self.key4 = Button(leftFrame, text="0.1 zł  ", height=4,width=15,background="white", command=lambda: self.thr0w(0.1, X))
        self.key4.pack(fill=Y,anchor=W)

        self.key5 = Button(leftFrame, text="0.2 zł ",height=4,width=15,background="white", command=lambda: self.thr0w(0.2, X))
        self.key5.pack(fill=Y, anchor=W)

        self.key6 = Button(leftFrame, text="0.5 zł ",height=4,width=15,background="white", command=lambda: self.thr0w(0.5, X))
        self.key6.pack(fill=Y, anchor=W)

        self.key7 = Button(sideFrame, text="1.0 zł  ",height=4,width=15,background="white", command=lambda: self.thr0w(1.0, X))
        self.key7.pack(fill=Y, anchor=W)

        self.key8 = Button(sideFrame, text="2.0 zł ",height=4,width=15,background="white", command=lambda: self.thr0w(2.0, X))
        self.key8.pack(fill=Y, anchor=W)

        self.key9 = Button(sideFrame, text="5.0 zł ",height=4,width=15, background="white", command=lambda: self.thr0w(5.0, X))
        self.key9.pack(fill=Y, anchor=W)

        self.key9 = Button(sideFrame, text="10.0 zł ", height=4, width=15, background="white",command=lambda: self.thr0w(10.0, X))
        self.key9.pack(fill=Y, anchor=W)

        self.key9 = Button(sideFrame, text="20.0 zł ", height=4, width=15, background="white",command=lambda: self.thr0w(20.0, X))
        self.key9.pack(fill=Y, anchor=W)

        self.key9 = Button(sideFrame, text="50.0 zł ", height=4, width=15, background="white",command=lambda: self.thr0w(50.0, X))
        self.key9.pack(fill=Y, anchor=W)

        self.wroc = Button(sideFrame, text="Wróć",height=4,width=15,background="grey", command=lambda: self.thr0w(0.0, X))
        self.wroc.pack(fill=Y, anchor=W)

    def thr0w(self, coin, X):

        self.__coins = coin
        X.quit()
        X.destroy()

    def get_coin(self):
        return self.__coins

    def center(self):

        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))