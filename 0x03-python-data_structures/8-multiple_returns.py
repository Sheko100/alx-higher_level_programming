#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    firstchar = sentence[0] if (strlen > 0) else None
    strobj = strlen, firstchar
    return (strobj)
