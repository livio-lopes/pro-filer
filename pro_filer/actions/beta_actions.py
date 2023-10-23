"""Arquivo que estudantes devem editar"""
# Abrindo o PR


def len_path_file(path_file):
    return len(path_file.split("/"))


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=len_path_file)
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name = file_name.lower()
            search_term = search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files


# code snippet to debug using vscode
if __name__ == "__main__":
    test = {
        "all_files": [
            "/home/trybe/Downloads/trybe_logo.png",
            "/home/trybe/Documents/aula/python/tests.txt",
        ]
    }

    # test = {
    #     "all_files": [
    #     ]
    # }

    find_file_by_name(test, "TESTS", case_sensitive=False)
