from errors_tokens import *
from astnode import *
import datetime
from os import path



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
        self.ymode = False

    def add_code(self, code:str):
        self.code = code.replace('\n', '').replace('\t', '').replace(' ', '')
        self.code_pointer = 0
    
    def load_file_code(self, filename:str=None):
        if filename and filename.endswith('.hc') and path.exists(filename):
            f = open(filename, 'r')
            self.code = f.read().replace('\n', '').replace('\t', '').replace(' ', '')
            self.code_pointer = 0
            f.close()
        else:
            raise FileNotFoundError(f"File does not exist, wasnt given or not using '.hc' file extension.")

    def error(self):
        raise UnrecognizedToken(self.current_token.name, self.code_pointer - 1)

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
                elif current_char == ">" and self.comment_mode != True:
                    token = Token(">", TOKENS.get(">"))
                    return token
                elif current_char == "<" and self.comment_mode != True:
                    token = Token("<", TOKENS.get("<"))
                    return token
                elif current_char == "^" and self.comment_mode != True:
                    token = Token("^", TOKENS.get("^"))
                    return token 
                elif current_char == "V" and self.comment_mode != True:
                    token = Token("V", TOKENS.get("V"))
                    return token
                elif current_char == "W" and self.comment_mode != True:
                    token = Token("W", TOKENS.get("W"))
                    return token
                elif current_char == "/" and self.comment_mode != True:
                    token = Token("/", TOKENS.get("/"))
                    return token
                elif current_char == "," and self.comment_mode != True:
                    token = Token(",", TOKENS.get(","))
                    return token
                elif current_char == ":" and self.comment_mode != True:
                    token = Token(":", TOKENS.get(":"))
                    return token
                elif current_char == "(" and self.comment_mode != True:
                    token = Token("(", TOKENS.get("("))
                    return token
                elif current_char == ")":
                    token = Token(")", TOKENS.get(")"))
                    return token
                elif current_char == "!" and self.comment_mode != True:
                    token = Token("!", TOKENS.get("!"))
                    return token
                elif current_char == "~" and self.comment_mode != True:
                    token = Token("~", TOKENS.get("~"))
                    return token
                elif current_char == "%" and self.comment_mode != True:
                    token = Token("%", TOKENS.get("%"))
                    return token
                elif current_char == "S" and self.comment_mode != True:
                    token = Token("S", TOKENS.get("S"))
                    return token
                elif current_char == "*" and self.comment_mode != True:
                    token = Token("*", TOKENS.get("*"))
                    return token
                elif current_char == "&" and self.comment_mode != True:
                    token = Token("&", TOKENS.get("&"))
                    return token
                elif current_char == "#" and self.comment_mode != True:
                    token = Token("#", TOKENS.get("#"))
                    return token
                elif current_char.isdigit() and self.comment_mode != True:
                    token = Token(current_char, 'INT')
                    return token
                elif current_char == "[" and self.comment_mode != True:
                    token = Token("[", TOKENS.get("["))
                    return token
                elif current_char == "]" and self.comment_mode != True:
                    token = Token("]", TOKENS.get("]"))
                    return token
        
                else:
                    if self.comment_mode:
                        return Token('comment', 'comment')
                    raise SyntaxError(f'{datetime.datetime.now()}: {current_char} is not valid syntax.')    


    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.tokenize()
        else:
            self.error()

    def adr(self):
        cmd = self.current_token.name
        if cmd == "+":
            if self.ymode:
                self.ytape[self.ccomby][self.yptr] += 1
            else:
                self.xtape[self.ccombx][self.xptr] += 1
        else:
            self.error()
        

    def mdr(self):
        cmd = self.current_token.name
        if cmd == "-":
            if self.ymode:
                self.ytape[self.ccomby][self.yptr] -= 1
            else:
                self.xtape[self.ccombx][self.yptr] -= 1
        else:
            self.error()

    def prv(self):
        cmd = self.current_token.name
        if cmd == ".":
            if self.ymode:
                print(self.ytape[self.ccomby][self.yptr])
            else:
                print(self.xtape[self.ccombx][self.xptr])
            self.outputs.append(self.xtape[self.ccombx][self.xptr])
        else:
            self.error()
    
    def nxcx(self):
        cmd = self.current_token.name
        if cmd == ">":
            self.xptr += 1
            self.ymode = False
        else:
            self.error()
    
    def pcx(self):
        cmd = self.current_token.name
        if cmd == "<" and self.xptr != 0:
            self.xptr -= 1
            self.ymode = False
        else:
            self.error()
    
    def ncy(self):
        cmd = self.current_token.name
        if cmd == "^":
            self.yptr += 1
            self.ymode = True
        else:
            self.error()
    
    def pcy(self):
        cmd = self.current_token.name
        if cmd == "V" and self.yptr != 0:
            self.yptr -= 1
            self.ymode = True
        else:
            self.error()
    
    def nxcc(self):
        cmd = self.current_token.name
        if cmd == "/":
            if self.ymode:
                self.ccomby += 1
            else:
                self.ccombx += 1
        else:
            self.error()
    
    def prcc(self):
        cmd = self.current_token.name
        if cmd == "W":
            if self.ymode:
                self.ccomby -= 1
            else:
                self.ccombx -= 1
        else:
            self.error()

    def prca(self):
        cmd = self.current_token.name
        if cmd == ",":
            if self.ymode:
                print(chr(self.ytape[self.ccomby][self.yptr]), end='')
            else:
                print(chr(self.xtape[self.ccombx][self.xptr]), end='')
        else:
            self.error()
    
    def cli(self):
        cmd = self.current_token.name
        if cmd == ":":
            if self.ymode:
                try:
                    self.ytape[self.ccomby][self.yptr] += int(input("> "))
                except ValueError:
                    raise ValueError("Input not int_type.")
            else:
                try:
                    self.xtape[self.ccombx][self.xptr] += int(input("> "))
                except ValueError:
                    raise ValueError("Input not int_type.")
        else:
            self.error()

    def cmst(self):
        cmd = self.current_token.name
        if cmd == "(":
            self.comment_mode = True
        else:
            self.error()
    
    def cmen(self):
        cmd = self.current_token.name
        if cmd == ")":
            self.comment_mode = False
        else:
            self.error()
    
    def clrt(self):
        cmd = self.current_token.name
        if cmd == "%":
            if self.ymode:
                self.ytape = [[0] * 30, [0] * 30, [0] * 30, [0] * 30, [0] * 30]  
            else:
                self.xtape = [[0] * 30, [0] * 30, [0] * 30, [0] * 30, [0] * 30]
        else:
            self.error()
    
    def clrcmb(self):
        cmd = self.current_token.name
        if cmd == "~":
            if self.ymode:
                self.ytape[self.ccomby] = [0] * 30
            else:
                self.xtape[self.ccombx] = [0] * 30
        else:
            self.error()

    def clrcl(self):
        cmd = self.current_token.name
        if cmd == "!":
            if self.ymode:
                self.ytape[self.ccomby][self.yptr] = 0
            else:
                self.xtape[self.ccombx][self.xptr] = 0
        else:
            self.error()
    
    def sqrcl(self):
        cmd = self.current_token.name
        if cmd == "S":
            if self.ymode:
                self.ytape[self.ccomby][self.yptr] *= self.ytape[self.ccomby][self.yptr]
            else:
                self.xtape[self.ccombx][self.xptr] *= self.xtape[self.ccombx][self.xptr]
        else:
            self.error()
    
    def svpl(self):
        cmd = self.current_token.name
        if cmd == "*":
            if self.ymode:
                self.save = self.ytape[self.ccomby][self.yptr]
            else:
                self.save = self.xtape[self.ccombx][self.xptr]
        else:
            self.error()
    
    def ldpl(self):
        cmd = self.current_token.name
        if cmd == "&":
            if self.ymode:
                self.ytape[self.ccomby][self.yptr] = self.save
            else:
                self.xtape[self.ccombx][self.xptr] = self.save
        else:
            self.error()

    def ifo(self):
        cmd = self.current_token.name
        if cmd == "#":
            if self.ymode:
                if self.ytape[self.ccomby][self.yptr] == 0:
                    self.yptr = int(self.code[self.code_pointer + 1])
            else:
                if self.xtape[self.ccombx][self.xptr] == 0:
                    self.xptr = int(self.code[self.code_pointer + 1])
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
            elif ">" in cmd1:
                self.nxcx()
                ast.append(CellRight())
            elif "<" in cmd1:
                self.pcx()
                ast.append(CellLeft())
            elif "^" in cmd1:
                self.ncy()
                ast.append(CellUp())
            elif "V" in cmd1:
                self.pcy()
                ast.append(CellDown())
            elif "W" in cmd1:
                self.prcc()
                ast.append(PreviousComb())
            elif "/" in cmd1:
                self.nxcc()
                ast.append(NextComb())
            elif "," in cmd1:
                self.prca()
                ast.append(PrintAscii())
            elif ":" in cmd1:
                self.cli()
                ast.append(CellInput())
            elif "(" in cmd1:
                self.cmst()
                ast.append(CommentStart())
            elif ")" in cmd1:
                self.cmen()
                ast.append(CommentEnd())
            elif "!" in cmd1:
                self.clrcl()
                ast.append(ClearCell())
            elif "~" in cmd1:
                self.clrcmb()
                ast.append(ClearComb())
            elif "%" in cmd1:
                self.clrt()
                ast.append(ClearTape())
            elif "S" in cmd1:
                self.sqrcl()
                ast.append(SquareCell())
            elif "*" in cmd1:
                self.svpl()
                ast.append(SavePollen())
            elif "&" in cmd1:
                self.ldpl()
                ast.append(LoadPollen())
            elif "#" in cmd1:
                self.ifo()
                ast.append(If0())
            elif "comment" in cmd1:
                pass
            elif "INT" in self.current_token.type:
                pass
            else:
                raise UnmappedToken(cmd1, self.code_pointer - 1)
            self.current_token = self.tokenize()
        


    
    

