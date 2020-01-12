from random import randint
class Arrays():
    separator = ","

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_in_wiers(array):
        print(*array, sep=Arrays.separator + ' ')   
    @staticmethod
    def newsame(elements, value):
        tab = []
        for x in range(elements):
            tab.append(value)
        return tab
    @staticmethod
    def newother(elements, value1, value2):
        tab = []
        for x in range(elements):
            tab.append(randint(value1, value2))
        return tab
    @staticmethod
    def checkelements(tab, value1, value2):
        var = 0
        for x in tab:
            if x >= value1 and x <= value2:
                var += 1
        return f'Ilość wartości z przedziału <{value1},{value2}>: {var}' 
    @staticmethod
    def change_sep(newsep):
        Arrays.separator = newsep          

                        
