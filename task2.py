def get_cats_info(path):
    try:
        with open(path, mode='r') as fh:
            all_file = fh.read().split('\n')
            cats = []
            for item in all_file:
                if (len(item) >= 3):
                    id, name, age = item.split(',')
                    cats.append({"id": id, "name": name, "age": age})
            return (cats)
    except FileNotFoundError:
        return ("This file doesn`t exist!")


cats_info = get_cats_info("cats.txt")
print(cats_info)
