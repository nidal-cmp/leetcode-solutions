
            elif ch == ']':
                previous, repeat = stack.pop()
                current = previous + current * repeat

            else:
                current += ch

        return current

