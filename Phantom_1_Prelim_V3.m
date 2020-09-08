%% Solid Motor Nozzle Contour Code
% Purpose: Automate the calculations for all future solid motor nozzle
% contours depending on paraM_eters. Referenced Rocket Propulsion EleM_ents
% 9th Ed (Sutton & Biblarz) & Modern Compressible Flow 3rd Ed (Anderson)
% Designed by Edwin G., 3/27/20

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   Subscript Notation:
%   0: Conditions in the Combustion Chamber (Equivalent to Stagnation
%   Properties)
%   t: Conditions in the Nozzle Throat
%   e: Conditions in the Nozzle Exit 
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Chamber Conditions (Input Values)
clc; close all; clear all;

% State Properties
p_0 = xlsread('Phantom_I.xlsx','Parameters','B2'); % [Pa] Chamber Pressure (AssuM_ed)
p_0_psi = p_0/(6895);
T_0 = xlsread('Phantom_I.xlsx','Parameters','B3'); % [K] Chamber Temperature (Calculated; Theoretical)
T_0_R = T_0 * 1.8;
rho_0_s = xlsread('Phantom_I.xlsx','Parameters','B4'); % [kg/m^3] Solid Product Chamber Density (Calculated; Actual)
v_0 = 0; % [m/s] Chamber velocity (AssuM_ed); Chemical reactions at nov exhuast gas velocity
k = xlsread('Phantom_I.xlsx','Parameters','B5'); % [No Units] Propellant Specific Heat Ratio
c_star = xlsread('Phantom_I.xlsx','Parameters','B7'); % [m/s] C-Star; Combustion Efficiency (Calculated; Theoretical)

