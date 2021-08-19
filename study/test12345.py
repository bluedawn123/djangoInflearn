class father():  # 부모 클래스
    def __init__(self, who):
        self.who = who

    def handsome(self):
        print("{}를 닮아 잘생겼다".format(self.who))


class sister(father):  # 자식클래스(부모클래스) 아빠매소드를 상속받겠다
    def __init__(self, who, what):
        super().__init__(who)
        self.what = what

    def choice(self):
        print("{} 말이야".format(self.what))

    def handsome(self):
        super().handsome()
        self.choice()



girl = sister("아빠", "얼굴")
girl.handsome()

