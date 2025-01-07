from multiprocessing import Pool
from time import time


def read_info(name):
    all_data = []
    with open(name, "r") as f:
        while True:
            num = f.readline()
            if not num:
                break
            all_data.append(int(num.strip()))

if __name__ == "__main__":

    files = [
        "file 1.txt",
        "file 2.txt",
        "file 3.txt",
        "file 4.txt"
    ]

    """st = time()
    for file in files:
        read_info(file)
    end = time()
    print(end-st)"""


    st = time()
    with Pool(processes=4) as pool:
        if __name__ == '__main__':
            pool.map(read_info, files)
    end = time()
    print(end - st)