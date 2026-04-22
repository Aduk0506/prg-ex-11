class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        x = self.scores[index]

        if x >= 90:
            return "A"
        elif 90 > x >= 80:
            return "B"
        elif 80 > x >= 70:
            return "C"
        elif 70 > x >= 60:
            return "D"
        elif 60 > x >= 50:
            return "E"
        else:
            return "F"

    def find(self, score):
        results = []
        for index, i in enumerate(self.scores):

            if i == score:
                results.append(index)

        return results

    def get_sorted(self):
        x = self.scores.copy()
        for j in range(len(x)):

            for n in range(len(x) - 1):

                if x[n] > x[n + 1]:
                    x[n], x[n + 1] = x[n + 1], x[n]
        return x


if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)

    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []

    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny