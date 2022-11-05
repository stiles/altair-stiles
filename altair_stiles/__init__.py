"""
A stiles theme for Altair.
"""
# Color schemes and defaults
palette = dict(
    black="#333333",
    white="#ffffff",
    default="#1c9099",
    accent="#016c59",
    highlight="#00848b",
    democrat="#6baed6",
    republican="#fb6a4a",
    schemes={
        "category-5": [
            "#66c2a5",
            "#fc8d62",
            "#8da0cb",
            "#e78ac3",
            "#a6d854",
        ],
        "teal-7": [
            "#7ff6f6",
            "#00eeef",
            "#00d4d8",
            "#00abb2",
            "#00848b",
            "#fbf2c7",
            '#00363d',
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
    },
)


def theme():
    """
    A stiles theme for Altair.
    """
    # Headlines
    headlineFontSize = 17
    headlineFontWeight = "bold"
    headlineFont = "Roboto Bold"

    # Titles for axes and legends
    titleFont = "Roboto, sans"
    titleFontWeight = "normal"
    titleFontSize = 15
    titleFontColor = '#1a1a1a'

    # Labels for ticks and legend entries
    labelFont = "Roboto, sans"
    labelFontSize = 13
    labelFontWeight = "normal"
    labelFontColor = '#1a1a1a'
    titleFontColor = '#1a1a1a'

    return dict(
        config=dict(
            view=dict(width=700, height=400, strokeOpacity=0),
            background=palette["white"],
            title=dict(
                anchor="start",
                font=headlineFont,
                fontColor='palette["black"]',
                fontSize=headlineFontSize,
                fontWeight=headlineFontWeight,
            ),
            arc=dict(fill=palette["default"]),
            area=dict(fill=palette["default"]),
            line=dict(stroke=palette["default"], strokeWidth=3),
            path=dict(stroke=palette["default"]),
            rect=dict(fill=palette["default"]),
            shape=dict(stroke=palette["default"]),
            bar=dict(fill=palette["default"]),
            point=dict(stroke=palette["default"]),
            symbol=dict(fill=palette["default"], size=30),
            axis=dict(
                titleFont=titleFont,
                titleFontSize=titleFontSize,
                titleFontWeight=titleFontWeight,
                labelFont=labelFont,
                labelFontSize=labelFontSize,
                labelFontWeight=labelFontWeight,
            ),
            axisX=dict(labelAngle=0, labelPadding=6, tickSize=3, stiles=False),
            axisY=dict(
                labelBaseline="middle",
                maxExtent=45,
                minExtent=45,
                titleAlign="left",
                titleAngle=0,
                titleX=-45,
                titleY=-11,
                domainOpacity=0,
                stilesWidth=0.6,
                stilesColor="#dddddd",
                offset=6,
                tickSize=0,
                titleColor='#1a1a1a'
            ),
            legend=dict(
                titleFont=titleFont,
                titleFontSize=titleFontSize,
                titleFontWeight=titleFontWeight,
                symbolType="square",
                labelFont=labelFont,
                labelFontSize=labelFontSize,
            ),
            range=dict(
                category=palette["schemes"]["category-5"],
                diverging=palette["schemes"]["cb-diverging-purpgrn"],
                heatmap=palette["schemes"]["teal-7"],
                ordinal=palette["schemes"]["category-5"],
                ramp=palette["schemes"]["teal-7"],
            ),
        )
    )