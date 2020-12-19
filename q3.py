# BT6270 Assignment 3
# NIVETHITHAN M BE17B023
# DATED: 13/12/2020

# Q3 Part A,B

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import imageio

w, h = 90, 100
dt = 0.05
l = 5
n = 300

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

### Uncomment data and filename variables of the required text file and comment the others

textfile = "ball.txt"
mat = converttomatrix(textfile)
#data = mat
#filename = 'ball'
S_ball = np.array(mat).reshape(9000,1)
W_ball = np.dot(S_ball,S_ball.T)/(w*h)

textfile = "cat.txt"
mat = converttomatrix(textfile)
#data = mat
#filename = 'cat'
S_cat = np.array(mat).reshape(9000,1)
W_cat = np.dot(S_cat,S_cat.T)/(w*h)

textfile = "mona.txt"
mat = converttomatrix(textfile)
data = mat
filename = 'mona'
S_mona = np.array(mat).reshape(9000,1)
W_mona = np.dot(S_mona,S_mona.T)/(w*h)

W = W_ball+W_cat+W_mona

U = {}
V = {}
rms = []
ims = []

def hopfield(data):  
  S = np.array(data).reshape(9000,1)
  U[0] = np.zeros(shape=(90,100))
  U[0][10:35,40:75] = data[10:35,40:75]
  plt.imsave(str(filename)+"_patch" + '.png', U[0], cmap=cm.gray)
  U[0] = U[0].reshape(9000,1)
  V[0] = np.zeros(shape=(9000,1))
  for i in range(300) :
      val = np.square(np.subtract(S,V[i]))
      print('Iteration number: ' + str(i+1))
      print('RMS: ' + str(np.sqrt(np.sum(val)/(w*h))))
      rms.append(np.sqrt(np.sum(val)/(w*h)))
      im = np.array(V[i]).reshape(w,h)
      plt.imshow(np.array(V[i]).reshape(w,h), cmap=cm.gray)
      ims.append(im)
      plt.show()
      dU = (-U[i]+np.dot(W,V[i]))*dt
      U[i+1] = U[i] + dU
      V[i+1] = np.tanh(l*U[i+1])

hopfield(data)
imageio.mimwrite('output_'+ str(filename) +'.gif', ims, fps=1)

# Plot RMS
num = []
for i in range(n):
  num.append(i)
rms_plot = plt.plot(num,rms, marker = 'o', )
plt.savefig('rms_plot.png')
