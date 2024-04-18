class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mn,mx,mode,max_freq,sm,total=inf,-inf,0,0,0,0
        arr = []
        for i,el in enumerate(count):
            if el > 0:
                mn = min(mn, i)
                mx = max(mx, i)
            if el > max_freq:
                max_freq = el
                mode = i
            sm += i*el
            total += el
            arr.append(total)
        med1 = bisect.bisect(arr, (total-1)//2)
        med2 = bisect.bisect(arr, total//2)
        return [mn, mx, sm/total, (med1 + med2)/2, mode]