class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
            # Convert deadends to a set for O(1) lookups
            deadends = set(deadends)

            # Check if starting point is in deadends or if target is not reachable
            if "0000" in deadends:
                return -1

            # BFS initialization
            queue = deque(['0000'])
            visited = set(['0000'])
            steps = 0

            while queue:
                level_length = len(queue)

                for i in range(level_length):
                    current_state = queue.popleft()

                    # If current state is target, we found the solution
                    if current_state == target:
                        return steps

                    # Generate all possible next states
                    for j in range(4):
                        up = current_state[:j] + str((int(current_state[j]) + 1) % 10) + current_state[j+1:]
                        down = current_state[:j] + str((int(current_state[j]) - 1) % 10) + current_state[j+1:]

                        if up not in visited and up not in deadends:
                            visited.add(up)
                            queue.append(up)

                        if down not in visited and down not in deadends:
                            visited.add(down)
                            queue.append(down)

                steps += 1

            # If we're here, then we haven't found the target
            return -1