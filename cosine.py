#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import math


plot_nr = 0

def plot_numbers(numbers, dividers, nr_points, plot_points=False):
    
    # Plotting the numbers
    plt.figure(figsize=(8, 5))  # Optional: Adjust the figure size

    for i, n in enumerate(numbers):
        label = dividers[i]
            
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
    
    cosine  = np.empty(nr_points)

    cor         = sprevi
    prev_cor    = sprevi
    first_zero  = False
    
    for i in range(nr_points):
        prev_cor    = cor
        cor         = sprevi - sprev2i
    
        cosine[i] = cor
        #print(i, cor)

        if prev_cor >= 0 and cor <= 0 and first_zero == False:
            bits = int(round(math.log(divider)/math.log(2)))
            #print("First zero crossing at %d" % (i-1))
            #print(f"    divider points {divider} / zero crossing {i-1} = {divider/(i-1)}")
            #print(f"    sqrt(divider points 2**{bits}) = { math.sqrt(divider) }")
            #print(f"    sqrt(divider points 2**{bits}) / zero crossing {i-1} =  { math.sqrt(divider) / (i-1) }")
            first_zero  = True

            sqrt_div_div_points = round(math.sqrt(divider) / (i-1), 4)
            print(f" | {bits} | { 2**bits } | {i-1} | { sqrt_div_div_points } |")
        
        si      = 2*sprevi - sprev2i//divider - sprev2i
        sprev2i = sprevi
        sprevi  = si

    return cosine

nr_points = 8192

if True:
    c1  = cosine(4096, nr_points)
    c2  = cosine(8192, nr_points)
    c3  = cosine(16384, nr_points)

    plot_numbers([ c1, c2, c3 ], [ 4096, 8192, 16384 ], nr_points )

    x = np.linspace(0, 10.2 * 2 * np.pi, nr_points)
    cos3 = np.cos(x) * 1000000           # Apply cosine function

    diff3 = cos3 - c3
    
    plot_numbers([ c3, cos3, diff3 ], [ 16384, "cos", "error" ], nr_points )
    
    plot_numbers([ c3, cos3, diff3 ], [ 16384, "cos", "error" ], 1000 )

    max_error_first_q = np.max(np.abs(diff3[0:201]))
    print("Abs max error in first quadrant: %d" % max_error_first_q)
    print("Rel max error over amplitidue in first quadrant: %f%%" % ((max_error_first_q/1000000)*100) )

    inst_rel_max_error_first_q = np.max( np.abs(diff3[0:201]) / cos3[0:201] )
    print("Instantaneous rel max error in first quadrant: %f%%" % (inst_rel_max_error_first_q * 100) )


if True:
    c4  = cosine(128, 128)

    x = np.linspace(0, 128/72 * 2 * np.pi, 128)  # 0 to 2π with 100 points
    cos4 = np.cos(x) * 1000000           # Apply cosine function

    diff4 = cos4 - c4

    plot_numbers([ c4, cos4, diff4 ], [ 128, "cos", "error" ], 40, True )

    max_error_first_q = np.max(np.abs(diff4[0:17]))
    print("Abs max error in first quadrant: %d" % max_error_first_q)
    print("Rel max error over amplitidue in first quadrant: %f%%" % ((max_error_first_q/1000000)*100) )


if True:
    for i in range(4,24):
        c = cosine(2**i, 2**i)

