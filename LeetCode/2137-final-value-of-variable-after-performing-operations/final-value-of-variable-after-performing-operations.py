class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        index = 0
        while index < len(operations):
            for operation in operations:
                if operation == "--X" or operation == "X--":
                    x -= 1
                    index += 1
                elif operation == "X++" or operation == "++X":
                    x += 1
                    index += 1
                else:
                    x = 0
                    index += 1
        return x
        