# Battleship Game

This is a simple command-line implementation of the classic Battleship game for a single player, played on a 5x5 grid in the Python terminal.

## How to Play

1. **Setup**: The computer randomly places 3 ships on a 5x5 grid.
2. **Gameplay**: 
   - Enter your guess in the format `row,col` (e.g., `2,3` for row 2, column 3).
   - Try to find and sink all the ships by guessing their locations.
   - Each turn, the game will show you your current grid:
     - `.` - unguessed
     - `O` - miss
     - `X` - hit
3. **Win Condition**: Sink all 3 ships to win. The game will show the final grid with all ship locations revealed.

## Running the Game

1. Make sure you have Python 3 installed.
2. Download or copy the `battleship.py` file from this repository.
3. Run the game in your terminal:

   ```bash
   python battleship.py
   ```

## Example

```
Welcome to Battleship!
  1 2 3 4 5
1 . . . . .
2 . . . . .
3 . . . . .
4 . . . . .
5 . . . . .
Enter your guess (row,col, e.g. 2,3): 2,3
Miss!
...
Congratulations! You sank all the ships in 10 turns.
Final grid (S = ship, X = hit, O = miss):
  1 2 3 4 5
1 . O . . .
2 . X . . .
3 S . . . .
4 . . X . .
5 . . . O .
```

## License

This project is provided for educational and personal use. Feel free to modify and share!
