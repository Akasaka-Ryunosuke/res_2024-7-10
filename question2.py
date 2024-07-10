while True:
    try:
        line = input()
        left_index = []
        right_index = []
        for i in range(len(line)):
            if line[i] == '(':
                left_index.append(i)
            elif line[i] == ')':
                if len(left_index) != 0:
                    left_index.pop()
                else:
                    right_index.append(i)
        s = ""
        for i in range(len(line)):
            if i in left_index:
                s += "x"
            elif i in right_index:
                s += "?"
            else:
                s += " "
        print(s)
    except EOFError:
        break
