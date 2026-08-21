class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # you just need a heap, which is an array
        # each operation is nlogn usually, as you have to rebalance the 
        # tree. Brute force is sorting, should be around n2logn as 
        # you have to sort then go through the list again
        self.arr = nums
        self.k = k

    def add(self, val: int) -> int:
        sol = 0
        self.arr.append(val)
        self.arr.sort(reverse=True)
        print(self.arr)
        for i in range(len(self.arr)):
            if i + 1 == self.k:
                sol = self.arr[i]
        return sol
        