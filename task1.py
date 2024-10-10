def total_salary(path):
    try:
        with open(path, mode='r') as fh:
            all_file = fh.read().split('\n')
            salary = []
            for item in all_file:
                if (len(item) >= 2):
                    salary.append(int(item.split(',')[1]))
            return (sum(salary), int(sum(salary)/len(salary)))
    except FileNotFoundError:
        return (0, 0)


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {
      total}, Середня заробітна плата: {average}")
