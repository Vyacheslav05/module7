from pprint import pprint

name = 'products.txt'

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self._file_name = 'products.txt'

    def get_products(self):
        with open(self._file_name, 'r', encoding='utf-8') as file:
            products = file.read()
        return products

    def add(self, *products):
        existing_products = set()
        try:
            with open(self._file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    existing_product = line.strip().split(', ')[0]
                    existing_products.add(existing_product)
        except FileNotFoundError:
            pass

        with open(self._file_name, 'a', encoding='utf-8') as file:
            for products in products:
                if products.name in existing_products:
                    print(f'Продукт {products.name} уже есть в магазине')
                else:
                    file.write(str(products) + '\n')
                    existing_products.add(products.name)

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
