# Rock, Paper, Scissors

This is a mini project created for the portfolio assignment.
A simple console game written in Python. The player chooses rock, paper, or
scissors, and the computer makes a random choice. The game keeps score until
the player quits.

## Program flow

```mermaid
flowchart TD
    A([Start]) --> B[Display welcome screen]
    B --> C[Ask for the player's choice]
    C --> D{Is the choice valid?}
    D -- No --> E[Display an error message]
    E --> C
    D -- Yes --> F{Did the player enter q?}
    F -- Yes --> G[Display final scores]
    G --> H([End])
    F -- No --> I[Generate the computer's choice]
    I --> J[Determine the round winner]
    J --> K[Update the player, computer, or draw score]
    K --> L[Display the round result]
    L --> C
```

## How to run the game

1. Open a terminal in this folder.
2. Run:

   ```bash
   python3 rock_paper_scissors.py
   ```

3. Enter `rock`, `paper`, or `scissors` when asked.
4. Enter `q` to finish the game.

## Game rules

- Rock beats scissors.
- Scissors beats paper.
- Paper beats rock.
- Matching choices result in a draw.
# Rock-Paper-Scissors
