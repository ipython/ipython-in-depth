ip = get_ipython()
png_f = ip.display_formatter.formatters['image/png']
png_f.for_type(np.ndarray, ndarray_to_png)