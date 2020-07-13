'''



'''
import numpy as np 

def main():

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC TIME

  max_time_int = 2e2
  time_step_float =  0.01
  time_interval_ary = np.arange( 0, max_time_int, time_step_float )

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC FILE

  out_file = open("ts_lorenz_system.dat","w")

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC INITIAL CONDITIONS 1

  x_aux_float = 1
  y_aux_float = 1
  z_aux_float = 1
  
  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC INITIAL CONDITIONS 2

  x_float = 1+1e-6
  y_float = 1+1e-6
  z_float = 1+1e-6
  

  out_file.write( str(x_float)+"\t"+str(y_float)+"\t"+str(z_float)+"\n"  )

  for time_float in time_interval_ary:

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC LYAPUNOV EXPONENT

    delta_x_rk4_float = x_float - x_aux_float
    delta_y_rk4_float = y_float - y_aux_float 
    delta_z_rk4_float = z_float - z_aux_float 

    delta_init_cond_float = np.log( np.sqrt( (delta_x_rk4_float*delta_x_rk4_float)+(delta_y_rk4_float*delta_y_rk4_float)+(delta_z_rk4_float*delta_z_rk4_float) ) )

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC OUTPUT

    out_file.write( str(time_float)+"\t"+str(x_float)+"\t"+str(y_float)+"\t"+str(z_float)+"\t"+str(delta_init_cond_float)+"\n"  )

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC LYAPUNOV

    k1x = lorentz_x( x_aux_float, y_aux_float )
    k1y = lorentz_y( x_aux_float, y_aux_float, z_aux_float )
    k1z = lorentz_z( x_aux_float, y_aux_float, z_aux_float )

    k2x = lorentz_x( x_aux_float+(time_step_float*k1x*0.5), y_aux_float )
    k2y = lorentz_y( x_aux_float, y_aux_float+(time_step_float*k1y*0.5), z_aux_float )
    k2z = lorentz_z( x_aux_float, y_aux_float, z_aux_float+(time_step_float*k1z*0.5) )

    k3x = lorentz_x( x_aux_float+(time_step_float*k2x*0.5), y_aux_float )
    k3y = lorentz_y( x_aux_float, y_aux_float+(time_step_float*k2y*0.5), z_aux_float )
    k3z = lorentz_z( x_aux_float, y_aux_float, z_aux_float+(time_step_float*k2z*0.5) )

    k4x = lorentz_x( x_aux_float+(time_step_float*k3x), y_aux_float )
    k4y = lorentz_y( x_aux_float, y_aux_float+(time_step_float*k3y), z_aux_float )
    k4z = lorentz_z( x_aux_float, y_aux_float, z_aux_float+(time_step_float*k3z) )

    x_aux_float += (time_step_float/6.0)*(k1x+(2.0*k2x)+(2.0*k3x)+k4x)
    y_aux_float += (time_step_float/6.0)*(k1y+(2.0*k2y)+(2.0*k3y)+k4y)
    z_aux_float += (time_step_float/6.0)*(k1z+(2.0*k2z)+(2.0*k3z)+k4z)

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC RK4

    k1x = lorentz_x( x_float, y_float )
    k1y = lorentz_y( x_float, y_float, z_float )
    k1z = lorentz_z( x_float, y_float, z_float )

    k2x = lorentz_x( x_float+(time_step_float*k1x*0.5), y_float )
    k2y = lorentz_y( x_float, y_float+(time_step_float*k1y*0.5), z_float )
    k2z = lorentz_z( x_float, y_float, z_float+(time_step_float*k1z*0.5) )

    k3x = lorentz_x( x_float+(time_step_float*k2x*0.5), y_float )
    k3y = lorentz_y( x_float, y_float+(time_step_float*k2y*0.5), z_float )
    k3z = lorentz_z( x_float, y_float, z_float+(time_step_float*k2z*0.5) )

    k4x = lorentz_x( x_float+(time_step_float*k3x), y_float )
    k4y = lorentz_y( x_float, y_float+(time_step_float*k3y), z_float )
    k4z = lorentz_z( x_float, y_float, z_float+(time_step_float*k3z) )

    x_float += (time_step_float/6.0)*(k1x+(2.0*k2x)+(2.0*k3x)+k4x)
    y_float += (time_step_float/6.0)*(k1y+(2.0*k2y)+(2.0*k3y)+k4y)
    z_float += (time_step_float/6.0)*(k1z+(2.0*k2z)+(2.0*k3z)+k4z)

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC EOF

  out_file.close()

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC LORENZ_SYTEM

def lorentz_x(
    x_float_,
    y_float_
  ):

  sigma_float = 10
  return sigma_float*( y_float_ - x_float_ )

def lorentz_y(
    x_float_,
    y_float_,
    z_float_
  ):

  rho_float = 28.
  return x_float_*( rho_float - z_float_) - y_float_

def lorentz_z(
    x_float_,
    y_float_,
    z_float_
  ):

  beta_float = 8./3.
  return (x_float_*y_float_ )- (beta_float*z_float_)


# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CALL MAIN

if __name__ == '__main__':
  main()