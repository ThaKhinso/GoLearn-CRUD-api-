def changetosecond(hour: int, minute: int, second: int):
    return (hour * 3600) + (minute * 60) + second

print(changetosecond(1,1,30))