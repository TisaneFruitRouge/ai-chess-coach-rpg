
from langgraph.graph import StateGraph, START, END
from consts import NUMBER_OF_LEVELS
from graph_nodes import (
    game_start,
    load_room,
    get_user_move,
    check_solution,
    wrong_move,
    right_move,
    end_game
)
from state import State

def check_result_edge(state: dict) -> str:
    return "success" if state["result"] == "success" else "fail"

def check_next_room(state: dict) -> str:
    return "end" if state['current_room'] > NUMBER_OF_LEVELS else "next"

graph_builder = StateGraph(State)

# Creating nodes
graph_builder.add_node("game_start", game_start)
graph_builder.add_node("load_room", load_room)
graph_builder.add_node("get_user_move", get_user_move)
graph_builder.add_node("check_solution", check_solution)
graph_builder.add_node("wrong_move", wrong_move)
graph_builder.add_node("right_move", right_move)
graph_builder.add_node("end_game", end_game)

# Creating edges
graph_builder.add_edge(START, "game_start")
graph_builder.add_edge("game_start", "load_room")
graph_builder.add_edge("load_room", "get_user_move")
graph_builder.add_edge("get_user_move", "check_solution")
graph_builder.add_conditional_edges(
    "check_solution",
    check_result_edge,
    {
        "success": "right_move",
        "fail": "wrong_move"
    }
)
graph_builder.add_edge("wrong_move", "get_user_move")
graph_builder.add_conditional_edges(
    "right_move",
    check_next_room,
    {
        "end": "end_game",
        "next": "load_room"
    }
)
graph_builder.add_edge("end_game", END)

graph = graph_builder.compile()
