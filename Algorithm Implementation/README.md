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
