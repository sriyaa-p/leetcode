class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]
        for current in asteroids:
            alive=True
            while stack and stack[-1]>0 and current<0:
                prev=stack[-1]
                if abs(prev)<abs(current):
                    stack.pop()
                elif abs(prev) > abs(current):
                    alive=False
                    break
                else:
                    stack.pop()
                    alive=False
                    break
            if alive:
                stack.append(current)
        return stack