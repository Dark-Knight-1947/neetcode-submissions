class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            asteroid = asteroids[i]

            while True:

                # stack is empty → asteroid can be added
                if not stack:
                    stack.append(asteroid)
                    break

                # TOP IS POSITIVE
                if stack[-1] > 0:

                    # positive + positive → no collision
                    if asteroid > 0:
                        stack.append(asteroid)
                        break

                    # positive + negative → COLLISION
                    else:
                        if stack[-1] < abs(asteroid):
                            stack.pop()
                            # DON'T append yet
                            # check asteroid against new top again

                        elif stack[-1] == abs(asteroid):
                            stack.pop()
                            # both destroyed
                            break

                        else:
                            # stack top survives
                            # asteroid destroyed
                            break

                # TOP IS NEGATIVE
                else:
                    # negative + negative → no collision
                    # negative + positive → no collision
                        stack.append(asteroid)
                        break

        return stack