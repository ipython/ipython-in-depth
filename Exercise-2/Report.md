## Attached markdown document to a console. 


Right-click somewhere on this document and click `"Create console for editor"`.
You will be prompted to select a kernel (new or existing). 

Now that this is done, the current or _fenced block_,  _selection_ or _line_ will be sent to the console and executed.

# Iris dataset

Let's learn some Pandas. First import `pandas`, it is common to alias to the shorter name `pd`. 

```
import pandas as pd
```

Pandas provides some nice utilities function to load csv datasets:

```
df = pd.read_csv('../data/iris.csv')
```

enable inline plotting with `%matplotlib` magic function:

```
%matplotlib inline
```

```
df.plot.scatter('sepal_width', 'sepal_length')
```

# Categorical
```
%load_ext autoreload
%autoreload 1
%aimport lib
```

```
df = pd.read_csv('../data/iris.csv')
lib.categorify(df, 'species')
df.plot.scatter('sepal_width', 'sepal_length', c='species', colormap='viridis')
```