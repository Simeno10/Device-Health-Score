"""
health_report.py

Creates human-readable device health reports.
"""


def generate_report(result: dict) -> str:
    report = []

    report.append("=" * 40)
    report.append("DEVICE HEALTH REPORT")
    report.append("=" * 40)

    report.append(f"Health Score : {result['health_score']}")
    report.append(f"Status       : {result['status']}")

    report.append("")

    report.append("Issues:")
    if result["issues"]:
        for issue in result["issues"]:
            report.append(f"  - {issue}")
    else:
        report.append("  None")

    report.append("")

    report.append("Recommendations:")
    if result["recommendations"]:
        for recommendation in result["recommendations"]:
            report.append(f"  - {recommendation}")
    else:
        report.append("  None")

    report.append("")
    report.append("=" * 40)

    return "\n".join(report)


if __name__ == "__main__":
    sample_result = {
        "health_score": 75,
        "status": "WARNING",
        "issues": [
            "Low storage space",
            "GPS disabled"
        ],
        "recommendations": [
            "Free additional storage space.",
            "Enable location services."
        ]
    }

    print(generate_report(sample_result))
