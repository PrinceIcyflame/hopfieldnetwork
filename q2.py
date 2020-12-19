# BT6270 Assignment 3
# NIVETHITHAN M BE17B023
# DATED: 13/12/2020

### Q2
### Plot Recall of Hopfield Network of ball.txt

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import imageio
import numpy as np

# Text file of the Ball Image
textfile = 'ball.txt'

# Matrix dimensions
w, h = 90, 100
# Time step
dt = 0.05
# Lambda value
l = 5
# No of time steps
n = 300

# To convert the given text file to a Matrix
def converttomatrix(textfile):
  data = []
  i = 1
  with open(textfile) as lines:
    i += 1
    for line in lines:
      line = line.split(',')
      for element in line:
        if(element == '-1' or element == '-1\n'):
          data.append(-1)
        elif(element == '1' or element == '1\n'):
          data.append(1)
        else:
          data.append(1)
  mat = np.array(data).reshape(w, h)
  return mat

# Empty set initialization for U & V values
U = {}
V = {}
ims = []
rms = []

# Hopfield network implementation
def hopfield(data):  
  S = np.array(data).reshape(9000,1)
  W = np.dot(S,S.T)/(w*h)
  U[0] = np.zeros(shape=(90,100))
  # Patch from 10:35, 40:75 selected for expt
  U[0][10:35,40:75] = data[10:35,40:75]
  plt.imsave("patch" + '.png', U[0], cmap=cm.gray)
  U[0] = U[0].reshape(9000,1)
  V[0] = np.zeros(shape=(9000,1))

  for i in range(300) :
      val = np.square(np.subtract(S,V[i]))
      print('Iteration number: ' + str(i+1))
      print('RMS: ' + str(np.sqrt(np.sum(val)/(w*h))))
      # Calculate rms value
      # RMS = SquareRoot(Sigma(Square(Neural_Network[i] - Pattern[i])))
      rms.append(np.sqrt(np.sum(val)/(w*h)))
      im = np.array(V[i]).reshape(w,h)
      plt.imshow(np.array(V[i]).reshape(w,h), cmap=cm.gray)
      ims.append(im)
      plt.show()
      # du/dt = -u + w*V[i]
      # V[i] = tanh(Lambda*u(i))
      dU = (-U[i]+np.dot(W,V[i]))*dt
      U[i+1] = U[i] + dU
      V[i+1] = np.tanh(l*U[i+1])


mat = converttomatrix(textfile)
data = mat

hopfield(data)
imageio.mimwrite('output.gif', ims, fps=1)

# Saved gif file of output
plt.show()

# Plot RMS
num = []
for i in range(n):
  num.append(i)
rms_plot = plt.plot(num,rms, marker = 'o', )
plt.savefig('rms_plot.png')
