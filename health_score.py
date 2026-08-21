"""
health_score.py

Device Health Score Engine

Calculates:
- Health Score (0-100)
- Status
- Grade
- Risk Level
- Detected Issues
- Recommendations
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class DeviceState:
    battery_percent: int
    network_available: bool
    free_storage_gb: float
    gps_enabled: bool


def get_health_grade(score: int) -> str:
    if score >= 90:
        return "A"

    if score >= 80:
        return "B"

    if score >= 70:
        return "C"

    if score >= 60:
        return "D"

    return "F"


def get_risk_level(score: int) -> str:
    """
    Determines operational risk based on score.
    """

    if score >= 90:
        return "LOW"

    if score >= 70:
        return "MEDIUM"

    if score >= 50:
        return "HIGH"

    return "CRITICAL"


def get_recommendations(issues):
    mapping = {
        "Critical battery level": "Charge the device immediately.",
        "Low battery level": "Consider charging the device soon.",
        "Network unavailable": "Verify Wi-Fi or cellular connection.",
        "Critical storage space": "Remove unnecessary files.",
        "Low storage space": "Free additional storage space.",
        "GPS disabled": "Enable location services."
    }

    recommendations = []

    for issue in issues:
        if issue in mapping:
            recommendations.append(mapping[issue])

    return recommendations


def calculate_health_score(device: DeviceState) -> dict:

    score = 100
    issues = []

    # Battery
    if device.battery_percent < 10:
        score -= 30
        issues.append("Critical battery level")

    elif device.battery_percent < 20:
        score -= 15
        issues.append("Low battery level")

    # Network
    if not device.network_available:
        score -= 20
        issues.append("Network unavailable")

    # Storage
    if device.free_storage_gb < 2:
        score -= 25
        issues.append("Critical storage space")

    elif device.free_storage_gb < 5:
        score -= 10
        issues.append("Low storage space")

    # GPS
    if not device.gps_enabled:
        score -= 10
        issues.append("GPS disabled")

    score = max(score, 0)

    if score >= 90:
        status = "HEALTHY"

    elif score >= 70:
        status = "WARNING"

    else:
        status = "CRITICAL"

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "health_score": score,
        "health_grade": get_health_grade(score),
        "risk_level": get_risk_level(score),
        "status": status,
        "issues": issues,
        "recommendations": get_recommendations(issues)
    }


if __name__ == "__main__":

    device = DeviceState(
        battery_percent=18,
        network_available=True,
        free_storage_gb=3.5,
        gps_enabled=False
    )

    result = calculate_health_score(device)

    print("=" * 50)
    print("DEVICE HEALTH REPORT")
    print("=" * 50)

    print(f"Timestamp    : {result['timestamp']}")
    print(f"Health Score : {result['health_score']}")
    print(f"Health Grade : {result['health_grade']}")
    print(f"Risk Level   : {result['risk_level']}")
    print(f"Status       : {result['status']}")

    print("\nIssues:")

    if result["issues"]:
        for issue in result["issues"]:
            print(f" - {issue}")
    else:
        print(" - None")

    print("\nRecommendations:")

    if result["recommendations"]:
        for recommendation in result["recommendations"]:
            print(f" - {recommendation}")
    else:
        print(" - None")

    print("=" * 50)
