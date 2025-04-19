# 8-Queen-Problem

**[8 Queen Analysis]:**



1. **Comparative Analysis:**

   |**Hill Climbing**|**Simulated Annealing**|**Local Beam Search**|
   | :- | :- | :- |
   |<p>- **Uses greedy approach to minimize conflicts.**</p><p>- **Can quickly find a solution, but often gets stuck in local optima or plateaus.**</p><p>- **If no better move is available, it terminates early, even if the solution is incorrect.**</p><p></p>|<p>- **Introduces randomness to accept worse moves with a probability based on temperature.**</p><p>- **Helps escape local optima, making it more reliable than hill climbing.**</p><p>- **As temperature decreases, it behaves more like hill climbing.**</p><p>- **Slower compared to other methods due to randomness in move selection.**</p><p></p>|<p>- **Maintains multiple candidate states (k states) at each step.**</p><p>- **Selects the best k successors, ensuring diversity in solutions.**</p><p>- **Less likely to get stuck in local optima compared to hill climbing.**</p><p>- **Efficient and scalable, especially with a higher k value.**</p><p></p>|
   **


2. **Which method found the solution the fastest?**

|**Hill Climbing**|**Simulated Annealing**|**Local Beam Search**|
| :- | :- | :- |
|**Fastest Found Solution**|**Took longer time due to the probability based acceptance of worse moves**|**Also efficient, finding the solution in a few iterations.**|
**



3. **How does randomness in Simulated Annealing impact the solution process?**
- **Simulated Annealing occasionally accepts a worse move to escape local optima. The probability of this acceptance is controlled by the temperature parameter.**
- **Initially, at high temperatures, bad moves are accepted more frequently. As the temperature decreases, it behaves more like hill climbing, reducing the chances of bad moves being accepted.**
- **This randomness helps explore more diverse states and prevents getting stuck in a local minimum too early, making it more robust than hill climbing in complex cases.**
**



4. **Explain how the visualization helps understand the search behavior.**

|**Hill Climbing**|**Simulated Annealing**|**Local Beam Search**|
| :- | :- | :- |
|**We can see a quick but often suboptimal solution.**|**The board sometimes worsens before improving, demonstrating the algorithm ability to escape local optima.**|**Multiple boards are processed, showing how different candidates evolve toward a solution simultaneously.**|
**




5. **Which local search algorithm is more likely to escape local optima, and why?**

|**Hill Climbing**|**Simulated Annealing**|**Local Beam Search**|
| :- | :- | :- |
|**The worst in this aspect, as it stops as soon as no better move is available, often leading to suboptimal solutions.**|**The best at escaping local optima because of its probabilistic acceptance of worse moves.**|**Also has a better chance of avoiding local optima by considering multiple board states at once, increasing the chances of finding a better solution.**|

**Hill Climbing**

![image](https://github.com/user-attachments/assets/13a42926-f6f9-406f-9919-9e0da1be4112)

![image](https://github.com/user-attachments/assets/ad3edd74-5e1f-47ed-ab84-32ddff9a1ef3)

**Simulated Annealing**

![image](https://github.com/user-attachments/assets/d46b82a0-b9b9-4436-9e12-01823336896a)

![image](https://github.com/user-attachments/assets/1e834328-4d63-43cf-836e-7a38223f1898)

**Local Beam Search**

![image](https://github.com/user-attachments/assets/7fb24719-5ca6-4578-83ea-a35e053ca6fd)

![image](https://github.com/user-attachments/assets/5c55c6b0-94a1-41bd-9148-4e402d06a2e7)

