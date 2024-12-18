def solution(a, b):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    totalDay = sum(month_days[: a - 1]) + b - 1

    return days[(totalDay + 5) % 7]