class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recursion(string, open_brackets, closed_brackets):
            if len(string) == 2 * n:
                result.append(string)
                return
            if open_brackets < n:
                recursion(string + "(", open_brackets + 1, closed_brackets)
            if closed_brackets < open_brackets:
                recursion(string + ")", open_brackets, closed_brackets + 1)
        recursion("", 0, 0)
        return result