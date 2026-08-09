class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = [] 
        for opp in operations: 
            if opp == "+": 
                records.append(records[-1] + records[-2])
            elif opp == "D":
                records.append(records[-1] * 2)
            elif opp == "C":
                records.pop()
            else: 
                records.append(int(opp))
        
        return sum(records)
        