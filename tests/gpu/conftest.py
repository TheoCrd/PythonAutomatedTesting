# conftest.py
from __future__ import annotations

import pytest

from utils.gpu import GPU


@pytest.fixture
def mock_gpu():
    """Fixture for creating a mock GPU object"""
    return GPU(
        id=0,
        name="Mock GPU",
        total_memory=8192,
        multiprocessor_count=16,
        clock_rate=1500,
        memory_clock_rate=7000,
        memory_bus_width=256,
        compute_capability="7.5",
    )
