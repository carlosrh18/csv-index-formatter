import sys
import pandas as pd
import uuid


if __name__ == '__main__':
    headers_check = None
    index_at_one = None
    if len(sys.argv) > 1:
        file_name = str(sys.argv[1])
    if len(sys.argv) > 2:
        headers_check = str(sys.argv[2]) or None
    if len(sys.argv) > 3:
        index_at_one = str(sys.argv[3]) or None


    print(len(sys.argv))
    filepath = './'+file_name
    new_file = './'+'csv_de_mi_tio'+str(uuid.uuid4().hex)+'.csv'
    if headers_check == '--no-headers':
        df = pd.read_csv(filepath, header=None)
    else:
        df = pd.read_csv(filepath)
    fst_col = df.columns[0]

    if index_at_one == '--index-at-one':
        df.index = df.index +1
    elif index_at_one == '--tio':
        print('para mi tio favorito')

    df = df.drop([fst_col], axis=1)
    df.to_csv(new_file)

