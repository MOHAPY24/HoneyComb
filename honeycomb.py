from errors_tokens import *
from astnode import *


class Token:
    def __init__(self, Name, Type):
        self.name = Name
        self.type = Type
    
    def __str__(self):
        return f"[{self.name}]:[{self.type}]"
    
    def __repr__(self):
        return self.__str__()
    

class Interperter:
    def __init__(self, code:str=None):
        self.code = code
        self.code_pointer = 0
        self.xptr = 0
        self.ccombx = 0
        self.ccomby = 0
        self.yptr = 0
        self.xtape = [[0] * 30, [0] * 30, [0] * 30, [0] * 30, [0] * 30]
        self.ytape = [[0] * 30, [0] * 30, [0] * 30, [0] * 30, [0] * 30]  
        self.outputs = []
        self.current_token = Token(None, "None")
        self.steps = 0
        self.comment_mode = False

    def add_code(self, code:str):
        self.code = code
        self.code_pointer = 0

    def error(self):
        raise Exception("Error occured in interpertation")

    def tokenize(self):
            if self.code_pointer > len(self.code) -1:
                return Token(None, "EOF")
        
            current_char = self.code[self.code_pointer]
            self.code_pointer += 1

            if current_char == "+" and self.comment_mode != True:
                token = Token("+", TOKENS.get("+"))
                return token
            elif current_char == "-" and self.comment_mode != True:
                token = Token("-", TOKENS.get("-"))
                return token
            elif current_char == "." and self.comment_mode != True:
                token = Token(".", TOKENS.get("."))
                return token
        
            else:
                raise SyntaxError(f'{current_char} is not valid syntax.')    


    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.tokenize()
        else:
            self.error()

    def adr(self):
        cmd = self.current_token.name
        if cmd == "+":
            self.xtape[self.ccombx][self.xptr] += 1
        else:
            self.error()
        

    def mdr(self):
        cmd = self.current_token.name
        if cmd == "-":
            self.xtape[self.ccombx][self.xptr] -= 1
        else:
            self.error()

    def prv(self):
        cmd = self.current_token.name
        if cmd == ".":
            print(self.xtape[self.ccombx][self.xptr])
        else:
            self.error()
    
    
    def parse(self):
        ast = []
        self.current_token = self.tokenize()
        while self.current_token.type != "EOF":
            cmd1 = self.current_token.name
            if "+" in cmd1:
                self.adr()
                ast.append(Increment())
            elif "-" in cmd1:
                self.mdr()
                ast.append(Decrement())
            elif "." in cmd1:
                self.prv()
                ast.append(PrintVal())
            else:
                raise SyntaxError(f'{cmd1} is not valid syntax.')
            self.current_token = self.tokenize()
        


    
    

