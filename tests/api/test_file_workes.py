from file_workers import read_from_file


def add_data_file(test_data):
    with open("prodfile.txt", "a") as f_o:
        f_o.writelines(test_data)


def test_read_file():
    test_data = ['10\n', '21\n', '32\n']
    add_data_file(test_data)
    assert test_data == read_from_file("prodfile.txt")
