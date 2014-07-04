def plot_iris(a=None, col1=0, col2=0):
    plt.scatter(a[:,col1], a[:,col2])

interact(plot_iris, a=fixed(iris_data.data), col1=(0,3), col2=(0,3));