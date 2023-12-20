from typing import List


def line(katz_deli: List[str]) -> str:
    List = []
    if not katz_deli:
        return "The line is currently empty."
    
    # current_line = "The line is currently:"
    # for i, name in enumerate(katz_deli, 1):
    #     current_line += f" {i}. {name}"
    # return current_line

def take_a_number(katz_deli: List[str], name: str) -> None:
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")
    
def now_serving(katz_deli: List[str]) -> None:
    if not katz_deli:
        print("There is nobody waiting to be served!")
        return
    
    name = katz_deli.pop(0)
    print(f"Currently serving {name}.")