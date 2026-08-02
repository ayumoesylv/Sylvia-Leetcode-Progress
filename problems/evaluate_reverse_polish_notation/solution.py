class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        process = []
        for token in tokens:
            if (token not in ['+', '-', '*', '/']):
                process.append(token)
            else:
                left = int(process.pop())
                right = int(process.pop())
                if token == '+':
                    process.append(right + left)
                elif token == '-':
                    process.append(right - left)
                elif token == '*':
                    process.append(right * left)
                elif token == '/':
                    intermediate = floor(right / left) if right / left > 0 else ceil(right / left)
                    process.append(intermediate)               
        return int(process[0])
        