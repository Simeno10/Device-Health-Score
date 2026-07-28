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


def get_recommendations(issues):
    recommendations = []

    mapping = {
        "Critical battery level": "Charge the device immediately.",
        "Low battery level": "Consider charging the device soon.",
        "Network unavailable": "Verify Wi-Fi or cellular connection.",
        "Critical storage space": "Remove unnecessary files.",
        "Low storage space": "Free additional storage space.",
        "GPS disabled": "Enable location services."
    }

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
        "health_score": score,
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

    print("Health Score:", result["health_score"])
    print("Status:", result["status"])

    if result["issues"]:
        print("\nIssues:")
        for issue in result["issues"]:
            print(f" - {issue}")

    if result["recommendations"]:
        print("\nRecommendations:")
        for recommendation in result["recommendations"]:
            print(f" - {recommendation}")
`
     
