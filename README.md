# Device Health Score

A lightweight Python-based diagnostic engine that evaluates device health and generates actionable insights based on key operational metrics.

---

## Features

- Health Score calculation (0-100)
- Health Grade classification (A-F)
- Device Risk Level assessment
- Reliability Score calculation
- Automatic issue detection
- Actionable recommendations
- Timestamped reports
- Human-readable output

---

## Metrics Evaluated

The engine evaluates:

- Battery percentage
- Network availability
- Available storage
- GPS availability

Each detected issue reduces the overall health score.

---

## Scoring Logic

The device starts with a score of 100.

| Condition | Penalty |
|------------|----------|
| Critical battery (<10%) | -30 |
| Low battery (<20%) | -15 |
| Network unavailable | -20 |
| Critical storage (<2 GB) | -25 |
| Low storage (<5 GB) | -10 |
| GPS disabled | -10 |

---

## Device Status

| Score | Status |
|---------|---------|
| 90-100 | HEALTHY |
| 70-89 | WARNING |
| 0-69 | CRITICAL |

---

## Health Grade

| Score | Grade |
|---------|---------|
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| Below 60 | F |

---

## Device Risk Level

Risk level indicates operational urgency.

| Score | Risk |
|---------|---------|
| 90-100 | LOW |
| 70-89 | MEDIUM |
| 50-69 | HIGH |
| Below 50 | CRITICAL |

Example:

```json
{
  "health_score": 82,
  "health_grade": "B",
  "risk_level": "MEDIUM"
}
```

---

## Reliability Score

Reliability is calculated from the number of detected issues.

| Issues | Reliability Score |
|----------|-------------------|
| 0 | 100 |
| 1 | 85 |
| 2 | 70 |
| 3 | 55 |
| 4 | 40 |
| 5+ | 25 or lower |

A lower reliability score indicates a device more likely to experience operational issues.

---

## Recommendations Engine

Detected issues automatically generate recommendations.

| Issue | Recommendation |
|---------|----------------|
| Critical battery level | Charge the device immediately |
| Low battery level | Consider charging the device soon |
| Network unavailable | Verify Wi-Fi or cellular connection |
| Critical storage space | Remove unnecessary files |
| Low storage space | Free additional storage space |
| GPS disabled | Enable location services |

---

## Example Output

```json
{
  "timestamp": "2026-08-26T14:20:00",
  "health_score": 65,
  "health_grade": "D",
  "risk_level": "HIGH",
  "reliability_score": 55,
  "status": "CRITICAL",
  "issues": [
    "Low battery level",
    "Low storage space",
    "GPS disabled"
  ],
  "recommendations": [
    "Consider charging the device soon.",
    "Free additional storage space.",
    "Enable location services."
  ]
}
```

---

## Example Usage

```python
from health_score import DeviceState, calculate_health_score

device = DeviceState(
    battery_percent=18,
    network_available=True,
    free_storage_gb=3.5,
    gps_enabled=False
)

result = calculate_health_score(device)

print(result)
```

---

## Future Improvements

- Health trend analysis
- CSV export
- HTML dashboard
- YAML configuration
- Device fleet management
- Web interface
- GitHub Actions integration
- Historical analytics

---

## License

MIT License
