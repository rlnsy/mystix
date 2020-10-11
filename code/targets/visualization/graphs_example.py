from code.targets.visualization.graphs import GraphManager
from threading import Thread
import time
from math import sin, pi
import numpy as np

MOCK_DATA_RESOLUTION = 1000
MOCK_DATA_SEED = [sin(t) for t in np.linspace(0, 2*pi, MOCK_DATA_RESOLUTION)]
mock_ptr = 0


def get_mock_data(count: int):
    data = []
    global mock_ptr
    for i in range(count):
        data.append(
            MOCK_DATA_SEED[
                (mock_ptr + i) % len(MOCK_DATA_SEED)])
    mock_ptr = mock_ptr + count
    return data


def run():
    gm = GraphManager()
    gm.add_plot("example_plot")

    def run_mock_logic():
        for i in range(50):
            gm.add_plot_data("example_plot", get_mock_data(40))
            time.sleep(0.1)

    logic = Thread(target=run_mock_logic)
    logic.start()

    gm.graphics.display()

    logic.join()
    gm.clean()
