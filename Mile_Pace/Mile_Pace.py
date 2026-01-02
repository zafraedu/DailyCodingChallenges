def mile_pace(miles: float, time: str) -> str:
    minutes, seconds = map(int, time.split(':'))
    total_seconds = minutes * 60 + seconds

    pace_seconds = total_seconds / miles

    pace_minutes = int(pace_seconds // 60)
    pace_seconds = int(round(pace_seconds % 60))

    return f"{pace_minutes:02d}:{pace_seconds:02d}"


# Tests
print(mile_pace(3, "24:00"))
print(mile_pace(1, "06:45"))
print(mile_pace(2, "07:00"))
print(mile_pace(26.2, "120:35"))