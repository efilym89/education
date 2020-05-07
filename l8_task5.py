"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь."""
from l8_task4 import Warehouse, Printer, Xerox, Scan

enter = input('Enter item:\n')
enter_2 = int(input('Enter quantity\n'))
if enter == 'xerox':
    item = Xerox
if enter == 'printer':
    item = Printer
if enter == 'scaner':
    item = Scan

product = {'name': item.name,
            'model': item.model,
            'color': item.color,
            'material': item.material,
            'weight': item.weight,
            'quantity': enter_2}

Warehouse.rack.append(product)
print(Warehouse.rack)
