from src.lorenz import integrate_lorenz
from src.plotter import plot_trajectory, compare_trajectories
import numpy as np

def main():
    # час інтеграції
    t_span = (0, 40)
    t_eval = np.linspace(*t_span, 10000)

    # базовий початковий стан
    initial_state = [1.0, 1.0, 1.0]

    # з легким відхиленням для демонстрації хаосу
    perturbed_state = [1.0001, 1.0, 1.0]

    # рішення системи
    sol_original = integrate_lorenz(initial_state, t_span, t_eval)
    sol_perturbed = integrate_lorenz(perturbed_state, t_span, t_eval)

    # побудова основної траєкторії
    plot_trajectory(sol_original, title="Lorenz Attractor - Original", color="blue", label="Original State")

    # порівняння двох траєкторій
    compare_trajectories(sol_original, sol_perturbed, labels=("Original", "Perturbed"))

if __name__ == "__main__":
    main()
