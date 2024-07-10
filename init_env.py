import os


def create_venv(path: str, name_db="data.db"):
    file_name = ".env"
    abspath = ""
    with open(file=file_name, mode="w+") as config_file:
        abspath = f'"{path + os.path.sep}{name_db}"'
        content = f'DATABASE={abspath}'    
        config_file.write(content)
    
    return abspath


def create_config(path_env):
    """Create a file config with the path for ".env" file"""
    filename = "config.py"

    if os.path.exists(".env"):
        with open(file=f"./src{os.path.sep + filename}", mode="w+") as file:
            content = f'path_env = "{os.path.abspath(".env")}"'
            file.write(content)
    else:
        create_venv(".")

if __name__ == "__main__":
    path_env = create_venv(os.path.abspath("."))
    create_config(path_env=path_env)
