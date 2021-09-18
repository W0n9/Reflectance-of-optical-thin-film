%Program Reflectance of optical thin film----for S polarization (by chengyou lin-2013.9.16)
clear all; clc %saves grief by clearing previous variables and clearing screen

%(a)set wavelength and angle of incident light(start)

lambda = 500; %set wavelength

angle = 0 * (pi / 180); %convert angle to radians and change convention
%(a)set wavelength and angle of incident light(over)

%(b)set structural parameters of multilayer(start)
Num = 5; %set the number of period in multilayer
z = zeros(2 * Num + 2, 1); %initialize the thickness for each layer
F = zeros(2 * Num + 2, 1); %initialize the  optical index for each layer

z(1) = 10; z(2 * Num + 2) = 10; %set the thickness of incident and exit medium
F(1) = 1; F(2 * Num + 2) = 1; %set the optical index of incident and exit medium

N = length(z); %calculate number of layers in ML

nH = 2.5; nL = 1.25; % set the index of each material in multilayer

dH = (1/4) * lambda / real(nH); %set optical thickness of layer to 1/4 wavelength
dL = (1/4) * lambda / real(nL); % %set optical thickness of layer to 1/4 wavelength

%assign thickness and index to each layer in multilayer
for m = 1:Num
    z(2 * m) = dH;
    F(2 * m) = nH; %low index material
    z(2 * m + 1) = dL;
    F(2 * m + 1) = nL; %high index material
end

%assign thickness and index to each layer in multilayer
%(b)set structural parameters of multilayer(over)

%{
%(b)set structural parameters of multilayer(start)
na = 1; ng = 1; nH = 2.5; nL = 1.25;
da = 10; dg = 10;
dH = (1/4) * lamda0 / real(nH); %set optical thickness of layer to 1/4 wavelength
dL = (1/4) * lamda0 / real(nL); % %set optical thickness of layer to 1/4 wavelength
z = [da; dH; dL; dH; dL; dH; dL; dH; dL; dH; dL; dg]; F = [na; nH; nL; nH; nL; nH; nL; nH; nL; nH; nL; ng];
N = length(z); %calculate number of layers in ML

%(b)set structural parameters of multilayer(over)

%}

%{
%(b)set structural parameters of multilayer(start)
fid1 = '001.txt'; [Fn, Fk, z] = textread(fid1, '%f %f %f');
F = Fn - Fk * 1i;
N = length(z); %calculate number of layers in ML

%(b)set structural parameters of multilayer(over)

%}

%(c)initialize calculating values (start)
theta = zeros(N, 1); theta(1) = angle;
%(c)initialize calculating values (over)

%(d)calculating r and t of multilayer(start)
% for m = 1:length(lamda) %changing Lambda

M = [1, 0; 0, 1];

for k = 2:N - 1 %changing interface/layers
    n1 = F(k); %determine refractive index of upper layer
    n2 = F(k - 1); %determine refractive index of this layer
    theta(k) = asin(sin(theta(k - 1)) * n2 / n1); %incident angle of this layer

    K = 2 * pi * cos(theta(k)) ./ lambda; %pre-determine repeating constants (to save time)
    Q = K * n1 * z(k); %有效位相厚度
    p = n1 * cos(theta(k)); %optical admittance (for now set to S-polarized)

    a = cos(Q); %a,b,c,d: component of 2x2 matrix representing each ML interface
    b = 1i * sin(Q) / p;
    c = 1i * p * sin(Q);
    %d = cos(Q);
    M = M * [a, b; c, a]; %M is the product of m1*m2*...

end

theta(N) = asin(sin(theta(1)) * F(1) / F(N)); % angle in emergent medium
p1 = F(1) * cos(theta(1)); ps = F(N) * cos(theta(N)); %optical admittance incident and emergent medium
S = M * [1; ps];
B = S(1, 1); C = S(2, 1);
Y = C / B; %等效光学导纳
r = (p1 - Y) / (p1 + Y); %reflection coefficient
Refl = abs(r)^2 %reflectivity

t = 2 * p1 / (B * p1 + C);
Trans = 4 * real(p1) * real(ps) / (abs(p1 * B + C)^2)
