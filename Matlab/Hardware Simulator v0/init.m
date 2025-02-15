%Mathematical model of tank with mass flow function based on inflow, outflow
%Constraints: min/max levels, pump capacity

% Tank
h = 3.8;
A = 160;
V = h*A; % 608 m3
LimitHigh = 3.8; % not used
LimitLow = 2; % not used
InitialLevel = 3.0;

% Flow
qV_max = 50/3600; % m3/s
qOut_median = 16.6/3600;
qOut_usualMax = 23.9/3600;
qOut_usualMin = 10.6/3600;
qOut_simAmplitude = (qOut_usualMax - qOut_usualMin)/2;
FlowBoost = 100; % multiplies flow to speed up simulation process

% Time
list301 = [0:300]*(86400/300); % used to lookup flowOut value from real values