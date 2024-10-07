# https://leetcode.com/problems/day-of-the-week/
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Adjust months for Zeller's congruence
        if month == 1 or month == 2:
            month += 12
            year -= 1

        q = day
        m = month
        K = year % 100  # Last two digits of the year
        J = year // 100  # First two digits of the year

        # Zeller's Congruence formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) - 2 * J) % 7

        # Mapping of Zeller's output to days of the week
        day_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        return day_of_week[h]

