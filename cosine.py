#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import math


plot_nr = 0

def plot_numbers(numbers, dividers, nr_points, plot_points=False):
    
    # Plotting the numbers
    plt.figure(figsize=(8, 5))  # Optional: Adjust the figure size

    for i, n in enumerate(numbers):
        if dividers[i] == None:
            label = "cosine"
        else:
            label = f"div %d" % dividers[i]
            
        if plot_points:
            plt.plot(n[0:nr_points], marker="x", label=label)
        else:
            plt.plot(n[0:nr_points], label=label)
            
    
    # Adding titles and labels
    plt.title('Cosine approximation')
    #plt.xlabel('Index')
    #plt.ylabel('Value')
    
    # Adding a grid and legend
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Display the plot
    global plot_nr
    plt.savefig('cosine_plot_%d.png' % plot_nr, dpi=300, bbox_inches='tight')
    plot_nr += 1
    plt.show()


def cosine(divider, nr_points):
    
    sprevi  = 1000000
    sprev2i = 0
    
    cosine  = []

    cor         = sprevi
    prev_cor    = sprevi
    first_zero  = False
    
    for i in range(nr_points):
        prev_cor    = cor
        cor         = sprevi - sprev2i
    
        cosine.append(cor)
        #print(i, cor)

        if prev_cor >= 0 and cor <= 0 and first_zero == False:
            bits = int(round(math.log(divider)/math.log(2)))
            print("First zero crossing at %d" % (i-1))
            print(f"    divider points {divider} / zero crossing {i-1} = {divider/(i-1)}")
            print(f"    sqrt(divider points 2**{bits}) = { math.sqrt(divider) }")
            print(f"    sqrt(divider points 2**{bits}) / zero crossing {i-1} =  { math.sqrt(divider) / (i-1) }")
            first_zero  = True
        
        si      = 2*sprevi - sprev2i//divider - sprev2i
        sprev2i = sprevi
        sprevi  = si

    return cosine

nr_points = 8192

if True:
    c1  = cosine(4096, nr_points)
    c2  = cosine(8192, nr_points)
    c3  = cosine(16384, nr_points)

    x = np.linspace(0, 10.2 * 2 * np.pi, nr_points)  # 0 to 2π with 100 points
    cos1 = np.cos(x) * 1000000           # Apply cosine function

    plot_numbers([ c1, c2, c3 ], [ 4096, 8192, 16384 ], nr_points )
    
    plot_numbers([ c3, cos1 ], [ 16384, None ], nr_points )
    
    plot_numbers([ c3, cos1 ], [ 16384, None ], 1000 )

if True:
    c4  = cosine(128, 128)

    x = np.linspace(0, 128/72 * 2 * np.pi, 128)  # 0 to 2π with 100 points
    cos4 = np.cos(x) * 1000000           # Apply cosine function

    plot_numbers([ c4, cos4 ], [ 128, None ], 40, True )


if True:
    for i in range(4,24):
        c = cosine(2**i, 2**i)

