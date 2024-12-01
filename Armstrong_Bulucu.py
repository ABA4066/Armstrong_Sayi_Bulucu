print("N haneli bir sayının basamaklarının n'inci üstlerinin toplamı, sayının kendisine eşitse, böyle sayılara Armstrong sayı denir.")
n=0

while True:
    top = 0

    n=n+1
    u=len(str(n))

    for i in range(0,u):
        top += int(str(n)[i])**u
    if top == int(n):
        print("\n{} bir Armstrong sayısıdır.\n".format(n))
