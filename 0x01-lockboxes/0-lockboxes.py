#!/usr/bin/python3
'''0-lockboxes.py'''


def canUnlockAll(boxes):
    '''0-lockboxes.py'''
    opened = {0}
    keys = [b for b in boxes[0] if b not in opened]
    while keys:
        key = keys.pop()
        opened.add(key)
        keys.extend([b for b in boxes[key] if b not in opened])
    return len(opened) == len(boxes)
