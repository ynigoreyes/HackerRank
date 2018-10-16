# O(n) Time O(1) space
def breakingRecords(scores):
    record = [scores[0], scores[0]] # left is max, right is min
    answer = [0, 0]
    for i, val in enumerate(scores):
        if record[0] < val:
            record[0] = val
            answer[0] += 1
        elif record[1] > val:
            record[1] = val
            answer[1] += 1
    
    return answer
