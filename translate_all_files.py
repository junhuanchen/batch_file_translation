
import os


def tree_files(dir_):
    if not os.path.isdir(dir_):
        return [dir_]
    res = []
    for item in os.listdir(dir_):
        item = os.path.join(dir_, item)
        res.extend(tree_files(item))
    return res


def get_file_type(file):
    return os.path.splitext(file)[-1]


def all_mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    return os.path.exists(path)


def extract_file(source_dir='test', goal_dir='result\\', file_set=['.txt', '.rst', '.md'], function=lambda t:t):
    files = tree_files(source_dir)
    # print(files)
    for fe in files:
        print(fe)
        if get_file_type(fe) in file_set:

            res = ''

            with open(fe, 'r', encoding='utf-8') as f:
                # print(f.read())
                res = f.read()

            path = os.path.dirname(fe)
            all_mkdir(goal_dir + path)

            res = function(res)

            with open(goal_dir + fe, 'w', encoding='utf-8') as f:
                (f.write(res))

def test(t):
    return 'test\n' + t 

if __name__ == "__main__":
    extract_file(function=test)
