class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            self.mp[key].append((value, timestamp))
        else:
            self.mp[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.mp.get(key, "")
        if len(values) > 0 and values[0] == "":
            return ""
        
        l, r = 0, len(values) - 1

        closest = "" 
        while l <= r:
            m = (l + r) // 2

            if values[m][1] == timestamp:
                return values[m][0]

            if values[m][1] < timestamp:
                closest = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return closest
