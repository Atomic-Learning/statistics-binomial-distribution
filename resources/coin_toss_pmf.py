from math import comb
from pathlib import Path

import matplotlib.pyplot as plt


def binomial_pmf(n: int, p: float, k: int) -> float:
	"""Return P(X = k) for X ~ Binomial(n, p)."""
	return comb(n, k) * (p**k) * ((1 - p) ** (n - k))


def main() -> None:
	n = 10
	p = 0.5
	k_values = list(range(n + 1))
	pmf_values = [binomial_pmf(n, p, k) for k in k_values]

	fig, ax = plt.subplots(figsize=(8, 4.5), constrained_layout=True)

	markers, stems, baseline = ax.stem(k_values, pmf_values, basefmt=" ")
	plt.setp(stems, linewidth=2)
	plt.setp(markers, markersize=7)

	ax.set_title("Binomial PMF: Number of Heads in 10 Fair Coin Tosses")
	ax.set_xlabel("Number of heads, k")
	ax.set_ylabel("P(X = k)")
	ax.set_xticks(k_values)
	ax.grid(axis="y", linestyle="--", alpha=0.35)

	output_path = Path(__file__).with_name("coin_toss_pmf.png")
	fig.savefig(output_path, dpi=300)
	plt.close(fig)

	print(f"Saved stem diagram to: {output_path}")


if __name__ == "__main__":
	main()
