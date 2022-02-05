def car_fleet(target, position, speed):
    pair = sorted(zip(position, speed), reverse=True)
    stack = []

    for pos, v in pair:

        dist = target - pos
        time = dist / v

        if not stack:
            stack.append(time)
        elif time > stack[-1]:
            stack.append(time)

    return len(stack)
