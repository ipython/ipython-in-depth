@interact(a=(0.0,5.0,0.1), b=(-5.0,5.0,0.1),
         style={'dotted red': 'r.', 'dashed black': 'k--'})
def plot_sin2(a, b, style='r.'):
    x = np.linspace(0,4*np.pi, 100)
    y = np.sin(a*x+b)
    plt.plot(x, y, style)