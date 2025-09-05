TOKENS = {
    "+" : "ADD_CELL",
    "-" : "MINUS_CELL",
    ">" : "CELL_LEFT",
    "<" : "CELL_RIGHT",
    "^" : "CELL_UP",
    "V" : "CELL_DOWN",
    "/" : "NEXT_COMB",
    "\ ".strip() : "PREVIOUS_COMB",
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
    "#" : "IF_0"
}

TOKENS_LIST = list(TOKENS)