def study_schedule(permanence_period, target_time):
    student = 0
    for period in permanence_period:
        if (
            type(target_time) != int
            or type(period[0]) != int
            or type(period[1]) != int
        ):
            return None
        if period[0] <= target_time <= period[1]:
            student += 1
    return student
