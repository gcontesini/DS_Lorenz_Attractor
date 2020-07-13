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

![original Lorenza attractor]()

![x ts]()

![y ts]()

![z ts]()

![Lyapunov Exponent]()

With a lyapunov exponent of 0.892456 and a Lyapunov time of 1.12050 the system is deterministic and not stochastic.

## Taken's Theorem

Taken's theorem used with only the x ts. Here I make a lag of 10 time steps

This is black magic for sure!

![Reconstruction of the Lorenz attractor based on taken's theorem]()
