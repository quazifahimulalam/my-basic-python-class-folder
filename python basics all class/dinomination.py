m = int(input("enter the withdrawal amount:"))

tk1000  = m // 1000
print("1000 tk note:",tk1000)
m %= 1000

tk500  = m // 500
print("500 tk note:",tk500)
m %= 500

tk200  = m // 200
print("200 tk note:",tk200)
m %= 200

tk100  = m // 100
print("100 tk note:",tk100)
m %= 100

tk50  = m // 50
print("50 tk note:",tk50)
m %= 50

tk20  = m // 20
print("20 tk note:",tk20)
m %= 20

tk10  = m // 10
print("10 tk note:",tk10)
m %= 10

tk5 = m // 5
print("5 tk note:",tk5)
m %= 5

tk2  = m // 2
print("2 tk note:",tk2)
m %= 2

print("1 tk note:",tk2)