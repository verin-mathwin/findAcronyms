import os
import re

dataPath = r"C:\Users\LiDAR Support Eng\Documents\GitHub\findAcronyms\findAbbrevs_data.txt"

def abbrevFinder(fp):
    """
    Lazily scahs a text file for likely abbreviations and prints their frequency of occurrence.

    Abbreviations are detected based on the following patterns:
    - Consecutive uppercase letters (e.g. NASA, ISO9001)
    - Abbreviations in parentheses (e.g. (GCCC))
    - Dot-separated uppercase initials (e.g. U.S.A.)

    Parameters:
        file_path (str): Path to the text file to be scanned.

    Returns:
        Writes a file "abbrevs.txt" into the host directory, with every matching object.
        May include random other capitalisations. Is not vetted.
    """
    folder = os.path.dirname(fp)
    outName = os.path.join(folder, 'abbrevs.txt')
    abbrevs = []
    with open(fp, 'r', encoding='utf-8') as f:
        t = f.read()
        print(t[:50])
        pattern = r'\b(?:[A-Z]{2,}\d*|(?:[A-Z]\.){2,})\b|\([A-Z]{2,}\d*\)'
        matches = re.findall(pattern, t)
        cleaned = [m.strip('()') for m in matches]
        abbrevs = sorted(list(set(cleaned)))
    with open(outName, 'w') as r:
        for a in abbrevs:
            r.write(a + '\n')

abbrevFinder(dataPath)
