# DS_Lorenz_Attractor
similar to the Rossler simulation
## Method

Simpletic Runge-Kutta of 4 order

### Global Conditions

time_step = 0.01

### Initial Conditions

x_0 = 1
y_0 = 1
z_0 = 1

for the Lyapunov calculation a $\delta=1e^{-6}$ was add to the original IC.

## Results 

![original Lorenz attractor](https://github.com/gcontesini/DS_Lorenz_Attractor/blob/master/lorenz_attractor_rk1.png)

![x ts](https://github.com/gcontesini/DS_Lorenz_Attractor/blob/master/lorenz_system_x_ts.png)

![y ts](https://github.com/gcontesini/DS_Lorenz_Attractor/blob/master/lorenz_system_y_ts.png)

![z ts](https://github.com/gcontesini/DS_Lorenz_Attractor/blob/master/lorenz_system_z_ts.png)

![Lyapunov Exponent](https://github.com/gcontesini/DS_Lorenz_Attractor/blob/master/lorenz_system_lyapunov_exp.png)

With a lyapunov exponent of 0.892456 and a Lyapunov time of 1.12050 the system is deterministic and not stochastic.

## Taken's Theorem

Taken's theorem used with only the x ts. Here I make a lag of 10 time steps

This is black magic for sure!

![Takens Theorem with x ts](https://github.com/gcontesini/DS_Lorenz_Attractor/blob/master/lorenz_x_takens_theorem.png)

![Takens Theorem with y ts](https://github.com/gcontesini/DS_Lorenz_Attractor/blob/master/lorenz_y_takens_theorem.png)

![Takens Theorem with z ts](https://github.com/gcontesini/DS_Lorenz_Attractor/blob/master/lorenz_z_takens_theorem.png)
