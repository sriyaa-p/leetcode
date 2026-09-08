class Solution:
    def isValid(self, s: str) -> bool:
        # Make an empty Stack
        stack=[]
        #Make a dictonary to match the opening and closing brackets
        pairs={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for parentheses in s:
            if parentheses in "({[":
                stack.append(parentheses)
            else:
                # if stack is empty will return true and if the Top Element doesn't match current elements's pair then we must return False
                if not stack or stack.pop()!=pairs[parentheses]:
                    return False
        # if the s= "(((" then len(stack)=3 then 3!=0 so we will return False since it is an invalid string
        return len(stack)==0