% Viscosity Properties (WILL NEED TO BE RE-DESIGNED IF # of CHEMICALS CHANGE)

h2_mf = xlsread('Phantom_I.xlsx','Parameters','B20'); % [No Units] Hydrogen Molar Frac.
co_mf = xlsread('Phantom_I.xlsx','Parameters','B24'); % [No Units] Carbon Monoxide Molar Frac.
n2_mf = xlsread('Phantom_I.xlsx','Parameters','B28'); % [No Units] Nitrogen Molar Frac.
hcl_mf = xlsread('Phantom_I.xlsx','Parameters','B32'); % [No Units] Hydrochloric Acid Molar Frac.

h2_mw = xlsread('Phantom_I.xlsx','Parameters','B21'); % [g/mol] Hydrogen Molecular Weight
co_mw = xlsread('Phantom_I.xlsx','Parameters','B25'); % [g/mol] Carbon Monoxide Molecular Weight
n2_mw = xlsread('Phantom_I.xlsx','Parameters','B29'); % [g/mol] Nitrogen Molecular Weight
hcl_mw = xlsread('Phantom_I.xlsx','Parameters','B33'); % [g/mol] Hydrochloric Acid Molecular Weight

Temp = 300:25:3000; % [k] Temp array to be used to solve for viscosity/therm conduc.

% Misc. Properties
mw = xlsread('Phantom_I.xlsx','Parameters','B6'); % [No Units] Overall Molecular Weight (Calculated; Theoretical)
I_s = xlsread('Phantom_I.xlsx','Parameters','B8'); % [s] Frozen Specific Impulse (Calculated; Theoretical)
I_t = xlsread('Phantom_I.xlsx','Parameters','B13'); % [N*s] Desired Total Impulse (AssuM_ed)
R = xlsread('Phantom_I.xlsx','Parameters','B9'); % [J/kg*k] Specific Propellant Gas Const. (Calculated; Theoretical)
FT = xlsread('Phantom_I.xlsx','Parameters','B10'); % [N] Average Thrust Desired (AssuM_ed)
r = xlsread('Phantom_I.xlsx','Parameters','B11'); % [in/s] Burn rate at Chamber Pressure (M_easured)

% State Properties (Pt.2); Calculating Gaseous Density of the Reactants
rho_0 = (p_0)/(R*T_0); % [kg/m^3] Gaseous Product Chamber Density (Calculated; Theoretical)

%% Throat Conditions (Calculated)

% Following key paraM_eters are calculated: v_t, M_t, T_t, p_t and vol_spec_t

term_t = ((2*k)/(k+1)); % Term used in throat velocity eq, simplifies computation
v_t = sqrt(term_t*R*T_0); % [m/s] Throat Velocity (Theoretical) - (Eq 3-23; Sutton)

a_t = v_t; % [m/s] Speed of Sound (Theoretical); Assuming flow will be choked at the throat

M_t = v_t/a_t; % [No Units] Throat Mach Number; Will be 1 since flow is choked at the throat

T_t = (2*T_0)/(k+1); % [K] Throat Static Temperature (Theoretical) - (Eq 3-22; Sutton)

p_t = p_0*(2/(k+1))^(k/(k-1)); % [Pa] Throat Static Pressure (Theoretical) - (Eq 3-20; Sutton)

% Instead of calculating density at the throat, we will calculate its
% reciporcal, specific voluM_e at the throat. Gives a more telling story of
% the expansion of the exhuast gases. 

vol_spec_0 = (1/rho_0);
vol_spec_t = (vol_spec_0)*((k+1)/2)^(1/(k-1)); % [m^3/kg] Static Throat Specific VoluM_e (Theoretical) - (Eq 3-21; Sutton)

%% Exit Conditions (Calculated)

% Following key paraM_eters are calculated: pr, v_e, vol_spec_e and M_e

p_e = 101325; % [Pa] Exit Pressure (AssuM_ed); The exit pressure is equivalent to ambient pressure
pr = p_e/p_0; % Pressure Ratio; Ratio of Static Exit Pressure to Static/Stagnation Chamber Pressure

term1_e = (2*k)/(k-1); % Term used in exit velocity eq, simplifies computation
term2_e = R*T_0; % Term used in exit velocity eq, simplifies computation
term3_e = 1-(pr)^((k-1)/k); % Term used in exit velocity eq, simplifies computation
v_e = sqrt((term1_e)*(term2_e)*(term3_e)); % [m/s] Mean Exit Velocity (Theoretical) - (Eq 3-16; Sutton)

vol_spec_e = vol_spec_0*(1/pr)^(1/k); % [m^3/kg] Exit Specific volume (Theoretical) - (Page 55; See Example 3.2; Sutton)

% There are two Methods of finding exit mach number, first you can
% calculate it by using:

% M_e = v_e/a_e = v_e/sqrt(k*R*T_e) ; However, we do not know T_e, so this
% M_ethod is not reasonable, there's another way...

% By using the isentropic relations laid out in (Eq 3-30; Anderson), we can
% relate the pressure ratio at the exit to the Mach # at the exit. 

term4_e = (1/(pr))^((k-1)/k)-1;  % Term used in exit mach # eq, simplifies computation
term5_e = 2/(k-1);  % Term used in exit mach # eq, simplifies computation 
M_e = sqrt((term4_e)*(term5_e)); % [No Units] Exit Mach Number (Theoretical) - (Eq 3-30; Anderson OR Eq 3-13; Sutton)

%% Nozzle Dimensions (Calculations)

% Following key paraM_eters are calculated: ar, e, cf, A_t, A_e, A_b,
% A_0, t_b and b

%cf = thrust coefficient
%ar = area ratio
%e = expansion ratio
%A_b = bore area of hole in solid fuel grain
%b = web thickness
%t_b = total burn time

term1_d = 1+((k-1)/2)*M_e^2;  % Term used in area ratio eq, simplifies computation
term2_d = 1+((k-1)/2); % Term used in area ratio eq, simplifies computation
ar = (1/M_e)*sqrt(((term1_d)/(term2_d))^((k+1)/(k-1))); % [No Units] Area Ratio (Exit Area/Throat Area) - (Eq 3-14; Sutton)

e = ar; % The previously calculated area ratio is equal to the paraM_eter known as the Nozzle Expansion Ratio

term3_d = (2*k^2)/(k-1); % Term used in Thrust coefficient eq, simplifies computation
term4_d = (2/(k+1))^((k+1)/(k-1)); % Term used in Thrust coefficient eq, simplifies computation
term5_d = term3_e; % Term used in Thrust coefficient eq, simplifies computation
cf = sqrt((term3_d)*(term4_d)*(term5_d)); % [No Units] Thrust Coefficient; Explains thrust amplification of nozzle (Theoretical) - (Eq 3-30; Sutton)

A_t_Meters = (FT/(cf*p_0)); % [m^2] Throat Area using Average Thrust Desired - (Eq 3-31; Sutton)
A_t = A_t_Meters * (39.37)^2; % [in^2] Throat Area; Converted from m^2 to in^2
TR = sqrt(A_t/pi); % [in] Throat radius

A_e = e*A_t; % [in^2] Exit Area
DR = sqrt(A_e/pi); % [in] Exit Radius (DR suppose to be ER: 4am type shit)


% Before A_b is calculated, let's understand what A_b exactly is. Subscript 0 refers to the 
% combustion chamber cross-sectional. However, we also have a bore hole in our propellant grains. Since we are following 
% a rule of thumb to avoid the cross-sectional area of the chamber equalling to that of the throat, we must make the bore 
% diaM_eter follow this rule. Therefore, A_b is the cross-sectional bore area, and it will be calculated, NOT A_0, 
% the inner combustion chamber cross-sectional area. 

A_b_least = 3.5 * A_t; % [in^2] Least possible bore area; Must be at least 3.5 times larger than the throat area to retain 99% thrust or more. (Table 3-2; Pg 75; Sutton)

A_0 = 1.373; % [in] This inner chamber cross-sectional area is imposed because of the diM_ensions of a 38mm motor casing interior diaM_eter. 

t_b = (I_t/FT) * 1.05; % [s] Burn tiM_e (duration) of the solid propellant; Multiplied by 1.05 to account for silvers in the propellant.
b = r*t_b; % [in] Web Thickness; DiaM_eter difference between the Bore Area & Chamber Inner Area; Neccsary for proper burn tiM_e.

%%%%%%%%%%%%%%%%%%% Boring Area Set of Calculations %%%%%%%%%%%%%%%%%%%%%

D_0 = 2*sqrt(A_0/pi); % [in] Inner chamber cross-sectional diaM_eter; To be used to calculate A_b
D_b_large = (D_0 - 2*b); % [in] Largest possible bore diaM_eter using the necessary web thickness
A_b_large = pi*(D_b_large/2)^2; % [in^2) Largest possible bore area; Following the requireM_ent of Web thickness

% The Bore ratio must be greater than 1 to demonstrate the boring diaM_eter
% is at least 3.5 tiM_es larger than than the throat diaM_eter

br = A_b_large/A_b_least; % [No Units] Bore ratio, Must be larger than 1 to determine the boring area is at least 3.5 tiM_es larger 
                         % and utilizes the necessary web thickness.

% To ensure, both boring requireM_ents are kept:
if br >= 1
    A_b = A_b_large;
else
    A_b = 0;
end

%% Viscosity & Thermal Conductivity Input Parameters --------------------------------------------------------------------------------

% The viscosity & thermal conductivity input parameters are turned into
% arrays, they will be utilized for thermal conductivity and visocisity
% calculations.

mw_a = [h2_mw co_mw n2_mw hcl_mw]; % Chem specimen molecular weight array (g/mol)
mf_a = [h2_mf co_mf n2_mf hcl_mf]; % Chem specimen molar fraction array (No Unit)


%% Viscosity & Thermal Conductivity Calculations -------------------------------------------------------------------------------- 

% Overview: The code below feeds different values of viscosity & thermal
% conductivity at different temperatures.  

% Arrays are given pre-located size to lessen computational time.

h2_mu_a = zeros(1, length(Temp));
co_mu_a = zeros(1, length(Temp));
n2_mu_a = zeros(1, length(Temp));
hcl_mu_a = zeros(1, length(Temp));

h2_k_a = zeros(1, length(Temp));
co_k_a = zeros(1, length(Temp));
n2_k_a = zeros(1, length(Temp));
hcl_k_a = zeros(1, length(Temp));

% Functions dependent on temperature are given for the properties of viscosity and thermal conductivity. 

for i=1:length(Temp)
    h2_mu_a(i) =(27.758+((2.12*10^-1)*(Temp(i)))+((-3.28*10^-5)*((Temp(i))^2)))*(10^-2); % Chem specimen viscosity array (10^-5 Pa*s or kg/mg*s) 
    co_mu_a(i) =((23.811)+(5.3944*10^-1)*(Temp(i))+(-1.5411*10^-4)*(Temp(i))^2)*10^-2; % Chem specimen viscosity array (10^-5 Pa*s or kg/m*s) 
    n2_mu_a(i) =((42.606)+(4.75*10^-1)*(Temp(i))+(-9.88*10^-5)*(Temp(i))^2)*10^-2; % Chem specimen viscosity array (10^-5 Pa*s or kg/m*s) 
    hcl_mu_a(i) =((-9.118)+(5.55*10^-1)*(Temp(i))+(-1.11*10^-4)*(Temp(i))^2)*10^-2; % Chem specimen viscosity array (10^-5 Pa*s or kg/m*s) 
    
    h2_k_a(i) =(0.03951+(4.5918*10^-4)*(Temp(i))+(-6.4933*10^-8)*(Temp(i))^2)*1000; % Chem specimen thermal conductivity array(W/m*k)
    co_k_a(i) =(0.00158+(8.2511*10^-5)*(Temp(i))+(-1.9081*10^-8)*(Temp(i))^2)*1000; % Chem specimen thermal conductivity array(W/m*k)
    n2_k_a(i) =(0.00309+(7.593*10^-5)*(Temp(i))+(-1.1014*10^-8)*(Temp(i))^2)*1000; % Chem specimen thermal conductivity array(W/m*k)
    hcl_k_a(i) =((0.00119)+(4.4775*10^-5)*(Temp(i))+(2.099*10^-10)*(Temp(i))^2)*1000; % Chem specimen thermal conductivity array(W/m*k)
end

% Arrays that are 1xlength(temp) size are computed that give the properties of viscosity and thermal conductivity for each chemical constituent over a given temperature range.

k_aa = [h2_k_a co_k_a n2_k_a hcl_k_a];
mu_aa = [h2_mu_a co_mu_a n2_mu_a hcl_mu_a];

visc_mixture_a = zeros(1, length(Temp));    %Viscosity results array
k_mixture_a = zeros(1, length(Temp));       %Thermal Conductivity results array

% Arrays that are 1x4 size for both viscosity and thermal conductivity. These represent the chemical consistuents' viscosity and thermal conductivity at a temperature data point. 
% These are inputted into the calc_visc_therm_mixture function in a for-loop manner. Which ultimately gives a tabulated data of the visocisty and thermal conudctivity for the gas mixture
% at temperature data points.

for kk=1:length(Temp)
    mu_aaa = [mu_aa(kk), mu_aa(kk+length(Temp)), mu_aa(kk+(2*length(Temp))), mu_aa(kk+(3*length(Temp)))]; %Feeds the 
    k_aaa = [k_aa(kk), k_aa(kk+length(Temp)), k_aa(kk+(2*length(Temp))), k_aa(kk+(3*length(Temp)))];
    
    [visc_mixture_a(kk), k_mixture_a(kk)] = calc_visc_therm_mixture(mw_a, mu_aaa, mf_a, k_aaa);
end

%% Output of All Answers

% Output of Chamber Conditions:
fprintf("The output of necessary parameter values for the Nozzle Contour Program: \n");
fprintf(" Exit Mach Number: %4.2f \n", M_e);
fprintf(" Throat Area [in^2]: %6.4f \n", A_t);
fprintf(" Throat Radius (Will Need to Multiply the Nozzle Contour After Outputted) [in]: %6.3f \n", TR);
fprintf(" Nozzle Expansion Ratio: %6.4f \n", e);
fprintf(" Chamber Pressure [Psi]: %6.2f \n", p_0_psi);
fprintf(" Chamber Temperature [R]: %6.2f \n", T_0_R);
fprintf(" Gamma: %5.4f \n", k);
fprintf(" Chamber Condition Viscosity (at 2000 K) [10^-5 kg/m*s]: %8.6f \n", visc_mixture_a(69));
fprintf(" Chamber Condition Thermal Conductivity (at 2000 K) [W/m*K]: %8.6f \n", k_mixture_a(69));
fprintf("The values of viscosity and thermal conductivity have been plotted in the 'Graphs' sheet of the excel sheet. \n");

xlswrite('Phantom_I.xlsx',transpose(Temp),'Graphs','A3:A111');
xlswrite('Phantom_I.xlsx',transpose(visc_mixture_a),'Graphs','B3:B111');
xlswrite('Phantom_I.xlsx',transpose(k_mixture_a),'Graphs','C3:C111');

% Graph 

visc_coef = polyfit(Temp, visc_mixture_a,2); % These are NOT the coefficients of the polynomial!
therm_coef = polyfit(Temp, k_mixture_a,2); % These are NOT the coefficients of the polynomial!

temp_plot = 1:1:3000;
visc_plot = polyval(visc_coef,temp_plot);
therm_plot = polyval(therm_coef,temp_plot);

figure(1)
plot(Temp,visc_mixture_a,'o',temp_plot,visc_plot);
title('Viscosity Values Over Temperature Distribution');
xlabel('Temperature (k)');
ylabel('Viscosity (10^-5 kg/m*s)');
legend('Viscosity Data Pts.','Estimated Viscosity Polynomial');
grid on

hold on

figure(2)
plot(Temp,k_mixture_a,'o',temp_plot,therm_plot);
title('Thermal Conductivity Values Over Temperature Distribution');
xlabel('Temperature (k)');
ylabel('Thermal Conductivity (W/m*K)');
legend('Therm C. Data Pts.','Estimated Therm C. Polynomial');
grid on
