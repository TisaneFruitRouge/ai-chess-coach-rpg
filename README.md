# ai-chess-coach-rpg

A RPG game that makes you solve puzzles in chess.
You will be walked though 6 levels where you will have to solve mate-in-1 puzzles, each time using a different chess piece:
- Level 1: Pawn
- Level 2: Knight
- Level 3: Bishop
- Level 4: Rook
- Level 5: Queen
- Level 6: King

## Using:
- Langraph, Langchain, Python, uv

## Setup and Installation

1. **Prerequisites**:
   - Python 3.12 or higher
   - [uv](https://github.com/astral-sh/uv) - Modern Python package manager and environment management tool

2. **Clone the repository**:
   ```bash
   git clone https://github.com/TisaneFruitRouge/ai-chess-coach-rpg.git
   cd ai-chess-coach-rpg
   ```

3. **Set up a virtual environment and install dependencies using uv**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

## Running the Game

To run the chess puzzle RPG:

```bash
# Make sure your virtual environment is activated
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Run the main script
python main.py
```
