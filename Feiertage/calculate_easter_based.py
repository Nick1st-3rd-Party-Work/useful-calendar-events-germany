from datetime import date, timedelta

def getEasterDate(year):
    k = year // 100
    m = 15 + (3*k + 3)//4 - (8*k+13)//25
    s = 2 - (3*k + 3)//4
    a = year % 19
    d = (19*a + m) % 30
    r = (d + a//11) // 29
    og = 21 + d - r
    sz = 7 - (year + year//4 + s)%7
    oe = 7 - (og - sz)%7
    os = og + oe - 1
    dt = date(year, 3, 1)
    return dt + timedelta(days=os)

def main():
    for i in range(2000, 2027):
        easter = getEasterDate(i)
        karfreitag = easter - timedelta(days=2)
        eastermonday = easter + timedelta(days=1)
        himmelfahrt = easter + timedelta(days=39)
        pfingstmontag = easter + timedelta(days=50)
        fronleichnam = easter + timedelta(days=60)
        print(karfreitag.strftime("%d.%m.%y, Karfreitag,"))
        print(eastermonday.strftime("%d.%m.%y, Ostermontag,"))
        print(himmelfahrt.strftime("%d.%m.%y, Christi-Himmelfahrts-Tag,"))
        print(pfingstmontag.strftime("%d.%m.%y, Pfingstmontag,"))
        print(fronleichnam.strftime("%d.%m.%y, Fronleichnamstag,"))

if __name__ == "__main__":
    main()
