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

        self.d_value = [0 for i in range(10)]
        self.spot_rates = [0 for i in range(10)]
        self.c_value = [0 for i in range(10)]
        self.a_value = [0 for i in range(10)]
        self.e_value = [0 for i in range(10)]

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
        self.calc_all_yields()
        self.eer = [i * 100 for i in self.eer]

        for i, j in enumerate(np.minimum.accumulate(self.eer[::-1])[::-1]):
            print(f"Average p.a. return (%) for Year {i + 1}: {j:.2f}")

        """
        These equation below only exists as experimental proof from equation 4.3 and equation 4.5
        
        def recursion_spot_rate(x, y):
            if x == 0:
                return self.eer[y] / (1 + self.spot_rates[x])
            else:
                return (self.eer[y] / ((1 + self.spot_rates[x]) ** (x + 1))) + recursion_spot_rate(x - 1, y)
                
        for i, j in enumerate(self.eer):  # Equation 4.3(a)
            if i == 0:
                self.d_value[i] = 1 / (1 + self.eer[i])
                self.spot_rates[i] = self.eer[i]
            else:
                self.d_value[i] = ((1 - (self.eer[i] * (sum(self.d_value[:i])))) / (1 + self.eer[i]))
                self.spot_rates[i] = (self.eer[i] * (i + 1)) - sum(self.spot_rates)

        def recursion_c_value(x):  # Equation 4.3(b)
            if x == 0:
                return self.c_value[x] * self.d_value[x]
            else:
                return (self.c_value[x] * self.d_value[x]) + recursion_c_value(x - 1)

        for i in range(len(self.c_value)):
            self.c_value[i] = ((1 - recursion_c_value(i)) / self.d_value[i]) - 1

            if i == 0:
                self.c_value[i] = (1 / self.d_value[i]) - 1
                self.a_value[i] = self.c_value[i]
            else:
                self.a_value[i] = self.c_value[i] - self.c_value[i - 1]
                if self.a_value[i] < 0:
                    self.a_value[i] = 0

        def recursion_proof(x):  # Equation 4.3(c)
            if x == 0:
                return self.c_value[x] / (1 + self.spot_rates[x])
            elif x == 9:
                return ((1 + self.c_value[x]) / ((1 + self.spot_rates[x]) ** (x + 1))) + recursion_proof(x - 1)
            else:
                return (self.c_value[x] / ((1 + self.spot_rates[x]) ** (x + 1))) + recursion_proof(x - 1)

        def recursion_e_value(x):  # Equation 4.5
            if x == 0:
                return self.a_value[x] / ((1 + self.spot_rates[x]) ** (x + 1))
            else:
                return (sum(self.a_value[:x + 1]) / ((1 + self.spot_rates[x]) ** (x + 1))) + recursion_e_value(x - 1)

        for i in range(10):
            self.e_value[i] = 1 - (1 / ((1 + self.spot_rates[i]) ** (i + 1))) - (recursion_e_value(i))
            if i == 9:
                self.e_value[i] = 0

        self.e_value = [(i ** 2) for i in self.e_value]
        """
