import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot, cm
from matplotlib.colors import Normalize

def equation_of_motion(u, v, dx, dy, NU, dt):
   uorg = u.copy()
   vorg = v.copy()
   u[1:-1, 1:-1] = (uorg[1:-1, 1:-1] - 
                           dt/dx * uorg[1:-1, 1:-1] * (uorg[1:-1, 1:-1] - uorg[1:-1, 0:-2]) - 
                           dt/dy * vorg[1:-1, 1:-1] * (uorg[1:-1, 1:-1] - uorg[0:-2, 1:-1]) + 
                           NU * dt/dx**2 * (uorg[1:-1, 2:] - 2*uorg[1:-1, 1:-1] + uorg[1:-1, 0:-2]) +
                           NU * dt/dy**2 * (uorg[2:, 1:-1] - 2*uorg[1:-1, 1:-1] + uorg[0:-2, 1:-1]))

   v[1:-1, 1:-1] = (vorg[1:-1, 1:-1] - 
                           dt/dx * uorg[1:-1, 1:-1] * (vorg[1:-1, 1:-1] - vorg[1:-1, 0:-2]) - 
                           dt/dy * vorg[1:-1, 1:-1] * (vorg[1:-1, 1:-1] - vorg[0:-2, 1:-1]) + 
                           NU * dt/dx**2 * (vorg[1:-1, 2:] - 2*vorg[1:-1, 1:-1] + vorg[1:-1, 0:-2]) +
                           NU * dt/dy**2 * (vorg[2:, 1:-1] - 2*vorg[1:-1, 1:-1] + vorg[0:-2, 1:-1]))

   v[1:-1, 1:-1] = (vorg[1:-1, 1:-1] - 
                           dt/dx * uorg[1:-1, 1:-1] * (vorg[1:-1, 1:-1] - vorg[1:-1, 0:-2]) -
                           dt/dy * vorg[1:-1, 1:-1] * (vorg[1:-1, 1:-1] - vorg[0:-2, 1:-1]) + 
                           NU * dt/dx**2 * (vorg[1:-1, 2:] - 2*vorg[1:-1, 1:-1] + vorg[1:-1, 0:-2]) +
                           NU * dt/dy**2 * (vorg[2:, 1:-1] - 2*vorg[1:-1, 1:-1] + vorg[0:-2, 1:-1]))

   # v = u.copy()

   return (u, v)


def boundary(u, v, nozzle_u, nozzle_v, nx, ny, t_step):
   u[0, :] = 0
   u[-1, :] = 0
   u[:, 0] = 0
   u[:, -1] = 0

   v[0, :] = 0
   v[-1, :] = 0
   v[:, 0] = 0
   v[:, -1] = 0

   # Nozzle BC
   u[ny//2-2:ny//2+2, 0] = nozzle_u[t_step]
   v[ny//2-2:ny//2+2, 0] = nozzle_v[t_step]

   return (u, v)

def evolve(u, v, dx, dy, nx, ny, NU, dt, noz_x, noz_y, passes, steps):
   for i in range(steps):
      (u, v) = equation_of_motion(u, v, dx, dy, NU, dt)
      (u, v) = boundary(u, v, noz_x, noz_y, nx, ny, i+passes)
   return (u, v)

def main():
   # Lx = Ly = 2
   nx = ny = 41
   dx = 2 / float(nx - 1)
   dy = 2 / float(ny - 1)
   # u = np.ones((ny, nx))
   # v = np.ones((ny, nx))

   SIGMA = 0.001
   NU = 0.01
   dt = SIGMA * dx * dy / NU

   nt = 2510

   # Get initial
   u = np.zeros((nx, ny))
   v = np.zeros((nx, ny))

   # Set nozzle
   nozzle_u = np.append(10*np.ones(1000), np.zeros(nt))
   nozzle_v = np.append(10*np.ones(1000), np.zeros(nt))
   
   for i in range(0, nt, 50):
      (u, v) = evolve(u, v, dx, dy, nx, ny, NU, dt, nozzle_u, nozzle_v, i, 50)
      ax = pyplot.figure()
      norm = Normalize()
      magnitude = np.sqrt(u[::2]**2 + v[::2]**2)
      pyplot.quiver(u[::2], v[::2], norm(magnitude), scale=60, cmap=pyplot.get_cmap("jet"))
      ax.savefig('frame'+str(i).zfill(5)+'.png', dpi=300)
      ax.clear()

main()