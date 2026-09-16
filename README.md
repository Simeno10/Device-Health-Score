# Device Health Score

A lightweight Python-based diagnostic engine that evaluates device health using key operational metrics and generates actionable insights.

The project is designed to provide a simple but expandable framework for assessing overall device condition and identifying potential reliability risks.

---

## Features

✅ Health Score calculation (0-100)

✅ Health Grade classification (A-F)

✅ Device Health Category

✅ Device Risk Level assessment

✅ Reliability Score calculation

✅ Automatic issue detection

✅ Actionable recommendations

✅ Timestamped reports

✅ Human-readable console output

---

## Health Metrics

The engine evaluates the following device characteristics:

- Battery percentage
- Network availability
- Available storage space
- GPS availability

Each detected issue reduces the overall health score.

---

## Scoring Logic

The device starts with a score of **100 points**.

Penalties are applied based on detected issues.

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

The score determines the device status.

| Score Range | Status |
|-------------|---------|
| 90-100 | HEALTHY |
| 70-89 | WARNING |
| 0-69 | CRITICAL |

---

## Health Grade

The engine converts the numerical score into a simple letter grade.

| Score Range | Grade |
|-------------|--------|
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| Below 60 | F |

---

## Device Risk Level

Risk level indicates the urgency of remediation.

| Score Range | Risk Level |
|-------------|------------|
| 90-100 | LOW |
| 70-89 | MEDIUM |
| 50-69 | HIGH |
| Below 50 | CRITICAL |

### Example

```json
{
  "health_score": 82,
  "risk_level": "MEDIUM"
}
```

---

## Device Health Category

Devices are grouped into business-friendly categories for easier reporting and fleet monitoring.

| Score Range | Category |
|-------------|------------|
| 90-100 | OPTIMAL |
| 75-89 | GOOD |
| 60-74 | FAIR |
| Below 60 | POOR |

### Example

```json
{
  "health_score": 78,
  "health_category": "GOOD"
}
```

---

## Reliability Score

Reliability is based on the number of detected issues.

| Number of Issues | Reliability Score |
|------------------|-------------------|
| 0 | 100 |
| 1 | 85 |
| 2 | 70 |
| 3 | 55 |
| 4 | 40 |
| 5+ | 25 or lower |

A lower reliability score indicates a higher risk of operational instability.

### Example

```json
{
  "reliability_score": 55
}
```

---

## Recommendations Engine

The engine automatically generates recommendations for detected issues.

| Issue | Recommendation |
|---------|---------------|
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
  "timestamp": "2026-09-16T09:30:00",
  "health_score": 65,
  "health_grade": "D",
  "health_category": "FAIR",
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
from health_score import DeviceState
from health_score import calculate_health_score

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

## Sample Console Report

```text
============================================================
DEVICE HEALTH REPORT
============================================================
Timestamp         : 2026-09-16T09:30:00
Health Score      : 65
Health Grade      : D
Health Category   : FAIR
Risk Level        : HIGH
Reliability Score : 55
Status            : CRITICAL

Issues:
 - Low battery level
 - Low storage space
 - GPS disabled

Recommendations:
 - Consider charging the device soon.
 - Free additional storage space.
 - Enable location services.
============================================================
```

---

## Project Structure

```text
.
├── health_score.py
├── README.md
└── requirements.txt
```

---

## Future Improvements

Planned enhancements:

- Historical trend analysis
- CSV export
- JSON export module
- HTML dashboard
- YAML configuration support
- Device fleet analysis
- Health score analytics
- GitHub Actions integration
- REST API interface
- Multi-device reporting

---

## Contributing

Contributions, feature requests, and suggestions are welcome.

Feel free to open an issue or submit a pull request.

---

## License

MIT License
