import random
from typing_extensions import Dict
from rich.style import Style
from stockfish import Stockfish
import chess
from rich.console import Console
from rich.table import Table
from rich.text import Text

from dotenv import load_dotenv
import os

from consts import UNICODE_PIECES

load_dotenv()

def load_random_problem(level: int):
    filename = f"./puzzles-db/puzzles/mate_in_{level}.fen"
    with open(filename, 'r') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

def get_solution(fen: str) -> Dict[str, str]:
    stockfish = Stockfish(path=os.environ['STOCKFISH_ENGINE_PATH'])
    stockfish.set_fen_position(fen)

    best_move_uci = stockfish.get_best_move()
    if not best_move_uci:
        return {"uci": "", "san": ""}

    # Convert UCI to human-readable algebraic notation
    board = chess.Board(fen)
    move = chess.Move.from_uci(best_move_uci)
    best_move_san = board.san(move)  # e.g., "Qxh3"

    return {"uci" : best_move_uci, "san" : best_move_san}

def print_board(fen: str) -> None:
   """Print a chess board with enhanced formatting using rich library."""
   console = Console()
   board = chess.Board(fen)

   # Build the board from rank 8 to 1 (top to bottom) without using Table
   for rank in range(8, 0, -1):
       line = Text(str(rank) + " ", style="dim")
       for file in range(8):
           square = chess.square(file, rank - 1)
           piece = board.piece_at(square)

           if piece:
               piece_symbol = UNICODE_PIECES.get(piece.symbol(), '.')
               if piece.color == chess.WHITE:
                   piece_text = Text(f" {piece_symbol} ", style=Style(color="bright_white", bgcolor="bright_white", bold=True))
               else:
                   piece_text = Text(f" {piece_symbol} ", style=Style(color="grey0", bgcolor="grey0", bold=True))
           else:
               piece_text = Text("   ", style="dim")

           # Alternate square colors (light/dark squares)
           if (rank + file) % 2 == 1:
               piece_text.stylize("on medium_orchid") # black square
           else:
               piece_text.stylize("on royal_blue1") # white square

           line.append_text(piece_text)

       console.print(line)

   console.print("   a  b  c  d  e  f  g  h", style="dim")
