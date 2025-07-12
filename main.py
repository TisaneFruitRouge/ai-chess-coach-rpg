from state import State
from state_graph import graph

def main():
    initial_state = State(
        current_room=1,
        user_move=None,
        correct_move=None,
        fen=None,
        result=None
    )

    final_state = graph.invoke(initial_state)
    print(final_state)


if __name__ == "__main__":
    main()
