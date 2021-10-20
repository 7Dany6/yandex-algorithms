def parenthesis(sequence):
    opening = 0
    closing = 0
    if sequence[0] == '(':
        for paren in sequence:
            if paren == '(':
                opening += 1
            else:
                closing += 1
    else:
        return "NO"
    if opening == closing:
        return "YES"
    else:
        return "NO"
print(parenthesis(input()))
