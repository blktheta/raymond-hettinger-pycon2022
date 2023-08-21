""" Test for sample data showcasing test tools and techniques.

    Tools used:
        Doctest:
        Pytest: superior tool than statndard unittest.
        Coverage: know what code have yet to be tested.
        Pyflakes: least noisy linter
        Hypothesis: helpful in generating cases.
"""
import re
import pytest
from hypothesis import given, strategies as st
from src.sample_data import SampleData

# Arrange
@pytest.fixture
def sample_data():
    return SampleData()


def test_load(sample_data):
    # Act
    load = sample_data.load
    category = 'heavy' if load >= 70 else 'light'

    # Assert
    assert category == 'heavy'
    assert sample_data.load_limits or load >= 50
    assert isinstance(load, int) and 0 <= load <= 100
    assert load in {55, 65, 75, 85, 95}


def test_verify(sample_data):
    # Act
    device_status = sample_data.device_status

    # Assert
    assert 'connected' in device_status.split()
    assert re.search(r'[Ss]tatus: [Cc]onnected', device_status)


def test_ports(sample_data):
    # Act
    ports_in_use = sample_data.ports_in_use
    dead_ports = sample_data.dead_ports

    # Assert
    assert dead_ports.isdisjoint(ports_in_use)              # No dead ports
    assert any(map(sample_data.is_active, ports_in_use))    # One port in use
    assert all(port < 1024 for port in ports_in_use)        # Ports under 1024
    assert ports_in_use <= sample_data.allowed_ports         # Ports allowed


@given(port = st.integers(min_value=1, max_value=1024).filter(lambda x: x % 2 == 0))
def test_is_active(port):
    # Act
    s  = SampleData()

    # Assert
    assert s.is_active(port)


if __name__ == '__main__':

    pytest.main()
