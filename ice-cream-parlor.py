# ==========================================
# Sistema Heladería Frosty Delights
# ==========================================

def inicializar_inventario():
  # lista que almacena diccionarios con atributos clave-valor
  productos = [
    {"sabor": "Chocolate", "precio": 2.5, "stock": 100},
    {"sabor": "Vainilla", "precio": 2.0, "stock": 80},
    {"sabor": "Fresa", "precio": 3.0, "stock": 70}
  ]
  return productos


def mostrar_sabores(lista_productos):
  # recorre e imprime los sabores de helado registrados con un formato limpio.
  print("\n=================================================")
  print(" Sabores de Helado:")
  print("=================================================")
  
  # iteración sobre la lista de colecciones
  for item in lista_productos:
    # extracción de datos formateada
    print(f"Sabor: {item['sabor']}, Precio: {item['precio']:.1f}, Stock: {item['stock']}")
  print("=================================================\n")


def agregar_nuevo_sabor(lista_productos):
  print("\n--- Registro de Nuevo Producto ---")
  sabor_nuevo = input("Ingrese el nombre del sabor: ").strip().capitalize()
  
  # validación de duplicados en la lista
  if any(item['sabor'] == sabor_nuevo for item in lista_productos):
    print(f"[AVISO] El sabor '{sabor_nuevo}' ya se encuentra registrado.\n")
    return

  try:
    precio = float(input(f"Ingrese el precio de {sabor_nuevo} (CLP): "))
    stock = int(input(f"Ingrese el stock inicial de {sabor_nuevo} (unidades): "))
    
    if precio < 0 or stock < 0:
      print("[ERROR] Los valores monetarios y de stock deben ser positivos.")
      return
        
    # creación dinámica de un nuevo nodo diccionario
    nuevo_item = {"sabor": sabor_nuevo, "precio": precio, "stock": stock}
    
    # mutamos la lista agregando el nuevo elemento
    lista_productos.append(nuevo_item)
    print(f"¡Sabor '{sabor_nuevo}' registrado exitosamente!")
      
  except ValueError:
    print("[ERROR] Entrada inválida. El precio debe ser decimal y el stock entero.")


def desplegar_sistema():
  # carga de la estructura de datos seleccionada
  inventario = inicializar_inventario()
  
  while True:
    print("   HELADERÍA FROSTY DELIGHTS - PANEL DE CONTROL   ")
    print("1. Visualizar Catálogo de Sabores")
    print("2. Registrar Nuevo Sabor de Helado")
    print("3. Salir del Sistema")
    print("--------------------------------------------------")
    
    opcion = input("Seleccione una opción de 1 a 3 (1-3): ").strip()
    
    if opcion == "1":
      mostrar_sabores(inventario)
    elif opcion == "2":
      agregar_nuevo_sabor(inventario)
    elif opcion == "3":
      print("\nSaliendo del sistema de la heladería. ¡Que tenga un buen día!")
      break
    else:
      print("\n[ERROR] Opción inválida. Seleccione estrictamente 1, 2 o 3.\n")


if __name__ == "__main__":
  desplegar_sistema()
