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
        self.eer = FixedBondYields.calc_fixed_yields()

    def calc_matrices(self):
        self.matrix_V[1] = 3 * ((((self.eer[4] - self.eer[1]) / 3) - (self.eer[1] - self.eer[0])) / 4) / 100
        self.matrix_V[2] = 3 * ((((self.eer[9] - self.eer[4]) / 5) - ((self.eer[4] - self.eer[1]) / 3)) / 8) / 100

        inv_matrix_u = np.linalg.inv(self.matrix_U)
        self.matrix_B = np.dot(inv_matrix_u, self.matrix_V)

    def spline_coefficients(self):
        self.calc_matrices()

        b_eer = list(filter(lambda x: x != 0, self.eer))

        for i in range(len(self.matrix_n)):
            odd_numbers = 1 + (i * 2)

            self.matrix_n[i][0] = (self.matrix_B[i + 1] - self.matrix_B[i]) / (3 * odd_numbers)
            self.matrix_n[i][1] = self.matrix_B[i]
            self.matrix_n[i][2] = ((b_eer[i + 1] - b_eer[i]) / 100) / odd_numbers - (odd_numbers / 3) * \
                                  (self.matrix_B[i + 1] + 2 * self.matrix_B[i])
            self.matrix_n[i][3] = b_eer[i] / 100

    def calc_all_yields(self):
        self.spline_coefficients()

        for i, j in enumerate(FixedBondYields.calc_fixed_yields()):
            if j == 0:
                if i <= 4:
                    self.eer[i] = (self.matrix_n[1][0] * ((i + 1) - 2) ** 3 +
                                   self.matrix_n[1][1] * ((i + 1) - 2) ** 2 +
                                   self.matrix_n[1][2] * ((i + 1) - 2) ** 1 +
                                   self.matrix_n[1][3]) * 100
                else:
                    self.eer[i] = (self.matrix_n[2][0] * ((i + 1) - 5) ** 3 +
                                   self.matrix_n[2][1] * ((i + 1) - 5) ** 2 +
                                   self.matrix_n[2][2] * ((i + 1) - 5) ** 1 +
                                   self.matrix_n[2][3]) * 100

        return self.eer

foo = InterpolatedYields()
foo.calc_matrices()

