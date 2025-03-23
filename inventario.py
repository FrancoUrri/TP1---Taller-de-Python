inventory = {}
def main_menu():
	options = [
	"Agregar producto",
	"Eliminar producto",
	"Mostrar inventario",
	"Salir"
	]
	menu = enumerate(options)
	print("Seleccione la opción deseada:")
	for option in menu:
		print(option[0] + 1, "-", option[1])
	user_choice = input()
	return user_choice
def add_item(inventory):
	new_item = input("Ingrese el producto que desea agregar: ")
	new_item = new_item.capitalize()
	new_item_amount = int(input("Ingrese la cantidad que desea agregar: "))
	if new_item in inventory:
		new_item_amount = inventory[new_item] + new_item_amount
	inventory[new_item] = new_item_amount
	print("¡Producto agregado!")
	return inventory
def delete_item(inventory):
	item_to_delete = input("Ingrese el producto que desea eliminar: ")
	item_to_delete = item_to_delete.capitalize()
	if item_to_delete not in inventory:
		print("Producto inexistente")
	else:
		inventory.pop(item_to_delete)
		print("¡Producto eliminado!")
	return inventory
def show_inventory(inventory):
	for item in inventory:
		print(f'{item}: {inventory[item]} unidades')
		print("")
user_choice = main_menu()
while user_choice != "4":
	if user_choice == "1":
		add_item(inventory)
	elif user_choice == "2":
		delete_item(inventory)
	elif user_choice == "3":
		show_inventory(inventory)
	elif user_choice == "4":
		exit()
	else:
		print("Opción inválida. Por favor ingrese un número del 1 al 4")
		user_choice = main_menu
	input("Presione intro para continuar")
	user_choice = main_menu()

