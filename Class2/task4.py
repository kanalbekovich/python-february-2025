for i in range(1,101):
    x=str(i)
    if i % 3 == 0:
        x += " foo "
    if i % 5 == 0:
        x += " bar "
    if i % 10 == 0:
        x += " hello "
    print(x)
