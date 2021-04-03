
def MyFunction():
    return

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__scores = []

    def Age(self):
        return self.__age

    def Name(self):
        return self.__name

    def GiveScore(self, score):
        self.__scores.append(score)
        return

    def Scores(self):
        return self.__scores

    def Category(self):
        result = "Отличник"
        minimal = 5
        for score in self.__scores:
            if score == 4 and minimal >= 4:
                result = "уд"
                minimal = 4
            if score == 3 and minimal >= 3:
                result = "тр"
                minimal = 3
            if score == 2 and minimal >= 2:
                result = "дв"
                minimal = 2
        return result


# Program:
st1 = Student("Aibek", 12)
st2 = Student("Chinara", 13)
st3 = Student("Ivan", 12)

st1.GiveScore(5)
st1.GiveScore(5)
st1.GiveScore(4)
st1.GiveScore(4)
st1.GiveScore(3)

st2.GiveScore(4)
st2.GiveScore(4)
st2.GiveScore(4)
st2.GiveScore(5)
st2.GiveScore(5)
st2.GiveScore(4)
st2.GiveScore(4)
st2.GiveScore(4)

st3.GiveScore(5)
st3.GiveScore(5)
st3.GiveScore(5)
st3.GiveScore(5)
st3.GiveScore(4)
st3.GiveScore(5)
st3.GiveScore(5)
st3.GiveScore(3)
st3.GiveScore(5)
st3.GiveScore(2)
st3.GiveScore(5)

print("Ученик: " + st1.Name())
print("Возраст: " + str(st1.Age()))
print("Оценки: " + st1.Category())
print("===================")
print("Ученик: " + st2.Name())
print("Возраст: " + str(st2.Age()))
print("Оценки: " + st2.Category())
print("===================")
print("Ученик: " + st3.Name())
print("Возраст: " + str(st3.Age()))
print("Оценки: " + st3.Category())
print("===================")
