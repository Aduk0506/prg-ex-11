import random
import matplotlib.pyplot as plt





def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]



def selection_sort(values):
    for n in range(len(values)):
        min_index = n
        min_val = values[min_index]


        for i in range(n + 1, len(values)):
            if values[i] < min_val:
                min_index = i
                min_val = values[i]
        values[n], values[min_index] = values[min_index], values[n]


    return values

def bubble_sort(values):
    for j in range(len(values)):

        for n in range(len(values)-1):

            if values[n] > values[n+1]:
                values[n], values[n+1] = values[n+1], values[n]


        print(values)
    return values




if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)# 5 čísel v rozsahu 0–20
    print(small)
    # selection_sort(values)
    bubble_sort(values)

