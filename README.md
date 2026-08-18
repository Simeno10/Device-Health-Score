## Device Health Assessment

The tool evaluates device health based on multiple diagnostic
signals and provides actionable recommendations for detected
issues.

### Metrics

- Battery level
- Network connectivity
- Available storage
- GPS status

### Output

- Health Score (0-100)
- Device Status
- Detected Issues
- Recommended Actions

## Health Trend Tracking

The project supports historical health score analysis,
allowing users to monitor device condition over time.

### Metrics

- Average health score
- Highest score
- Lowest score
- Trend detection

Possible trends:

- IMPROVING
- STABLE
- DECLINING

  ## Device Health Assessment

The tool evaluates device health based on multiple diagnostic
signals and provides actionable recommendations for detected
issues.

### Metrics

- Battery level
- Network connectivity
- Available storage
- GPS status

### Output

- Health Score (0-100)
- Device Status
- Detected Issues
- Recommended Actions

## Health Trend Tracking

The project supports historical health score analysis,
allowing users to monitor device condition over time.

### Metrics

- Average health score
- Highest score
- Lowest score
- Trend detection

Possible trends:

- IMPROVING
- STABLE
- DECLINING

  ## Scoring Logic

The health score starts at 100 points and is reduced based on detected issues.

| Condition | Penalty |
|------------|----------|
| Critical battery level (<10%) | -30 |
| Low battery level (<20%) | -15 |
| Network unavailable | -20 |
| Critical storage space (<2 GB) | -25 |
| Low storage space (<5 GB) | -10 |
| GPS disabled | -10 |

### Status Thresholds

| Score | Status |
|---------|---------|
| 90-100 | HEALTHY |
| 70-89 | WARNING |
| 0-69 | CRITICAL |

## Recommendations Engine

Detected issues are automatically mapped to actionable recommendations:

- Battery issues → charging recommendations
- Network issues → connectivity checks
- Storage issues → cleanup suggestions
- GPS issues → location service guidance

## Future Improvements

- Historical trend analysis
- CSV report export
- HTML dashboard generation
- YAML-based configuration
- Health score visualization
- GitHub Actions integration
``
