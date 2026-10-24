from datetime import datetime
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        return max(0, (datetime.strptime(end, "%m-%d") - datetime.strptime(start, "%m-%d")).days + 1)