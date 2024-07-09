import os

def create_file(path:str, name_db="data.db"):
    file_name = ".env"
    content=""
    with open(file=file_name, mode="w+") as config_file:
        content = f'DATABASE="{path + os.path.sep}{name_db}"'
        
        config_file.write(content)
        

if __name__ == "__main__":
    create_file(os.path.abspath("."))
    