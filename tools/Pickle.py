import pickle
from Classes.Aircraft import Aircraft as ac

teste = ac("TP-336","boeing","747SP","PW JT9D7A","980",10800,20.24,0.26,400,350)

def dump(content, file: str):
    """
    Method that returns a simple confirmation string ("Done!") everytime the method is called, although it's not catching or managing any error (This is something that needs to be improved in the next versions).

    Args:
        content (Any): Any content that relates to the content already written in the file "file".
        file (str): The file where the contents is going to be saved.

    Returns:
        str: Confirmation string
    """
    with open(file, "wb") as current_file:
        pickle.dump(content, current_file)

    return "done!"

def load(file:str):
    with open(file, "rb") as current_file:
        file = pickle.load(current_file)
        print(file)

dump(teste, "fleet.txt")