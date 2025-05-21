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


def generate_and_plot_track(x,y,steps,count):
    track = simulation2.generate_track(x,y,steps,count)

    print("track len=", len(track))
    print("track=", track)

    # plot the track[[x0,y0],[x1,y1],[x2,y2],...    ]
    x, y = zip(*track)
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    plt.plot(x, y)
    plt.title('Track (dx,dy)=(' + str(dx) + ',' + str(dy) + ')')    
    plt.show()
    return track

def generate_and_plot_image_sequence(track, height, width, x0, y0):
    # Generate the image sequence
    sequence = simulation2.generate_image_sequence(track, height, width, x0, y0)
    print("Sequence length:", len(sequence))
    
    # Plot the sequence
    n_images = len(sequence)
    fig, axes = plt.subplots(1, n_images, figsize=(n_images * 3, 3))
    if n_images == 1:
        axes = [axes]
    
    for i, img in enumerate(sequence):
        axes[i].imshow(img[0])  # img[0] because the image is in shape (1, height, width)
        axes[i].set_title(f'Frame {i}')
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.show()
    
# Track increments. Simplest cases where a single step is repeated.
def setup_steps():
    st0 = [(0,0),(0,0)]            # Does not move
    st1 = [(1,1),(1,1)]            # Up-right
    st2 = [(1,0),(1,0)]            # Right
    st3 = [(0,1),(0,1)]            # Up
    st4 = [(1,-1),(1,-1)]         # Down-right
    st5 = [(0,-1),(0,-1)]         # Down
    st6 = [(-1,1),(-1,1)]        # Up-left
    st7 = [(-1,0),(-1,0)]        # Left
    st8 = [(-1,-1),(-1,-1)]     # Down-left
    st = [st0,st1,st2,st3,st4,st5,st6,st7,st8]
    return st

# Test the track generation
steps = setup_steps()
for i in range(len(t)):
    generate_and_plot_track(0,0,t[i],10)

# Test the image sequence generation
# Generate a sequence using the up-right movement (t1)
generate_and_plot_image_sequence(steps[1], 18, 18, 8, 8)  # Start from center of 18x18 image


