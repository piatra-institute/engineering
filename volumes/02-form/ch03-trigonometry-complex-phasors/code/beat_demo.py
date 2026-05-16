"""Beat demonstration: two sinusoids at nearby frequencies and their sum.

Synthesises two unit-amplitude sinusoids at frequencies f_1 and f_2
and plots their sum to display the beat envelope at half the
difference frequency.

Usage:
    uv run --with numpy --with matplotlib beat_demo.py

Dependencies: numpy, matplotlib.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    f_1 = 10.0
    f_2 = 11.0
    t = np.linspace(0, 4.0, 5001)
    x1 = np.cos(2 * np.pi * f_1 * t)
    x2 = np.cos(2 * np.pi * f_2 * t)
    x_sum = x1 + x2
    envelope = 2 * np.abs(np.cos(np.pi * (f_2 - f_1) * t))

    fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(7, 5),
                                          sharex=True)
    ax_top.plot(t, x1, label=f"{f_1} Hz", linewidth=0.8, color="blue")
    ax_top.plot(t, x2, label=f"{f_2} Hz", linewidth=0.8, color="red")
    ax_top.set_ylabel("amplitude")
    ax_top.legend(loc="best", fontsize=8)
    ax_top.grid(True, alpha=0.3)

    ax_bot.plot(t, x_sum, label="sum", linewidth=0.8, color="black")
    ax_bot.plot(t, envelope, label="envelope $|2\\cos(\\pi\\Delta f t)|$",
                linewidth=1.4, color="red")
    ax_bot.plot(t, -envelope, linewidth=1.4, color="red")
    ax_bot.set_xlabel("t (s)")
    ax_bot.set_ylabel("amplitude")
    ax_bot.legend(loc="best", fontsize=8)
    ax_bot.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("beat_demo.png", dpi=120)
    print("Wrote beat_demo.png")
    print(f"Envelope period: {1.0 / (f_2 - f_1):.4f} s = "
          f"1 / Delta f = 1 / {f_2 - f_1} Hz")


if __name__ == "__main__":
    main()
