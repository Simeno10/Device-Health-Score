"""
health_history.py

Tracks device health score history and trend.
"""

from statistics import mean


def calculate_trend(scores):
    if len(scores) < 2:
        return "INSUFFICIENT_DATA"

    if scores[-1] > scores[0]:
        return "IMPROVING"

    if scores[-1:
        return "DECLINING"

    return "STABLE"


def generate_summary(scores):
    if        return {
            "trend": "NO_DATA",
            "average_score": 0,
            "highest_score": 0,
            "lowest_score": 0
        }

    return {
        "trend": calculate_trend(scores),
        "average_score": round(mean(scores), 2),
        "highest_score": max(scores),
        "lowest_score": min(scores)
    }


if __name__ == "__main__":
    history = [65, 68, 72, 76, 81]

    result = generate_summary(history)

    print("Trend:", result["trend"])
    print("Average:", result["average_score"])
    print("Highest:", result["highest_score"])
    print("Lowest:", result["lowest_score"])
