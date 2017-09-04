# def convert_temperature(T_f):
#     return (5/9)*(T_f-32)
#
#
# def main():
#     try:
#         T_f = int(input("Please enter a temperature in celsius: "))
#         print(convert_temperature(T_f))
#     except ValueError:
#         print("Dedbil")
# if __name__ == "__main__":
#
#     main()
a = ()
for elements in range(10):
    if elements % 2 != 0:
        a.append(elements)
a = a[:3]

b = ()
for elements in range(10):
    if elements % 2 == 0:
        b.append(elements)
b = b[:3]
print(a)
print(b)
c = []
c = a+b
print(c)
d = []
d = sorted(c, reverse=True )
print(d)
c[3] = 42
print(c)
d.append(10)
print(d)
print(c[:3])
c.extend([7, 8, 9])
print(c)
print(d[-1])
print(len(d))
)
