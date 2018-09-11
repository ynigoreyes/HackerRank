class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Create a hash table to store the lefts or rights in a hash table.
        # At the end of parse, subtract the left and the right and then the Up and then down
        # and check if they equal 0
        
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        table = {
            "U": 0,
            "D": 0,
            "R": 0,
            "L": 0
        }
        
        for i, move in enumerate(moves):
            table[move] += 1
        
        if table["U"] - table["D"] == 0 and table["R"] - table["L"] == 0:
            return True
        else:
            return False
