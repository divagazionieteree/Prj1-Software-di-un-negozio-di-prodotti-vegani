import json
from datetime import datetime

class CommandsCRM:
    
    def aggiungi(product_name, quantity, purchase_price, selling_price, wharehouse_dict):
        
        """
        aggiungi un prodotto al magazzino
        """
        product_dict = {"product_name": product_name, "quantity": quantity, "purchase_prize": purchase_price, "sale_prize": selling_price}        
        wharehouse_dict.append(product_dict)
    
        print(f"AGGIUNTO {quantity} X {product_name}")
    
    def elenca(wharehouse_dict): 
        """
        elenca i prodotto in magazzino
        """
        for item in wharehouse_dict:
            print(item)
    
    
    def vendita(product_name, quantity, sales_dict, wharehouse_dict): 
        """
        registra una vendita effettuata
        """
    
        is_product = 0
    
        for i, val in enumerate(wharehouse_dict):
            if wharehouse_dict[i]["product_name"] == product_name:
                is_product +=1
                prod_index = i
    
        if is_product > 0:
            if wharehouse_dict[i]["quantity"] >= quantity:
                current_date = str(datetime.now())
                cost = wharehouse_dict[prod_index]["purchase_prize"] * quantity
                billing = wharehouse_dict[prod_index]["sale_prize"] * quantity
                selling_dict = {"product_name": product_name, "quantity": quantity, "date": current_date, "cost": cost, "billing": billing }        
                sales_dict.append(selling_dict)
                wharehouse_dict[prod_index]["quantity"] -= quantity
            else:
               print("non ci sono abbastanza prodotti")
        
        else:
            print("prodotto non presente")
    
    def profitti(sales_dict): 
        """
        mostra i profitti totali
        """
        total_cost = 0
        total_billing = 0
    
        for i, val in enumerate(sales_dict):
            total_cost = total_cost + sales_dict[i]["cost"]
            total_billing = total_billing + sales_dict[i]["billing"]
    
        total_margin = total_billing - total_cost
        print(f"Il fatturato totale è: {total_billing}")
        print(f"Il margine totale è: {total_margin}")
    
    def aiuto(): 
        """
        mostra i possibili comandi
        """
        str_aiuto = " I comandi disponibili sono i seguenti: \n aggiungi: aggiungi un prodotto al magazzino \n elenca: elenca i prodotto in magazzino \n vendita: registra una vendita effettuata \n profitti: mostra i profitti totali \n aiuto: mostra i possibili comandi \n chiudi: esci dal programma"
        print(str_aiuto)
    
    def chiudi(wharehouse_json, sales_json, wharehouse_dict, sales_dict): 
        """
        esci dal programma e salva le variabili nei json
        """
    
        with open(wharehouse_json, "w") as outfile:
            json.dump(wharehouse_dict, outfile)
        
        with open(sales_json, "w") as outfile:
            json.dump(sales_dict, outfile)
    
        return print("Grazie e Buona giornata")