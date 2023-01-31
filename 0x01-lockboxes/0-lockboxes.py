#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """

    def canUnlockAll(boxes):
        opened = [0]
        for i in boxes[0]:
            if i < len(boxes) and i not in opened:
                opened.append(i)
                for j in boxes[i]:
                    if j < len(boxes) and j not in opened:
                        opened.append(j)
        return len(opened) == len(boxes)
