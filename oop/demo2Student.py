class Student:  # 类名一般首字母大写，多个单词采用驼峰原则
    def __init__(self, name, score):  # self必须位于第一个参数
        print(id(self), name, score)
        self.name = name
        self.score = score

    def say_score(self):  # self必须位于第一个参数
        print("{0}的分数是：{1}".format(self.name, self.score))


st = Student("高琪", 18)
print(id(st))
st.say_score()