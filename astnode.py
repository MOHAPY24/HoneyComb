class ASTNode:
    pass

class Increment(ASTNode):
    def __init__(self):
        self.op = '+'

    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class Decrement(ASTNode):
    def __init__(self):
        self.op = '-'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()


class PrintVal(ASTNode):
    def __init__(self):
        self.op = '.'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class PrintAscii(ASTNode):
    def __init__(self):
        self.op = ','
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class CellInput(ASTNode):
    def __init__(self):
        self.op = ':'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class CommentStart(ASTNode):
    def __init__(self):
        self.op = '('
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class CommentEnd(ASTNode):
    def __init__(self):
        self.op = ')'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class ClearTape(ASTNode):
    def __init__(self):
        self.op = '%'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()
    
class ClearComb(ASTNode):
    def __init__(self):
        self.op = '~'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()
    

class ClearCell(ASTNode):
    def __init__(self):
        self.op = '!'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class SquareCell(ASTNode):
    def __init__(self):
        self.op = 'S'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class LoadPollen(ASTNode):
    def __init__(self):
        self.op = '&'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class SavePollen(ASTNode):
    def __init__(self):
        self.op = '*'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class PreviousComb(ASTNode):
    def __init__(self):
        self.op = 'W'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()
    
class NextComb(ASTNode):
    def __init__(self):
        self.op = '/'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()


class CellDown(ASTNode):
    def __init__(self):
        self.op = 'V'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class CellUp(ASTNode):
    def __init__(self):
        self.op = '^'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class CellRight(ASTNode):
    def __init__(self):
        self.op = '>'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class CellLeft(ASTNode):
    def __init__(self):
        self.op = '<'
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class CommentChar(ASTNode):
    def __init__(self, comment):
        self.op = comment
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class If0(ASTNode):
    def __init__(self):
        self.op = "#"
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()
    
    
class LpS(ASTNode):
    def __init__(self):
        self.op = "["
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()

class LpE(ASTNode):
    def __init__(self):
        self.op = "]"
    
    def __str__(self):
        return self.op
    
    def __repr__(self):
        return self.__str__()
    
ALL_AST_NODES = list(ASTNode.__subclasses__())