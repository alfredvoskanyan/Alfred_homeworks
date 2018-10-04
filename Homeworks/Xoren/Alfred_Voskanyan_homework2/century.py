def get_century(n):
    return (n+99)//100


while True:
    year = int(input("Enter the year or 0 to exit"))
    if not year:
        print("Thanks")
        break
    print("Year: %s ---- Century: %s" % (year, get_century(year)))



