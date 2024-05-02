class CommandsCRM:
    
    def __init__(self, product_name: str, quantity: int, purchase_price: float, selling_price: float, wharehouse_dict: list):
    
        """
        __init__ Function
        """
        self.product_name = product_name
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.wharehouse_dict = wharehouse_dict
         
    def aggiungi(self):
        
        """
        aggiungi un prodotto al magazzino
        """
        product_dict = {"product_name": self.product_name, "quantity": self.quantity, "purchase_prize": self.purchase_price, "sale_prize": self.selling_price}        
        self.wharehouse_dict.append(product_dict)
        
        return print(self.wharehouse_dict)
    
    def elenca(self): 
        """
        elenca i prodotto in magazzino
        """
        return print("Hello World")
    
    def vendita(self): 
        """
        registra una vendita effettuata
        """
        return print("Hello World")
    
    def profitti(self): 
        """
        mostra i profitti totali
        """
        return print("Hello World")
    
    def aiuto(self): 
        """
        mostra i possibili comandi
        """
        list_aiuto = ["I comandi disponibili sono i seguenti:",
                      "aggiungi: aggiungi un prodotto al magazzino",
                      "elenca: elenca i prodotto in magazzino",
                      "vendita: registra una vendita effettuata",
                      "profitti: mostra i profitti totali",
                      "aiuto: mostra i possibili comandi",
                      "chiudi: esci dal programma"]
        return print(list_aiuto)
    
    def chiudi(self): 
        """
        esci dal programma
        """
        return print("Hello World")