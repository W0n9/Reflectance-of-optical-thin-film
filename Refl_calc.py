#%%
from math import *

import numpy as np

# %% [markdown]
# set wavelength and angle of incident light
#%%
# set wavelength
lambda_0 = 500
# convert angle to radians and change convention
angle = 0 * (pi / 180)

# %% [markdown]
# set structural parameters of multilayer

#%%
def Refl_calc(optical_thickness):
    # set the number of period in multilayer
    Num = 1
    # initialize the thickness for each layer
    z = np.zeros((2 * Num + 1, 1))
    # initialize the optical index for each layer
    F = np.zeros((2 * Num + 1, 1))
    # set the thickness of incident and exit medium
    z[0] = 10
    z[-1] = 10
    # set the optical index of incident and exit medium
    F[0] = 1
    F[-1] = 1.5
    # calculate number of layers in ML
    N = len(z)
    # set the index of each material in multilayer
    nL = 1.38
    # set optical thickness of layer to 1/4 wavelength
    dL = (optical_thickness) * lambda_0 / np.real(nL)

    # assign thickness and index to each layer in multilayer
    z[1] = dL
    F[1] = nL

    #%%
    # (c)initialize calculating values
    theta = np.zeros((N, 1))
    theta[0] = angle

    #%%
    # (d)calculating r and t of multilayer
    M = np.array([[1, 0], [0, 1]])
    # changing interface/layers
    for k in range(2, N):
        # determine refractive index of upper layer
        n1 = F[k - 1]
        # determine refractive index of this layer
        n2 = F[k - 2]
        # incident angle of this layer
        theta[k - 1] = asin(sin(theta[k - 1]) * n2 / n1)
        # pre-determine repeating constants (to save time)
        K = 2 * pi * cos(theta[k - 1]) / lambda_0
        # 有效位相厚度
        Q = K * n1 * z[k - 1]
        # optical admittance (for now set to S-polarized)
        p = n1 * cos(theta[k - 1])
        # a,b,c,d: component of 2x2 matrix representing each ML interface
        a = cos(Q)
        b = 1j * sin(Q) / p
        c = 1j * p * sin(Q)
        # d = cos(Q)
        # M is the product of m1*m2*...
        M = M @ np.array([[a, b], [c, a]], dtype=object)

    # angle in emergent medium
    theta[N - 1] = asin(sin(theta[0]) * F[0] / F[N - 1])
    # optical admittance incident and emergent medium
    p1 = F[0] * cos(theta[0])
    ps = F[N - 1] * cos(theta[N - 1])

    # S = M * [1; ps]
    S = M @ np.array([[1], [ps]], dtype=object)
    B = S[0, 0]
    C = S[1, 0]
    # 等效光学导纳
    Y = C / B
    # reflection coefficient
    r = (p1 - Y) / (p1 + Y)
    # reflectivity
    Refl = r * r.conj()
    return Refl[0].real
    # print("f'Refl = ", Refl[0].real)
    # print(f"Refl = {Refl[0].real:.3f}")


# t = 2 * p1 / (B * p1 + C)
# Trans = 4 * np.real(p1) * np.real(ps) / ((p1 * B + C) * (p1 * B + C).conj())
# print("Trans = ", Trans.real)
