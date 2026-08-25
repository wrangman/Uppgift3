import csv
import subprocess
import locale



def format_currency(value):
   return locale.currency(value,grouping=True)


def list_products(products):
   for idx, product in enumerate(products, 1):
      name = product['name']
      price = format_currency(product['price'])
      quantity = product['quantity']

      print(f"{idx}) {name} \t {price} \t {quantity:<5}")


def view_product(idx, products):
   subprocess.run('cls', shell=True)
   
   product = products[idx - 1]
   
   print(f"VISAR PRODUKT MED ID: #{product['id']}")
   print("="*40)
   print("Namn:", product['name'])
   print("Beskr.:", product['desc'])
   print("Pris:", product['price'])
   print("Kvanitet:", product['quantity'], end="\n\n")


def add_product(products):
   
   find_max = max(products, key=lambda id: id['id'])
   max_id = find_max['id']
   
   new_id = max_id + 1

   name = input("Namn:")
   desc = input("Beskr.:")
   price = float(input("Pris:"))
   quantity = int(input("Antal:"))
   
   product = {}

   product['id'] = new_id
   product['name'] = name
   product['desc'] = desc
   product['price'] = price
   product['quantity'] = quantity

   products.append(product)
   
   return product
   


   
def load_data(filename): 
   products = []           #lista
   
   with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
      reader = csv.DictReader(file)
      for row in reader:
         id = int(row['id'])
         name = row['name']
         desc = row['desc']
         price = float(row['price'])
         quantity = int(row['quantity'])
         
         products.append(
               {                   
                  "id": id,       
                  "name": name,
                  "desc": desc,
                  "price": price,
                  "quantity": quantity
               }
         )
         
   return products


#TODO: hur gör man så funktionen load_data returnerar products istället?
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id

   # found_max = max(products, key=lambda id: id['id'])
   # max_id = found_max['id']
   # new_id = max_id + 1
   
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

subprocess.run('cls',shell=True)

products = load_data('db_products.csv')


while True:
   list_products(products)
   
   print("-" * 140)
   option = input("Vad vill du göra? [# = visa produkt | L = lägg till | T = ta bort | E = ändra | Q = avsluta] ")
   
   if option.isnumeric():
      idx = int(option)
      
      if 0 < idx <= len(products):   
         view_product(idx, products)
         input()

   else:
      if option.upper() == "L":
         product = add_product(products)
         print(f"Lade till produkt: {product['name']}")
         input()