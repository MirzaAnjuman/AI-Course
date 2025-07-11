Algorithm Implementation - AI Lab Submission
1. Breadth-First Search (BFS)
   
How it works: Explores nodes level by level from the start node using a queue (FIFO).

Applications:

Finding shortest path in unweighted graphs

Social networking (degree of connection)

Complexity:

Time: O(V + E)

Space: O(V)

![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/960aeac2c333c6b4f39fb714d549912ecba7f6be/Algorithm%20Implementation/Screenshot_1.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/14df34d50da91ea92bb1e1aba2fcd446d5f425bf/Algorithm%20Implementation/Screenshot_2.png)

 2. Depth-First Search (DFS)
    
How it works: Explores as far as possible along each branch before backtracking using a stack
 (LIFO).
 
 Applications:
 
 Solving mazes
 
 Topological sorting
 
 Complexity:
 
 Time: O(V + E)
 
 Space: O(V)

 ![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/69802018b084940673b14a035e8953f065feee2c/Algorithm%20Implementation/Screenshot_4.png)
 
 ![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/2d9520516f99ef4cc99447bc694c9ee74ef486ca/Algorithm%20Implementation/Screenshot_3.png)

3. Iterative Deepening Search (IDS)

How it works: Combines DFS and BFS by performing DFS with increasing depth limits.

Applications:
 
Memory-efficient search
 
Used in game trees
 
Complexity:
 
Time: O(b^d)
 
Space: O(d)

![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/bccf5df220a0faca2b1768e96408940a576ccdcb/Algorithm%20Implementation/Screenshot_6.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/bccf5df220a0faca2b1768e96408940a576ccdcb/Algorithm%20Implementation/Screenshot_5.png)

4. Bidirectional Search

How it works:
Runs two simultaneous searches — one forward from the start node and one backward from the goal node — until they meet.

Applications:

Finding the shortest path in maps and graphs

Route planning (e.g., GPS navigation systems)

Puzzle solving (e.g., 8-puzzle)

Complexity:

Time: O(b^(d/2))

Space: O(b^(d/2))

![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/4f4d0e02095f430eedda7b8816e4a861403349d7/Algorithm%20Implementation/Screenshot_7.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/4f4d0e02095f430eedda7b8816e4a861403349d7/Algorithm%20Implementation/Screenshot_8.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/4f4d0e02095f430eedda7b8816e4a861403349d7/Algorithm%20Implementation/Screenshot_9.png)

5. Depth-Limited Search (DLS)
   
How it works:

Performs a Depth-First Search (DFS) but with a predefined depth limit l. Nodes beyond this depth are not expanded.

Applications:

Searching in infinite or very large search spaces

Useful when the depth of the solution is known or bounded

Web crawling with depth restrictions

AI planning

Complexity:

Time: O(b^l)

Space: O(l)
(Where b = branching factor, l = depth limit)

![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/7421c218b82d34ef35f11b18b42096f32f66a36e/Algorithm%20Implementation/Screenshot_10.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/7421c218b82d34ef35f11b18b42096f32f66a36e/Algorithm%20Implementation/Screenshot_11.png)

6. Heuristic Search
   
How it works:
Heuristic Search uses a heuristic function to estimate the cost from a current node to the goal. This estimate helps prioritize which nodes to explore, making the search more efficient than uninformed methods.

Applications:

Puzzle solving (e.g., 8-puzzle, sliding tiles)

Game playing (e.g., chess, tic-tac-toe)

Pathfinding (e.g., A* in maps or navigation systems)

Robotics and planning

Complexity:

Depends on the heuristic:

A good heuristic reduces time and space complexity

A poor heuristic can degrade performance to that of uninformed search

![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/4a1efb426c46279ee51d279f572aee86190625d2/Algorithm%20Implementation/Screenshot_12.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/4a1efb426c46279ee51d279f572aee86190625d2/Algorithm%20Implementation/Screenshot_13.png)

7. Best-First Search
   
How it works:

It uses a heuristic function to evaluate which node appears to be closest to the goal.

Always expands the node with the lowest heuristic cost h(n) — this is known as the Greedy Best-First Search.

It is called "best-first" because it chooses the "best-looking" node at each step based on the heuristic.

Applications:

