import statistics
class statystyka():
    def __init__(self, nums):
        self.nums = nums
    def show(self):
        print(self.nums)
    def add_numbers(self):
        x = int(input("Wprowadź liczbę do tablicy: "))
        self.nums.append(x)
        self.nums.sort()
    def max(self):
        print(max(self.nums))
    def min(self):
        print(min(self.nums))
    def ave(self):
        print(statistics.mean(self.nums))
    def med(self):
        print(statistics.median(self.nums))    

    




l1 = statystyka([12, 37, 6, 9, 17])
l1.add_numbers()
l1.max()
l1.min()
l1.ave()
l1.med()
l1.show()      






