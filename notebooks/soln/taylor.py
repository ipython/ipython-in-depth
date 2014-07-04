# For an expression made from elementary functions, we must first make it into
# a callable function, the simplest way is to use the Python lambda construct.
plot_taylor_approximations(lambda x: 1/cos(x), 0, [2,4,6], (0, 2*pi), (-5,5))