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




