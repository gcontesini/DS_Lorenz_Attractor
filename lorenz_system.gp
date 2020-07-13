
# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC START
reset

set terminal png

data_pnt="ts_lorenz_system.dat"

# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC STATS

do for [COL=1:4] {stats data_pnt u COL name sprintf("stats_%d",COL) nooutput}

# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC SINGLE TS

set view 55,296,1,1
set mapping cartesian
set grid 
set output "lorenz_system_attractor.png"
set label 1 "" at sprintf("%f %f %f",stats_2_mean, stats_3_mean, stats_4_mean) point pt 7 lw 1.5
splot data_pnt u 2:3:4 notitle w l

reset

set grid 
set yrange[-30:40]
set arrow 5 from 160, stats_2_mean to 160, stats_2_min 
set label 5 at 160, stats_2_min-1.5 sprintf("%f",stats_2_mean) center
plot data_pnt u 1:2 notitle w l
replot stats_2_mean lt rgb "black" title "mean" 
set output "lorenz_system_x_ts.png"
replot

reset

set grid 
set yrange[-30:30]
set arrow 5 from 155, stats_3_mean to 155, stats_3_min
set label 5 at 155, stats_3_min-1.5 sprintf("%f",stats_3_mean) center 
plot data_pnt u 1:3 notitle w l
replot stats_3_mean lt rgb "black"  title "mean"
set output "lorenz_system_y_ts.png"
replot

reset

set grid 
set yrange[-5:140]
set arrow 5 from 160, stats_4_mean to 160, stats_4_max-10
set label 5 at 160, stats_4_max+2-10 sprintf("%f",stats_4_mean) center 
set yrange[-2:140]
plot data_pnt u 1:4 notitle w l
replot stats_4_mean lt rgb "black"  title "mean"
set output "lorenz_system_z_ts.png"
replot

reset

set grid
# set xrange[0:1]
set yrange[-14:5]
# set yrange [1e-3:1e2]
f(x) = a*x+b
fit[0:20] f(x) data_pnt u 1:5 via a,b
a               = 0.892456
b               = -12.7598
plot[1:50] data_pnt u 1:5 notitle w l
replot[0:20] f(x) lt rgb "black" lw 2 title "L_{exp} = 0.892456"
set output "lorenz_system_lyapunov_exp.png"
replot

reset

# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC TAKENS THEOREM

reset

takens_x_data_pnt = "takens_x_data_pnt.dat"
set grid
set view 64, 352, 0.902, 1.43333
splot takens_x_data_pnt u 2:3:4 w l title "x ts"
set output "lorenz_x_takens_theorem.png"
replot 

takens_y_data_pnt = "takens_y_data_pnt.dat"
set grid
set view 55, 34, 0.902, 1.43333
splot takens_y_data_pnt u 2:3:4 w l title "y ts"
set output "lorenz_y_takens_theorem.png"
replot 

takens_z_data_pnt = "takens_z_data_pnt.dat"
set grid
set view 59, 76, 0.902, 1.43333
splot takens_z_data_pnt u 2:3:4 w l title "z ts"
set output "lorenz_z_takens_theorem.png"

replot

# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC MULTIPLOT

reset

set autoscale
set output "lorenz_system_rk4.png"
set multiplot

set size 0.5, 0.5 
set origin 0, 0
splot data_pnt u 2:3:4 notitle w l
set origin 0, 0.5
# set xrange[0:50]
# set yrange[-20:30]
plot data_pnt u 1:2 w l title "x ts"
set origin 0.5, 0 
# set yrange[-30:40]
plot data_pnt u 1:3 w l title "y ts"
set origin 0.5, 0.5
# set yrange[0:60]
plot data_pnt u 1:4 w l title "z ts"

reset
# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC END