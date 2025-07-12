from typing_extensions import TypedDict


class State(TypedDict):
    current_room: int
    user_move: str | None
    correct_move_uci: str | None
    correct_move_san: str | None
    fen: str | None
    result: str | None         # "success", "fail"
