from random import randint
class Matrix():

    @staticmethod
    def create(x,y):
        matrix = [[0 for col in range(y)] for row in range(x)]
        return matrix

    @staticmethod
    def create_unit(x):
        matrix = Matrix.create(x, x)
        return matrix


    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
    @staticmethod
    def fill_random(matrix, m, n):
        for w in range(len(matrix)):
            for k in range(len(matrix[w])):
                r = randint(m, n)
                matrix[w][k] = r
        return matrix  
    @staticmethod
    def transposite(matrix):
        temp = [[0 for col in range(len(matrix))] for row in range(len(matrix[0]))]
        for w in range(len(matrix)):
            for k in range(len(matrix[w])):
                temp[k][w] = matrix[w][k]
        return temp    

        


m = Matrix.create_unit(4)
Matrix.print(m)
print()
Matrix.fill_random(m, 5, 9)
Matrix.print(m)
print(m[2][2])
print()

m = Matrix.transposite(m)
Matrix.print(m)

