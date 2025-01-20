
# Cosine Approximation

[cnohr](https://bsky.app/profile/cnlohr.bsky.social) posted this interesting
cosine and sine approximation function on [Bluesky](https://bsky.app/profile/cnlohr.bsky.social/post/3lg5e3c7ifc26).

![Cosine approximation function](cosine_approximation_function.jpg)

The original code has a `>>13` or divide by 8192 term that determines the number of
points in one period.

I reimplemented the function in Python to have a closer look at the behavior.

Here's what happens when you use different dividers:

![Plots for divider numberes 4096, 8192, 16384](cosine_plot_0.png)

