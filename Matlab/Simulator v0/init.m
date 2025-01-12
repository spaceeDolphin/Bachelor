%Mathematical model of tank with mass flow function based on inflow, outflow
%MPC optimization: minimize run costs
%Constraints: min/max levels, pump capacity

h = 7;
A = 380;
V = h*A;
qV_max = 120/3600; % m3/s
qOut_median = 30/3600;

list24 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]*3600;