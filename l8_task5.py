"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь."""
from l8_task4 import Printer, Scan, Xerox

test = Xerox
test_2 = Printer
test_3 = Scan

inquiry = {
            'item': test.name,
            'color': test.color,
            'material': test.material,
            'weight': test.weight
           }

print(inquiry)
print(type(inquiry))

