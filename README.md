# Altair, my way

The `Stiles` theme for the [Altair visualization](https://altair-viz.github.io/) library in Python.

### Getting started

Install from PyPI.

```bash
$ pip install altair-stiles
```

Import with Altair.

```python
import altair as alt
import altair_stiles as altstiles
```

Register and enable the theme.

```python
alt.themes.register('stiles', altstiles.theme)
alt.themes.enable('stiles')
```

Make a chart.

```python
from vega_datasets import data
source = data.iowa_electricity()

alt.Chart(source, title="Iowa's renewable energy boom").mark_area().encode(
    x=alt.X(
        "year:T",
        title="Year"
    ),
    y=alt.Y(
        "net_generation:Q",
        stack="normalize",
        title="Share of net generation",
        axis=alt.Axis(format=".0%"),
    ),
    color=alt.Color(
        "source:N",
        legend=alt.Legend(title="Electricity source"),
    )
)
```

![example](./area.png)

### What else?

This library requires that you have the "Roboto" font installed. 