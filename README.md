# 8-Queen-Problem

**[8 Queen Analysis]:**
**



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

