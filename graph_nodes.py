from state import State
from utils import get_solution, load_random_problem, print_board

def game_start(state: State):
    state["current_room"] = 1
    state["result"] = "fail"
    return state

def load_room(state: State):
    level = state["current_room"]
    state["fen"] = load_random_problem(level)
    uci, san = get_solution(state["fen"]).values()
    state["correct_move_uci"] = uci
    state["correct_move_san"] = san
    print(uci, san)
    print_board(state["fen"])
    return state

def get_user_move(state: State):
    user_move = input("Enter your move: ")
    state["user_move"] = user_move
    return state

def check_solution(state: State):
    result = state["user_move"] == state["correct_move_uci"] or state["user_move"] == state["correct_move_san"]
    state["result"] = "success" if result else "fail"
    return state

def wrong_move(state: State):
    return state

def right_move(state: State):
    state["current_room"] += 1
    return state

def end_game(state: State):
    return state
