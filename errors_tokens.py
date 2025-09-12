TOKENS = {
    "+" : "ADD_CELL",
    "-" : "MINUS_CELL",
    ">" : "CELL_LEFT",
    "<" : "CELL_RIGHT",
    "^" : "CELL_UP",
    "V" : "CELL_DOWN",
    "/" : "NEXT_COMB",
    "W" : "PREVIOUS_COMB",
    "*" : "SAVE_POLLEN",
    "&" : "LOAD_POLLEN",
    "S" : "SQUARE_CELL",
    "!" : "CLEAR_CELL",
    "~" : "CLEAR_COMB",
    "%" : "CLEAR_TAPE",
    "." : "PRINT_CELL_VALUE",
    "," : "PRINT_CELL_ASCII",
    ":" : "CELL_INPUT",
    "(" : "COMMENT_START",
    ")" : "COMMENT_END",
    "]" : "LOOP_END",
    "[" : "LOOP_START",
    "#" : "IF_0"
}


class UnrecognizedToken(Exception):
    def __init__(self, character, position):
        self.character = character
        self.position = position
        super().__init__(f"Unrecognized token '{self.character}' at position {self.position}")
        

class UnmappedToken(Exception):
    def __init__(self, token, position):
        self.token = token
        self.position = position
        super().__init__(f"Unmapped token '{self.token}' at position {self.position}, either your interperter is outdated, the token is not implemented or your interperter install is broken.")
        


TOKENS_LIST = list(TOKENS)