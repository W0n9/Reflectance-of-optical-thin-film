import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from Refl_calc import Refl_calc

chinese_font = FontProperties(fname="/usr/share/fonts/source/SourceHanSans-Normal.ttc")

if __name__ == "__main__":
    x = []
    R = []
    for _ in range(0, 1001):
        x.append(_ / 1000)
        R.append(Refl_calc(_ / 1000))

    plt.figure(figsize=(12, 9))
    plt.plot(x, R)
    plt.title("反射率R随MgF2薄膜光学厚度变化的曲线", fontproperties=chinese_font)
    plt.xlabel("λ0", fontproperties=chinese_font)
    plt.ylabel("反射率R", fontproperties=chinese_font)
    plt.show()
