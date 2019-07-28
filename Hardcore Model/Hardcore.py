import numpy as np


class Hardcore:
    """
    The hard-core model comes from statistical physics. Given a grid of size n, we are interested in the expected number
    of 1's, if the configuration is feasible, i.e. no two adjacent values are 1.
    See more at:
    http://www.mathematik.uni-ulm.de/stochastik/lehre/ss06/markov/skript_engl/node34.html
    """
    def __init__(self,k=8):
        """

        :param k: grid size
        """

        # initial configuration
        if k <1:
            raise ValueError("Grid size must be at least 1")
        self.__grid = np.zeros((k,k))
        self.__size = k

    def count_ones(self) -> int:
        return len(np.where(self.__grid==1)[0])

    def is_feasible_cell(self,i,j):
        # works only for inner cells, for simplicity reasons
        assert 0<i<self.__size-1 and 0<j<self.__size-1
        if self.__grid[i,j]==0:
            return True
        # if the value of a cell is 1, check if all neighbours are equal to 0
        return self.__grid[i,j]==1 and self.__grid[i-1,j]+self.__grid[i,j-1] +\
                                       self.__grid[i+1,j]+self.__grid[i,j+1] == 0

    def is_feasible(self) -> bool:
        # for all 1's in the grid check if no 2 neighbours are 1's
        for i in range(1,self.__size-1):
            for j in range(1,self.__size-1):
                if not self.is_feasible_cell(i,j):
                    return False
        return True

    def change(self,times=1):
        for i in range(times):
            # change configuration
            i = np.random.randint(0,self.__size)
            j = np.random.randint(0,self.__size)
            coin = np.random.randint(2)

            if coin and self.__grid[max(0,i-1),j]+\
                        self.__grid[i,max(0,j-1)]+\
                        self.__grid[min(self.__size-1,i+1),j]+\
                        self.__grid[i,min(self.__size-1,j+1)] == 0:
                self.__grid[i,j] = 1

    def tostring(self):
        return self.__grid

    @property
    def get_size(self):
        return self.__size


