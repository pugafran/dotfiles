import random

MAX_FAC=9
MAX_LEV=7

def main () -> int:
    f = open("py_events.txt", "w")
    total: dict [str, dict [str, int]] = { }
    for i in range (0, 10000, 1):
        fac: str = str(random.randint(-1, MAX_FAC+1))
        lev: str = str(random.randint(-1, MAX_LEV+1))
        if (int(fac) >= 0 and int(fac) <= MAX_FAC and int(lev) >= 0 and int(lev) <= MAX_LEV):
            if (not fac in total):
                total[fac] = { }
            if (not lev in total[fac]):
                total[fac][lev] = 0
            total[fac][lev] += 1
        f.write(str(random.randint(-1, 9)) + ":" + str(random.randint(-1, 7)) + ":" + "python generated (" + str(i) + ")\n")
    f.close()
    show_totals(total)
    return 0

def show_totals (dic: dict [str, dict [str, int]]) -> None:
    print(end="\t")
    for i in range (0, MAX_LEV+1, 1):
        print(str(i), end="\t")
    print()
    for fac, subdic in sorted(dic.items()):
        print(fac, end="\t")
        for lev, tot in subdic.items():
            print(str(tot), end="\t")
        print()
    return

if __name__ == '__main__':
    main()
