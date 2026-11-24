# --- CONVERSOR DE MONEDAS ---

usd_a_cop = 4200.0  # 1 Dolar = 4200 Pesos
usd_a_eur = 0.95    # 1 Dolar = 0.95 Euros

print("--- BIENVENIDO AL CONVERSOR DE MONEDAS ---")
print("1. Pesos Colombianos (COP)")
print("2. Dolares (USD)")
print("3. Euros (EUR)")

opcion = input("Elige el numero de tu moneda de origen (1, 2 o 3): ")

if opcion == "1":
    cop = float(input("Ingresa la cantidad en Pesos (COP): "))
    # Convertimos de COP a las otras monedas
    dolares = cop / usd_a_cop
    euros = dolares * usd_a_eur
    print(f"{cop} COP equivalen a {dolares:.2f} USD y {euros:.2f} EUR")

elif opcion == "2":
    dolares = float(input("Ingresa la cantidad en Dólares (USD): "))
    # Convertimos de USD a las otras monedas
    cop = dolares * usd_a_cop
    euros = dolares * usd_a_eur
    print(f"{dolares} USD equivalen a {cop:.2f} COP y {euros:.2f} EUR")

elif opcion == "3":
    euros = float(input("Ingresa la cantidad en Euros (EUR): "))
    # Convertimos de EUR a las otras monedas
    dolares = euros / usd_a_eur
    cop = dolares * usd_a_cop
    print(f"{euros} EUR equivalen a {dolares:.2f} USD y {cop:.2f} COP")

else:
    print("Opción no válida. Por favor, ejecuta el programa de nuevo y elige 1, 2 o 3.")



