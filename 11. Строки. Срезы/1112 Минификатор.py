N = int(input())
for _ in range(N):
    string = input()
    quote_opened = False
    still_spaces = True
    i = 0
    while i < (len(string) - 1):
        if string[i] != ' ':
            still_spaces = False
        if string[i] == '#' and not quote_opened:
            string = string[:i]
        elif string[i] == '\'' and not (string[i - 1] == '\\' and string[i - 2] != '\\'):
            quote_opened = not quote_opened
        elif string[i] == ' ' and not still_spaces and not quote_opened:
            if string[i + 1] == ' ':
                string = string[: i] + string [i + 1:]
                i -= 1
        i += 1
    print(string)