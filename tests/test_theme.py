import altair as alt
import pytest

import altair_stiles


def test_config_is_valid_vega_lite():
    # Vega-Lite ignores unknown config keys, so a typo like "labelFontColor"
    # never errors at render time. Validating against the schema does.
    alt.Config.from_dict(altair_stiles.theme()["config"])


def test_registered_and_applied():
    assert "stiles" in alt.theme.names()
    previous = alt.theme.active
    altair_stiles.enable()
    try:
        spec = alt.Chart({"values": [{"a": 1}]}).mark_bar().encode(x="a:Q").to_dict()
    finally:
        alt.theme.enable(previous)
    assert spec["config"]["font"] == altair_stiles.FONT
    assert spec["config"]["bar"]["fill"] == altair_stiles.palette["default"]


def test_chart_settings_override_theme():
    with alt.theme.enable("stiles"):
        spec = (
            alt.Chart({"values": [{"a": 1}]})
            .mark_bar()
            .encode(x="a:Q")
            .configure_axis(labelColor="red")
            .to_dict()
        )
    assert spec["config"]["axis"]["labelColor"] == "red"
    assert spec["config"]["axis"]["labelFontSize"] == 12


@pytest.mark.parametrize("name", ["black", "white", "default", "accent", "highlight"])
def test_legacy_palette_keys(name):
    assert altair_stiles.palette[name].startswith("#")
