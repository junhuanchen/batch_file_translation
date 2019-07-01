
def tree_files(dir_):
    if not os.path.isdir(dir_):
        return [dir_]

    res = []
    for item in os.listdir(dir_):
        item = os.path.join(dir_, item)
        res.extend(tree_files(item))
    return res

if __name__ == "__main__":
    tree_files()