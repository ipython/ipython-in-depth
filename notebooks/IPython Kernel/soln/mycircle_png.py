ip = get_ipython()
png_f = ip.display_formatter.formatters['image/png']
png_f.for_type(MyCircle, circle_to_png)