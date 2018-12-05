def read_input():
    with open('input-5') as input_file:
        return input_file.read().strip()


def annihilate(polymer):
    stack = [polymer[0]]
    i = 1
    while i < len(polymer):
        if stack and abs(ord(polymer[i]) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(polymer[i])

        i += 1

    return ''.join(stack)
