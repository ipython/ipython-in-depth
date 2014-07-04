def plot_sin(a, b):
    x = np.linspace(0,4*np.pi, 100)
    y = np.sin(a*x+b)
    plt.plot(x,y)

interact(plot_sin, a=(0.0,5.0,0.1), b=(-5.0,5.0,0.1));