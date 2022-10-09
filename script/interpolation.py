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

        self.c_value = [0 for i in range(10)]
        self.a_value = [0 for i in range(10)]
        self.e_value = [0 for i in range(10)]
        self.var = [0 for i in range(10)]

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
            if i >= 2:
                if i <= 4:
                    self.eer[i] = (self.matrix_n[1][0] * ((i + 1) - 2) ** 3 +
                                   self.matrix_n[1][1] * ((i + 1) - 2) ** 2 +
                                   self.matrix_n[1][2] * ((i + 1) - 2) ** 1 +
                                   self.matrix_n[1][3])
                else:
                    self.eer[i] = (self.matrix_n[2][0] * ((i + 1) - 5) ** 3 +
                                   self.matrix_n[2][1] * ((i + 1) - 5) ** 2 +
                                   self.matrix_n[2][2] * ((i + 1) - 5) ** 1 +
                                   self.matrix_n[2][3])
            else:
                self.eer[i] /= 100

        return self.eer

    def step_up_rates(self):
        def recursion_time(step_up, yikes, n):  # This proves equation c!
            if (not step_up) or (not yikes):
                return 0
            else:
                if n == 10:
                    return ((1 + step_up[-1]) / (1 + yikes[-1]) ** n) + recursion_time(step_up[:-1], yikes[:-1], n - 1)
                else:
                    return ((step_up[-1]) / (1 + yikes[-1]) ** n) + recursion_time(step_up[:-1], yikes[:-1], n - 1)

        self.var = self.calc_all_yields()

        # Manual mathematical jargon to calculate C, this is necessary but, I will need to optimize this in code.
        self.c_value[0] = self.var[0]
        self.c_value[1] = ((1 - (self.var[0] / (1 + self.var[0]) ** 1)) * ((1 + self.var[1]) ** 2)) - 1
        self.c_value[2] = ((1 - (self.var[0] / (1 + self.var[0]) ** 1) - (self.var[1] / (1 + self.var[1]) ** 2)) *
                           ((1 + self.var[2]) ** 3)) - 1
        self.c_value[3] = ((1 - (self.var[0] / (1 + self.var[0]) ** 1) - (self.var[1] / (1 + self.var[1]) ** 2) -
                            (self.var[2] / (1 + self.var[2]) ** 3)) * ((1 + self.var[3]) ** 4)) - 1
        self.c_value[4] = ((1 - (self.var[0] / (1 + self.var[0]) ** 1) - (self.var[1] / (1 + self.var[1]) ** 2) -
                            (self.var[2] / (1 + self.var[2]) ** 3) - (self.var[3] / (1 + self.var[3]) ** 4)) *
                           ((1 + self.var[4]) ** 5)) - 1
        self.c_value[5] = ((1 - (self.var[0] / (1 + self.var[0]) ** 1) - (self.var[1] / (1 + self.var[1]) ** 2) -
                            (self.var[2] / (1 + self.var[2]) ** 3) - (self.var[3] / (1 + self.var[3]) ** 4) -
                            (self.var[4] / (1 + self.var[4]) ** 5)) * ((1 + self.var[5]) ** 6)) - 1
        self.c_value[6] = ((1 - (self.var[0] / (1 + self.var[0]) ** 1) - (self.var[1] / (1 + self.var[1]) ** 2) -
                            (self.var[2] / (1 + self.var[2]) ** 3) - (self.var[3] / (1 + self.var[3]) ** 4) -
                            (self.var[4] / (1 + self.var[4]) ** 5) - (self.var[5] / (1 + self.var[5]) ** 6)) *
                           ((1 + self.var[6]) ** 7)) - 1
        self.c_value[7] = ((1 - (self.var[0] / (1 + self.var[0]) ** 1) - (self.var[1] / (1 + self.var[1]) ** 2) -
                            (self.var[2] / (1 + self.var[2]) ** 3) - (self.var[3] / (1 + self.var[3]) ** 4) -
                            (self.var[4] / (1 + self.var[4]) ** 5) - (self.var[5] / (1 + self.var[5]) ** 6) -
                            (self.var[6] / (1 + self.var[6]) ** 7)) * ((1 + self.var[7]) ** 8)) - 1
        self.c_value[8] = ((1 - (self.var[0] / (1 + self.var[0]) ** 1) - (self.var[1] / (1 + self.var[1]) ** 2) -
                            (self.var[2] / (1 + self.var[2]) ** 3) - (self.var[3] / (1 + self.var[3]) ** 4) -
                            (self.var[4] / (1 + self.var[4]) ** 5) - (self.var[5] / (1 + self.var[5]) ** 6) -
                            (self.var[6] / (1 + self.var[6]) ** 7) - (self.var[7] / (1 + self.var[7]) ** 8)) *
                           ((1 + self.var[8]) ** 9)) - 1
        self.c_value[9] = ((1 - (self.var[0] / (1 + self.var[0]) ** 1) - (self.var[1] / (1 + self.var[1]) ** 2) -
                            (self.var[2] / (1 + self.var[2]) ** 3) - (self.var[3] / (1 + self.var[3]) ** 4) -
                            (self.var[4] / (1 + self.var[4]) ** 5) - (self.var[5] / (1 + self.var[5]) ** 6) -
                            (self.var[6] / (1 + self.var[6]) ** 7) - (self.var[7] / (1 + self.var[7]) ** 8) -
                            (self.var[8] / (1 + self.var[8]) ** 9)) * ((1 + self.var[9]) ** 10)) - 1

    def adjustments(self):
        self.step_up_rates()

        for i, j in enumerate(self.a_value):
            if i == 0:
                self.a_value[i] = self.c_value[i]
            else:
                self.a_value[i] = self.c_value[i] - self.c_value[i - 1]

        r_value = [0 for i in range(10)]
        t_value = [0 for i in range(10)]

        print(self.var)

        for i in range(10):
            r_value[i] = (1 + self.var[i]) ** (i + 1)

            t_value[i] = sum(self.a_value[0: i + 1]) / r_value[i]  # Issue

        for i in range(9):
            self.e_value[i] = 1 - (1 / r_value[i]) - sum(t_value[0: i + 1])

        self.e_value = [self.e_value[i] ** 2 for i in range(10)]

        print(self.e_value)
        print(self.eer)

