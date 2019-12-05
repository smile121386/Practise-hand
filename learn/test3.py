class MyClass:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def info(self):
        print("学生：%s； 分数：%s"%(self.name, self.score))

    def get_score(self):
        return self.score

    def set_score(self, score):
        if score >= 0 and score <= 100:
            self.score = score
            return self.score
        else:
            print("请输入0-100")

my_class = MyClass('xiaomeng', 90)
my_class.info()
my_class.set_score(101)
my_class.info()