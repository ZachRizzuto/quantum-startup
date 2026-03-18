import pytest
from dash import Dash, html, dcc
import d
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def Tapp():
    Tapp = d.app
    return Tapp

def test_header(dash_duo, Tapp):
    dash_duo.start_server(Tapp)
    header = dash_duo.find_element("h1")
    assert header.text == "Sales Data"

def test_region_picker(dash_duo, Tapp):
    dash_duo.start_server(Tapp)
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker.is_displayed()

def test_graph(dash_duo, Tapp):
    dash_duo.start_server(Tapp)
    graph = dash_duo.find_element("#sales-graph")
    assert graph.is_displayed()

