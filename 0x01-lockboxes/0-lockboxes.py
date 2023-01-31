#!/usr/bin/python3
'''0-lockboxes.py'''


def canUnlockAll(boxes):
    '''0-lockboxes.py'''
    opened_boxes = set([0])
    keys = boxes[0]
    while keys:
        key = keys.pop()
        if key not in opened_boxes:
            opened_boxes.add(key)
            keys += boxes[key]
    return len(opened_boxes) == len(boxes)
