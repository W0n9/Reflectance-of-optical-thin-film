from Refl_calc import Refl_calc

if __name__ == "__main__":
    optical_thickness_list = [0.25, 0.5, 0.75, 1]
    for _ in optical_thickness_list:
        print(f"Current Optical Thickness is {_} * lambda")
        print(f"Refl = {Refl_calc(_):.3f}")
