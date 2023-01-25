def read_from_file(filepath):
    with open(filepath, 'r') as f_o:
        typ = f_o.readlines()
        return typ


print(read_from_file("prodfile.txt"))
