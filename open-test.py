import csv
import subprocess
import locale


def format_currency(value):
   return locale.currency(value,grouping=True)


def list_products(products):
   for idx, product in enumerate(products):
      
      name = product['name']
      price = format_currency(product['price'])
      quantity = product['quantity']

      print(f"{idx}) {name} \t {price} \t {quantity:<5}")


def view_product(idx, products):
   subprocess.run('cls', shell=True)
   
   product = products[idx]

   
   
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


#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv klart funktionen som returnerar en specifik produkt med hjälp av id & products
#TODO: skriv en funkion som skapar en ny produkt - den behöver inte spara till fil!
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
   
   
   if option.isdigit():
      idx = int(option)
      
      if 0 < idx <= len(products):   
         view_product(idx, products)
         input() #bara vänta till tangentbordsklick

   