import datetime
def check(m,y) :
    d = datetime.date(y,m,13)
    w = d.weekday()
    return w == 4
print(check(11,2023))