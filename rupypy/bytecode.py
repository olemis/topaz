class Bytecode(object):
    _immutable_fields_ = [
        "code", "consts_w[*]", "max_stackdepth", "locals[*]", "cells[*]",
        "arg_locs[*]", "arg_pos[*]"
    ]

    UNKNOWN = 0
    LOCAL = 1
    CELL = 2

    def __init__(self, name, code, max_stackdepth, consts, args, locals, cells):
        self.name = name
        self.code = code
        self.max_stackdepth = max_stackdepth
        self.consts_w = consts
        self.locals = locals
        self.cells = cells

        arg_locs = [self.UNKNOWN] * len(args)
        arg_pos = [-1] * len(args)
        for idx, arg in enumerate(args):
            if arg in locals:
                arg_locs[idx] = self.LOCAL
                arg_pos[idx] = locals.index(arg)
            elif arg in cells:
                arg_locs[idx] = self.CELL
                arg_pos[idx] = cells.index(arg)
        self.arg_locs = arg_locs
        self.arg_pos = arg_pos
