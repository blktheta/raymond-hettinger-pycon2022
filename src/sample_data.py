""" Sample data for test application."""
from dataclasses import dataclass


@dataclass
class SampleData:
    """Example data for test application."""
    device_status: str = 'Status: connected'
    load_limits: bool = False
    load: int = 75
    dead_ports  = {12, 8, 15, 25}
    ports_in_use  = {18, 14, 6, 7, 20}
    allowed_ports = {2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22}

    def is_active(self, port: int) -> bool:
        """Predictate returning True if x is even.

        >>> s = SampleData()
        >>> s.is_active(port=8)
        True
        >>> s.is_active(port=7)
        False
        """
        return port % 2 == 0


if __name__ == '__main__':
    """
    Besides testing value, the benifit of incorporating examples in
    docstrings is speeding up the overall development process. It helps
    teach the readers how to user the tools/functions.

    Call the file with using the '-v' parameter for additional info.
    """
    import doctest

    print(doctest.testmod())
