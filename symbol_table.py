
class SymbolTable:
    def __init__(self):
        self.symbol_table={}
        
    def free(self):
        self.symbol_table={}
    
    def lookup(self,name):
        return symbol_table[name]
    
    def insert(self,name):
        if(symbol_table.get(name,None)==None):
            symbol_table[name]={}
            return symbol_table[name]
        return None
    def set_attribute(self,name,attribute_name,attribute_value):
        symbol_table[name][attribute_name]=attribute_value
        
    def get_attribute(self,name,attribute_name):
        return symbol_table[name][attribute_name]
        
        
