class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        results = []
        for i in range(len(pairs)):
            j = i - 1
            
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j -= 1

            results.append(pairs.copy())

        return results
