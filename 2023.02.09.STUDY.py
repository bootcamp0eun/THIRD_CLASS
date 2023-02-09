# 선형 리스트

# 리스트에 원하는 위치에 데이터 삽입하고, 데이터 삭제하는 함수 만들기


class LinearList:
    def __init__(self):
        self.real = []

    def __str__(self):
        return f"{self.real}"

    def add(self, data):
        self.real.append(None)
        self.real[len(self.real) - 1] = data

    def insert(self, index, data):
        if index < 0 or index > len(self.real):
            print("삽입 가능 범위를 벗어났습니다.")
            return
        self.real.append(None)
        for i in range(len(self.real) - 1, index, -1):
            self.real[i] = self.real[i - 1]
            self.real[i - 1] = None
        self.real[index] = data

    def delete(self, index):
        if index < 0 or index >= len(self.real):
            print("삭제 가능 범위를 벗어났습니다.")
            return
        self.real[index] = None
        for i in range(index+1, len(self.real)):
            self.real[i - 1] = self.real[i]
            self.real[i] = None
        del self.real[len(self.real) - 1]


a = LinearList()

print(a)
a.add("오리사")
a.add("둠피스트")
a.add("정커퀸")
a.add("메르시")
a.add("겐지")
print(a)
a.insert(4, "파라")
print(a)
a.insert(5, "아나")
print(a)
a.delete(1)
print(a)
