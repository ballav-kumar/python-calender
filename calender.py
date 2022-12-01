# calender range 1600 - 2399
def year(yr):
    num = yr - 1
    n1 = int(num / 100) * 100
    n2 = num % 100

    leap = int(n2 / 4)
    ordinary = n2 - leap

    odd = ((leap * 2) + ordinary) % 7

    odd1 = 0
    if 1600 <= n1 < 2000:
        remain = n1 - 1600
        if remain == 300:
            odd1 = 1
        elif remain == 200:
            odd1 = 3
        elif remain == 100:
            odd1 = 5
        else:
            odd1 = 0

    elif 2000 <= n1 < 2400:
        remain = n1 - 2000
        if remain == 300:
            odd1 = 1
        elif remain == 200:
            odd1 = 3
        elif remain == 100:
            odd1 = 5
        else:
            odd1 = 0
    return (odd + odd1) % 7


def month(mon, yr):
    leapyear = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    ordyear = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    preodd = 0

    if yr % 4 == 0:
        for i in range(mon-1):
            preodd += leapyear[i]
    else:
        for i in range(mon-1):
            preodd += ordyear[i]
    odd = preodd % 7
    return odd


def day(d):
    odd = d % 7
    return odd


def week(n):
    switcher = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return switcher.get(n)


if __name__ == "__main__":
    print("--this program in to provide the weekday of the year--")
    d = int(input("provide the day in numbers: "))
    mon = int(input("provide the month in numbers: "))
    yr = int(input("provide the year in numbers: "))

    odd = year(yr)
    odd1 = month(mon, yr)
    odd2 = day(d)

    fodd = (odd + odd1 + odd2) % 7

    wek = week(fodd)
    print("The weekday is: ", wek)
