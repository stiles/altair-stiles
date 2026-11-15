"""Matt Stiles' chart theme for Altair.

Usage::

    import altair as alt
    import altair_stiles

    alt.theme.enable("stiles")

How a theme works
-----------------
An Altair chart is a Python object that serializes to a Vega-Lite JSON spec.
``alt.Chart(df).mark_bar().encode(x="a", y="b")`` becomes
``{"data": ..., "mark": "bar", "encoding": {"x": ..., "y": ...}}``.

Vega-Lite specs have one more top-level key, ``config``, which holds defaults
for everything the chart did not set itself: fonts, colors, axis styling and
so on. A theme is a function that returns ``{"config": {...}}``. Altair merges
that dict into every chart it renders. Anything set on a chart directly
(``alt.Axis(labelColor=...)``, ``.configure_axis(...)``) wins over the theme.

The keys inside ``config`` are Vega-Lite's, in camelCase, and are documented at
https://vega.github.io/vega-lite/docs/config.html. Vega-Lite ignores keys it
does not recognize, so a typo fails silently. ``tests/test_theme.py`` validates
this theme against the Vega-Lite schema to catch that.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

import altair as alt

try:
    __version__ = version("altair-stiles")
except PackageNotFoundError:  # running from a source checkout
    __version__ = "0.0.0"

__all__ = ["FONT", "FONT_DIR", "enable", "palette", "theme"]

# A CSS-style font stack. Charts in a notebook or web page are drawn by the
# browser, which uses the first of these fonts it can find.
FONT = "Inter, Roboto, Helvetica Neue, Arial, sans-serif"

# chart.save("chart.png") is drawn by vl-convert instead, which has two quirks:
# it draws no text at all when it finds none of the fonts, and it ignores
# weights in variable fonts, so bold and light come out regular. The package
# ships four static Inter weights (300, 400, 500, 700) to cover both.
FONT_DIR = Path(__file__).parent / "fonts"

try:
    import vl_convert

    vl_convert.register_font_directory(str(FONT_DIR))
except ImportError:  # vl-convert is optional; only static export needs it
    pass

palette = dict(
    # Text and chrome
    text="#262626",
    muted="#8e8e8e",  # source lines, notes
    axis="#A6A6A6",  # axis tick labels
    grid="#B1B1B1",
    baseline="#6e6e6e",
    background="#FEFEFE",
    # Marks
    default="#5194C3",
    accent="#F18851",
    highlight="#F18851",
    democrat="#5194C3",
    republican="#C52622",
    # Kept from 0.0.x so old code that looks these up still runs
    black="#262626",
    white="#FEFEFE",
    schemes={
        "category-6": [
            "#5194C3",  # blue
            "#F8C153",  # yellow
            "#C52622",  # red
            "#53A796",  # teal
            "#F18851",  # orange
            "#7C4EA5",  # purple
        ],
        # ColorBrewer Blues
        "blues-7": [
            "#eff3ff",
            "#c6dbef",
            "#9ecae1",
            "#6baed6",
            "#4292c6",
            "#2171b5",
            "#084594",
        ],
        # ColorBrewer RdBu, reversed so low is blue and high is red
        "rdbu-7": [
            "#2166ac",
            "#67a9cf",
            "#d1e5f0",
            "#f7f7f7",
            "#fddbc7",
            "#ef8a62",
            "#b2182b",
        ],
        # Schemes from 0.0.x. Not used by the theme, available by name.
        "category-5": ["#64938B", "#d95f02", "#7570b3", "#e7298a", "#66a61e"],
        "teal-7": [
            "#C7EAE5",
            "#A6CDC7",
            "#85B0A9",
            "#64938B",
            "#42766C",
            "#21594E",
            "#003C30",
        ],
        "fireandice-6": [
            "#e68a4f",
            "#f4bb6a",
            "#f9e39c",
            "#dadfe2",
            "#a6b7c6",
            "#849eae",
        ],
        "ice-7": [
            "#edefee",
            "#dadfe2",
            "#c4ccd2",
            "#a6b7c6",
            "#849eae",
            "#607785",
            "#47525d",
        ],
        "cb-diverging-purpgrn": [
            "#762a83",
            "#af8dc3",
            "#e7d4e8",
            "#f7f7f7",
            "#d9f0d3",
            "#7fbf7b",
            "#1b7837",
        ],
        "cb-diverging-bluegreen": [
            "#8c510a",
            "#d8b365",
            "#f6e8c3",
            "#f5f5f5",
            "#c7eae5",
            "#5ab4ac",
            "#01665e",
        ],
    },
)


def theme() -> alt.theme.ThemeConfig:
    """Return the Vega-Lite config for the stiles theme."""
    p = palette
    schemes = p["schemes"]
    fill = {"fill": p["default"]}
    stroke = {"stroke": p["default"]}

    return {
        "config": {
            # Top level: applies to the whole chart
            "font": FONT,
            "background": p["background"],
            "padding": 12,
            # view = the plotting rectangle inside the axes. The size here is
            # for continuous scales; band scales size themselves per category.
            "view": {
                "continuousWidth": 650,
                "continuousHeight": 400,
                "stroke": "transparent",
            },
            # title = alt.Chart(df, title=...) or alt.Title("...", subtitle=...)
            "title": {
                "anchor": "start",
                "color": p["text"],
                "fontSize": 18,
                "fontWeight": "bold",
                "subtitleColor": p["text"],
                "subtitleFontSize": 15,
                "subtitleFontWeight": 300,
                "subtitlePadding": 6,
                "offset": 16,
            },
            # One block per mark type: defaults for mark_bar(), mark_line() etc.
            # Filled marks take "fill", stroked marks take "stroke".
            "arc": fill,
            "area": fill,
            "bar": fill,
            "rect": fill,
            "circle": {**fill, "size": 60},
            "square": {**fill, "size": 60},
            "point": {**fill, "filled": True, "size": 60},
            "geoshape": {**fill, "stroke": "#FFFFFF", "strokeWidth": 0.5},
            "line": {**stroke, "strokeWidth": 2.5, "strokeCap": "round"},
            "trail": fill,
            "tick": {"color": p["default"]},
            "rule": {"color": p["baseline"], "strokeWidth": 0.5},
            "text": {"color": p["text"], "fontSize": 12},
            # axis = both axes. axisX and axisY override it per direction, and
            # there are narrower blocks still (axisYQuantitative, axisXTemporal).
            "axis": {
                "labelColor": p["axis"],
                "labelFontSize": 12,
                "labelFontWeight": 300,
                "labelPadding": 6,
                "titleColor": p["text"],
                "titleFontSize": 12,
                "titleFontWeight": 500,
                "titlePadding": 10,
                "gridColor": p["grid"],
                "gridWidth": 0.5,
                "domainColor": p["baseline"],
                "domainWidth": 0.5,
                "tickColor": p["baseline"],
                "tickWidth": 0.5,
            },
            "axisX": {
                "grid": False,
                "labelAngle": 0,
                "tickSize": 4,
            },
            "axisY": {
                "domain": False,
                "ticks": False,
                "labelPadding": 8,
            },
            "axisQuantitative": {"tickCount": 5},
            "legend": {
                "orient": "top",
                "labelColor": p["text"],
                "labelFontSize": 12,
                "labelFontWeight": 300,
                "titleColor": p["text"],
                "titleFontSize": 12,
                "titleFontWeight": 500,
                "symbolSize": 100,
                "gradientLength": 200,
                "gradientThickness": 10,
            },
            # header = facet labels, from .facet() or row=/column= encodings
            "header": {
                "labelColor": p["text"],
                "labelFontSize": 12,
                "labelFontWeight": 500,
                "titleColor": p["text"],
                "titleFontSize": 12,
                "titleFontWeight": 500,
            },
            # range = the default colors a color scale maps data onto, by
            # data type: category for :N, ordinal for :O, ramp for :Q.
            "range": {
                "category": schemes["category-6"],
                "ordinal": schemes["blues-7"],
                "ramp": schemes["blues-7"],
                "heatmap": schemes["blues-7"],
                "diverging": schemes["rdbu-7"],
            },
        }
    }


# Importing the package registers the theme under the name "stiles".
alt.theme.register("stiles", enable=False)(theme)


def enable() -> None:
    """Enable the theme. Same as ``alt.theme.enable("stiles")``."""
    alt.theme.enable("stiles")
