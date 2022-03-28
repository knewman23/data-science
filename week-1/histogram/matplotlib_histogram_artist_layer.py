import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

fig = Figure()
canvas = FigureCanvas(fig)

# create 10000 random numbers using np
x = np.random.randn(10000)

# create an axes artist
ax = fig.add_subplot(111)
ax.hist(x, 100)
ax.set_title("Normal distribution with $\mu=0, \sigma=1$")
fig.savefig("./images/matplotlib_histogram_artist_layer.png")
