"""
health_score.py

Simple device health score calculator.

Score range: 0-100
"""

from dataclasses import dataclass


@dataclass
class DeviceState:
    battery_percent: int
    network_available: bool
    free_storage_gb: float
    gps_enabled: bool


def calculate_health_score(device: DeviceState) -> dict:
    score = 100
    issues = []

    # Battery
    if device.battery_percent < 10:
        score -= 30
        issues.append("Critical battery level")
    elif device.battery_percent < 20:
     
