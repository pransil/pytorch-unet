#data_test.py

import numpy as np
import matplotlib.pyplot as plt
import simulation2
import helper

def generate_and_plot_data(height, width, count):
    X, Y = simulation2.generate_random_data(16, 16, 2)
    print("X.shape=", X.shape)

    print("X[0].shape=", X[0].shape)

    print("X=[0,0:,0:]\n", X[0,0:,0:])
    print("shape.X=[0,0:,0:]\n", X[0,0:,0:].shape)

    # Plot each sample separately
    for i in range(len(X)):
        
        # Create a figure with two subplots side by side
        plt.figure(figsize=(10, 5))

        # Plot input image
        plt.subplot(1, 2, 1)
        plt.imshow(X[i])
        plt.title('Input Image')
        plt.axis('off')
        
        # Plot masks
        plt.show()


def generate_and_plot_track(x,y,increments,count):
    track = simulation2.generate_track(x,y,increments,count)

    print("track len=", len(track))
    print("track=", track)

    # plot the track[[x0,y0],[x1,y1],[x2,y2],...    ]
    x, y = zip(*track)
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    plt.plot(x, y)
    plt.title('Track (dx,dy)=(' + str(dx) + ',' + str(dy) + ')')    
    plt.show()
    
# Track increments. Could have just used 2 point in each for these simple cases.
t0 = [(0,0),(0,0),(0,0)]            # Does not move
t1 = [(1,1),(1,1),(1,1)]            # Up-right
t2 = [(1,0),(1,0),(1,0)]            # Right
t3 = [(0,1),(0,1),(0,1)]            # Up
t4 = [(1,-1),(1,-1),(1,-1)]         # Down-right
t5 = [(0,-1),(0,-1),(0,-1)]         # Down
t6 = [(-1,1),(-1,1),(-1,1)]        # Up-left
t7 = [(-1,0),(-1,0),(-1,0)]        # Left
t8 = [(-1,-1),(-1,-1),(-1,-1)]     # Down-left
    

t = [t0,t1,t2,t3,t4,t5,t6,t7,t8]
for i in range(len(t)):
    generate_and_plot_track(0,0,t[i],10)


