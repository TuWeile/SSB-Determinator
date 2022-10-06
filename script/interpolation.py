from fixed_yields import *
import numpy as np


class InterpolatedYields(FixedBondYields):

    def __init__(self):
        self.matrix_U = np.zeros((4, 4))

        np.fill_diagonal(self.matrix_U, 2)
        self.matrix_U[1][0], self.matrix_U[2][1] = 1 / (1 + 3), 3 / (3 + 5)
        self.matrix_U[1][2], self.matrix_U[2][3] = 1 - self.matrix_U[1][0], 1 - self.matrix_U[2][1]

        self.matrix_V = np.zeros((4, 1))
        self.matrix_n = np.zeros((3, 4))
        self.matrix_B = None
        self.eer = None

    def calc_matrices(self):
        var = FixedBondYields()
        eer = var.calc_fixed_yields()
        self.eer = eer

        self.matrix_V[1] = 3 * ((((eer[4] - eer[1]) / 3) - (eer[1] - eer[0])) / 4) / 100
        self.matrix_V[2] = 3 * ((((eer[9] - eer[4]) / 5) - ((eer[4] - eer[1]) / 3)) / 8) / 100

        inv_matrix_u = np.linalg.inv(self.matrix_U)

        self.matrix_B = np.dot(inv_matrix_u, self.matrix_V)

    def spline_coefficients(self):
        for i in range(len(self.matrix_n)):
            self.matrix_n[i][0] = (self.matrix_B[i + 1] - self.matrix_B[i]) / (3 * (1 + (i * 2)))
            self.matrix_n[i][1] = self.matrix_B[i]



        return self.matrix_n


foo = InterpolatedYields()
foo.calc_matrices()
print(foo.spline_coefficients())

