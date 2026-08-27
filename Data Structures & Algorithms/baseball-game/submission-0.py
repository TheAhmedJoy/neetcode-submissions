class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scorecard = []

        for i in range (len(operations)):
            if operations[i] == "C":
                scorecard.pop()
            elif operations[i] == "D":
                scorecard.append(scorecard[-1] * 2)
            elif operations[i] == "+":
                scorecard.append(scorecard[-1] + scorecard[-2])
            else:
                scorecard.append(int(operations[i]))
        
        return sum(scorecard)
