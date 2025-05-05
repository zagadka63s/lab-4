import unittest
import numpy as np
from src.lorenz import integrate_lorenz

class TestLorenzModel(unittest.TestCase):

    def test_solution_shape(self):
        """
        перевірка - що розмір вихідного рішення правильний: 3 змінні × N точок часу
        """
        t_span = (0, 10)
        t_eval = np.linspace(*t_span, 100)
        initial_state = [1.0, 1.0, 1.0]

        sol = integrate_lorenz(initial_state, t_span, t_eval)

        self.assertEqual(sol.y.shape, (3, 100))

    def test_sensitivity_to_initial_conditions(self):
        """
        перевірка - що мала зміна початкового стану призводить до значних відмінностей із часом
        """
        t_span = (0, 20)
        t_eval = np.linspace(*t_span, 1000)

        initial_state1 = [1.0, 1.0, 1.0]
        initial_state2 = [1.0001, 1.0, 1.0]

        sol1 = integrate_lorenz(initial_state1, t_span, t_eval)
        sol2 = integrate_lorenz(initial_state2, t_span, t_eval)

        difference = np.linalg.norm(sol1.y - sol2.y)

        self.assertGreater(difference, 1.0)

    def test_no_nans_or_infs(self):
        """
        проверка - что в решении нет NaN или Inf значений
        """
        t_span = (0, 20)
        t_eval = np.linspace(*t_span, 1000)
        initial_state = [1.0, 1.0, 1.0]

        sol = integrate_lorenz(initial_state, t_span, t_eval)

        self.assertFalse(np.isnan(sol.y).any(), "Розчин містить значення NaN.")
        self.assertFalse(np.isinf(sol.y).any(), "Розв'язок містить значення Inf.")

    def test_zero_initial_state(self):
        """
        перевірка - чи працює модель для початкового стану [0, 0, 0]
        """
        t_span = (0, 10)
        t_eval = np.linspace(*t_span, 100)
        initial_state = [0.0, 0.0, 0.0]

        sol = integrate_lorenz(initial_state, t_span, t_eval)

        self.assertEqual(sol.y.shape, (3, 100))

    def test_parameter_sensitivity(self):
        """
        перевірка – що зміна параметрів (σ, ρ, β) змінює результат
        """
        t_span = (0, 20)
        t_eval = np.linspace(*t_span, 1000)
        initial_state = [1.0, 1.0, 1.0]

        sol_default = integrate_lorenz(initial_state, t_span, t_eval)
        sol_modified = integrate_lorenz(initial_state, t_span, t_eval, sigma=14.0, rho=35.0, beta=3.0)

        delta = np.linalg.norm(sol_default.y - sol_modified.y)
        self.assertGreater(delta, 1.0)

if __name__ == "__main__":
    unittest.main()
