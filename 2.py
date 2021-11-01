import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from Refl_calc import Refl_calc

# chinese_font = FontProperties(fname="/usr/share/fonts/source/SourceHanSans-Bold.ttc")

if __name__ == "__main__":
    x = []
    R = []
    for _ in range(0, 1001):
        x.append(_ / 1000)
        R.append(Refl_calc(_ / 1000))

    plt.figure(figsize=(12, 9))
    plt.plot(x, R, "b", linewidth=5.0)
    plt.title("Reflectivity with the optical thickness of MgF2")
    plt.xlabel("λ0")
    plt.ylabel("Reflectivity")
    plt.savefig("fig.jpg", pad_inches=0)
    plt.show()
