import argparse

import numpy as np


def estimate_pi(num_points: int, seed: int | None = None):
    if seed is not None:
        np.random.seed(seed)

    x_coords = np.random.uniform(-1, 1, num_points)
    y_coords = np.random.uniform(-1, 1, num_points)

    distances = x_coords**2 + y_coords**2
    points_inside_circle = np.sum(distances <= 1)

    pi_estimate = 4 * points_inside_circle / num_points

    print(f"Number of points: {num_points}")
    print(f"Points inside circle: {points_inside_circle}")
    print(f"Estimated value of Pi: {pi_estimate}")
    print(f"Seed used: {seed}")


def main():
    parser = argparse.ArgumentParser(
        description="Estimate Pi using Monte Carlo simulation."
    )

    parser.add_argument(
        "--num-points",
        type=int,
        default=100000,
        help="Number of random points to generate.",
    )

    parser.add_argument(
        "--seed", type=int, default=None, help="Random seed for reproducibility."
    )

    args = parser.parse_args()

    estimate_pi(num_points=args.num_points, seed=args.seed)


if __name__ == "__main__":
    main()
