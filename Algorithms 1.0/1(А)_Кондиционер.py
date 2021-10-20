def conditioner(now, wanted, reg):
    flag = True
    if now > wanted:
        flag = False
    if reg == "freeze":
        return now if flag else wanted
    elif reg == "heat":
        return wanted if flag else now
    elif reg == "auto":
        return wanted
    else:
        return now


troom, tcond = map(int, input().split())
regime = input()

print(conditioner(troom, tcond, regime))
