import pandas as pd
import sys
import ntpath

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


for file in sys.argv[1:]:
    droppedFile = file
    df = pd.read_csv(droppedFile)
    file_path = droppedFile.split('.')
    folder_name = ntpath.dirname(droppedFile)
    folder_name = path_leaf(folder_name)
    df.columns = df.columns[:2].union(folder_name+ '_' + df.columns[2:])
    df.to_csv(file_path[0] + '_edit.' + file_path[1], index=False)






