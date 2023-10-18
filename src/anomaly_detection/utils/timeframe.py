def calculate_timeframe(
    total_rows: int,
    t0_percentage: float,
    t1_percentage: float,
    t2_percentage: float,
) -> tuple[int, int, int]:
    t0 = int(t0_percentage * total_rows)
    t1 = int(t1_percentage * total_rows)
    t2 = int(t2_percentage * total_rows)
    uncounted_days = t0 + t1 + t2 - total_rows

    if uncounted_days < 0:
        t1 += abs(uncounted_days)
    elif uncounted_days > 0:
        t1 -= uncounted_days
    return (t0, t1, t2)
