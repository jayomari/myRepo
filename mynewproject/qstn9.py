#!/usr/bin/env python3

def concatenate_strings(*args, sep=" "):
    """
    This function concatenates strings that have been passed to it.
    """
    return sep.join(args)

print(concatenate_strings("My","Very","Educated","Mother","just","showed","us","nine","planets"))