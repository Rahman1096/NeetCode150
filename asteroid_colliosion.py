class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:

            # If stack is empty, simply push the asteroid.
            if not stack:
                stack.append(num)

            # Both asteroids are moving right, so no collision.
            elif num > 0 and stack[-1] > 0:
                stack.append(num)

            # Top of stack is moving left.
            # (-- and -+) cases never collide.
            elif stack[-1] < 0:
                stack.append(num)

            # (+-) case: collision is possible.
            else:
                alive = True

                while stack and stack[-1] > 0:

                    # Top of stack is larger.
                    # Current asteroid explodes.
                    if stack[-1] > abs(num):
                        alive = False
                        break

                    # Current asteroid is larger.
                    # Remove the top asteroid and continue checking.
                    elif stack[-1] < abs(num):
                        stack.pop()

                    # Both are equal.
                    # Both explode.
                    else:
                        stack.pop()
                        alive = False
                        break

                # Push only if the current asteroid survived.
                if alive:
                    stack.append(num)

        return stack