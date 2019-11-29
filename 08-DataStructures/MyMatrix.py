class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

m = matrix.create(4,3)
matrix.print(m)