Pathfinding (e.g., navigation systems)

Puzzle solving (e.g., 8-puzzle)

Game AI

Web crawling

Complexity:

Time: O(b^m)

Space: O(b^m)
(where b is the branching factor, m is the maximum depth explored — may vary based on heuristic quality)

![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/c1655aefdadacd0b597cf7f8ad6c393aaebc6248/Algorithm%20Implementation/Screenshot_14.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/c1655aefdadacd0b597cf7f8ad6c393aaebc6248/Algorithm%20Implementation/Screenshot_15.png)

8. AO* Algorithm
   
How it works:

AO* (And-Or Star) is an extension of the A* algorithm designed for AND-OR graphs, where solving a problem may involve:

OR nodes: choosing one among multiple alternatives

AND nodes: satisfying multiple sub-goals together

It uses a heuristic function to estimate costs, like A*, and builds a solution graph while backtracking and updating costs.

Applications:

Expert systems

Automated planning and reasoning

Problem solving with hierarchical tasks or dependencies

Complexity:

Time complexity: Exponential in the worst case — depends on:

Branching factor

Number of AND/OR combinations

Heuristic accuracy

Space complexity: Also exponential due to storing the solution graph and backtracking

![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/f285d6d232ca6325bac54751e8124c2abb971345/Algorithm%20Implementation/Screenshot_16.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/f285d6d232ca6325bac54751e8124c2abb971345/Algorithm%20Implementation/Screenshot_17.png)

9. Beam Search
    
How it works:

Beam Search is a heuristic search algorithm that, at each level of the search tree, keeps only the best k nodes (based on heuristic score) and discards the rest.

k is the beam width, which controls how many nodes are expanded at each level.

It's like a breadth-first search, but memory-efficient due to pruning.

Applications:

Natural Language Processing (NLP)

Machine translation (e.g., sequence-to-sequence models)

Text generation

Speech recognition

Any domain where sequence prediction is needed

Complexity:

Time: O(k × d)
(where k = beam width, d = depth of the search)

Space: O(k × d)
(Much more efficient than BFS or A

![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/ccacb528f1b23d7742c05d5ac00ef3bfc7446be5/Algorithm%20Implementation/Screenshot_18.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/ccacb528f1b23d7742c05d5ac00ef3bfc7446be5/Algorithm%20Implementation/Screenshot_19.png)

10.Minimax Algorithm

How it works:

The Minimax algorithm is used in two-player, turn-based, zero-sum games.

It recursively explores the game tree to a certain depth d, assuming:

One player (Max) tries to maximize the score

The other player (Min) tries to minimize it

It selects the move that maximizes the minimum possible loss — i.e., assumes the opponent plays optimally.

Applications:

Game AI:

Tic Tac Toe

Chess

Checkers

Connect Four

Complexity:

Time: O(b^d)
(where b = branching factor, d = depth of the tree)

Space: O(d) (with recursion stack)

![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/614002347e3919dab982af570da2f7a160c82726/Algorithm%20Implementation/Screenshot_20.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/614002347e3919dab982af570da2f7a160c82726/Algorithm%20Implementation/Screenshot_21.png)

11. Alpha-Beta Pruning
    
How it works:

Alpha-Beta Pruning is an optimization of the Minimax algorithm.

It eliminates branches in the game tree that don’t need to be explored because they cannot affect the final decision.

It uses two values:

Alpha (α): the best already explored value along the path to the maximizer

Beta (β): the best already explored value along the path to the minimizer

If the current branch cannot produce a better outcome than previously explored ones, it is pruned (cut off).

Applications:

Efficient game-tree pruning in:

Chess engines

Tic Tac Toe

Checkers

Any Minimax-based AI

Complexity:

Time complexity:

Best case: O(b^(d/2))

Worst case: O(b^d) (same as Minimax)
(Where b = branching factor, d = depth of the tree)

Space complexity: O(d) (due to recursion stack)

![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/f4b378be5d2445b63dd0d33c2e11d0e37ae0aa0d/Algorithm%20Implementation/Screenshot_22.png)
![image alt](https://github.com/MirzaAnjuman/AI-Course/blob/f4b378be5d2445b63dd0d33c2e11d0e37ae0aa0d/Algorithm%20Implementation/Screenshot_23.png)







