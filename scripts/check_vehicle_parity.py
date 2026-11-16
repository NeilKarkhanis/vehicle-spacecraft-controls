import csv
import math
from pathlib import Path
import subprocess
import sys

from vehicle.model import Vehicle


def check_parity(executable):
    output = subprocess.check_output([executable], text=True)
    rows = list(csv.DictReader(output.splitlines()))
    scenarios = {
        "ideal": Vehicle(1600.0),
        "realistic": Vehicle(
            1600.0, drag_coefficient=0.28, rolling_resistance_coefficient=0.01
        ),
    }

    names = [row.get("scenario") for row in rows]
    if sorted(names, key=str) != sorted(scenarios):
        raise SystemExit(f"Expected one row per scenario, got {names!r}")

    for row in rows:
        name = row["scenario"]
        vehicle = scenarios[name]
        for _ in range(3000):
            vehicle.update(4000.0, 0.01)

        for column, expected in (
            ("velocity_m_s", vehicle.velocity),
            ("position_m", vehicle.position),
        ):
            actual = float(row[column])
            if not math.isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-12):
                raise SystemExit(
                    f"{name} {column}: C++ returned {actual!r}, Python returned {expected!r}"
                )


if __name__ == "__main__":
    check_parity(Path(sys.argv[1]).resolve())
