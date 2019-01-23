# Minimax
For most multi-player turn based games, the most basic advarsarial search algorithm is Minimax; which finds a path to the most optimal game state. The main loop alternates between players (in this case 2), one player minimizing the evaluation of the board (a smaller value indicates a better position for that team) and the other maximizing it (a greater value indicating a better position for them). Minimax claculates all possible outcomes from the current position and follows the path that leads to the best outcome for its team (highest value) and the lesser outcome for it's opponent, it maximizes the minimum of the opponents evaluation.

<pre>
        1          -> X (Minimizing player)
     /     \
   8         1     -> O (Maximizing player)
  / \       / \ 
-12  8     1  -3   -> X
</pre>

Example output:
<pre>
Move: 1 1
X - - 
- - - 
- - - 

X - - 
- O - 
- - - 

Move: 3 3
X - - 
- O - 
- - X 

X O - 
- O - 
- - X 

  .
  .
  .

X O X 
- O O 
O X X 

Move: 1 2
X O X 
X O O 
O X X 
</pre>
