class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = [] 
        for opp in operations: 
            if opp == "+": 
                 record.append(record[-1] + record[-2])
            elif opp == "D": 
                record.append(record[-1] * 2) 
            elif opp == "C": 
                record.pop()
            else: #its an integer 
                record.append(int(opp))

        return sum(record)
             

        