class Solution:
    def simplifyPath(self, path: str) -> str:
        flush = ""
        new_path = []
        final = ""
        for ch in path + '/':
            if flush != "" and ch == '/':
                if flush == '..': 
                    if len(new_path) > 0:
                        new_path.pop() 
                elif flush != '.':
                    new_path.append(flush)                    
                flush = ""
            elif ch != '/':
                flush += ch 
        final = "/" + "/".join(new_path)
        return final

