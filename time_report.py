from dataclasses import dataclass


@dataclass
class TimeReport:
    cores: int
    time: float
    version_name: str
    base_python_time: float

    @property
    def speedup(self):
        return self.base_python_time / self.time
