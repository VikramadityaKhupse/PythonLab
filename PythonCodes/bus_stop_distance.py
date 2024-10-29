# https://leetcode.com/problems/distance-between-bus-stops/description/
class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start, destination = destination, start

        clockwise_distance = sum(distance[start:destination])

        total_distance = sum(distance)
        counterclockwise_distance = total_distance - clockwise_distance

        return min(clockwise_distance, counterclockwise_distance)
