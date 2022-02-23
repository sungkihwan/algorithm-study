from collections import deque

def solution(bridge_length, weight, truck_weights):
    count = 0
    truck_weights = deque(i for i in truck_weights)
    bridge_truck = deque()
    bridge_weight = 0

    while truck_weights:
        count += 1
        if len(bridge_truck) == bridge_length:
            cur = bridge_truck.popleft()
            bridge_weight -= cur

        if bridge_weight + truck_weights[0] <= weight:
            cur = truck_weights.popleft()
            bridge_weight += cur
            bridge_truck.append(cur)
        else:
            bridge_truck.append(0)

    count += bridge_length

    return count

print(solution(2,10,[7, 4, 5, 6]))