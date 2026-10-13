"""Seminar 5 - In-class code"""

name_to_score = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanellie': 9}
width = max(len(name) for name in name_to_score)
# print(width)
# TODO: get sorting working (by score, high-to-low)
for name, score in name_to_score.items():
    print(f"{name:{width}} = {score:3}")
