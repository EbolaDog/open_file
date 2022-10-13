def line_sorting(*files):
    line = {}
    for file in files:
        with open(file, encoding='utf-8') as file_1:
            line.update({file: len(file_1.readlines())})
    lines = {}
    for fl in sorted(line, key=line.get):
        lines[fl] = line[fl]
    return lines

def entry(*files):
    dict_file = {}
    for file in line_sorting('files/1.txt', 'files/2.txt', 'files/3.txt'):
        with open(file, encoding='utf-8') as file_1:
            f = file_1.read()
            dict_file.update({file: f})
    
    for key, meaning in dict_file.items():
        with open('files/rez.txt', 'a', encoding='utf-8') as file:
            file.writelines([f"\n{key}\n{line_sorting(*files)[key]}\n{meaning}\n"])

entry('files/1.txt', 'files/2.txt', 'files/3.txt')