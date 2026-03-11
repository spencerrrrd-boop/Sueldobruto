# ====================================
# Calculadora de Sueldo Neto (RD)
# ====================================

# ----- CONSTANTES -----

TSS = 0.0591        # 5.91% Seguridad Social
ISR = 0.15          # 15% Impuesto Sobre la Renta (simplificado)
BONIFICACION = 0.10 # 10% Bonificación
DOBLE_SUELDO = 1    # equivalente a un sueldo adicional


print("====================================")
print("  CALCULADORA DE SUELDO NETO (RD)   ")
print("====================================")

# ----- ENTRADA DE DATOS -----

sueldo_bruto = float(input("Ingrese el sueldo bruto del empleado: RD$ "))

# Validación
if sueldo_bruto <= 0:
    print("Error: el sueldo debe ser mayor que 0")
    exit()

otros_descuentos = float(input("Ingrese otros descuentos (si no hay escriba 0): RD$ "))

respuesta_bonificacion = input("¿El empleado recibe bonificación? (si/no): ").lower()
respuesta_doble = input("¿Aplica doble sueldo? (si/no): ").lower()

# ----- CALCULOS -----

descuento_tss = sueldo_bruto * TSS
descuento_isr = sueldo_bruto * ISR

# Bonificación
if respuesta_bonificacion == "si":
    bonificacion = sueldo_bruto * BONIFICACION
else:
    bonificacion = 0

# Doble sueldo
if respuesta_doble == "si":
    doble_sueldo = sueldo_bruto * DOBLE_SUELDO
else:
    doble_sueldo = 0

# Sueldo neto
sueldo_neto = sueldo_bruto - descuento_tss - descuento_isr - otros_descuentos + bonificacion + doble_sueldo


# ----- RESULTADOS -----

print("\n----------- RESULTADOS -----------")

print(f"Sueldo Bruto: RD${sueldo_bruto:.2f}")
print(f"Descuento Seguridad Social: RD${descuento_tss:.2f}")
print(f"Descuento ISR: RD${descuento_isr:.2f}")
print(f"Otros Descuentos: RD${otros_descuentos:.2f}")
print(f"Bonificación: RD${bonificacion:.2f}")
print(f"Doble sueldo: RD${doble_sueldo:.2f}")

print("----------------------------------")
print(f"Sueldo Neto Final: RD${sueldo_neto:.2f}")