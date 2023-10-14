#!/usr/bin/python3

def sum_of_evennumbers():
    total = 0
    for num in range(1,10):
        if num % 2 == 0:
            total += num
            return num



    if __name__ == "__main__":
        result = sum_of_evennumbers()
        print(result)
