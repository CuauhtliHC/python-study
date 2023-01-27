name = input("¿Cual es tu nombre?")
sales = input("¿Cuales fueron tus ventas?")

print(f"Ok {name} este mes ganaste ${round(int(sales) / 100 * 13, 2)}")