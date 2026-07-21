# Part 4 — CPU Scheduling, Concurrency Synchronization & Deadlock Analysis

## 1. Priority Scheduling with Aging Trace

Higher numeric value = Higher scheduling priority.

### Starvation Scenario
Low-priority process $P_{low}$ (Priority 1) arrives at $t=0$. High-priority processes continue arriving at every time unit. Without aging, $P_{low}$ is continuously preempted and starves indefinitely.

### Aging Mitigation Trace
**Aging Rule:** Increment priority by +1 for every 5 units spent in waiting queue.

| Time Window | Process | Waiting Time | Base Priority | Aged Priority | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $t = 0-5$ | $P_{low}$ | 5 | 1 | 2 | Waiting |
| $t = 5-10$ | $P_{low}$ | 10 | 1 | 3 | Waiting |
| $t = 10-15$ | $P_{low}$ | 15 | 1 | 4 | Selected for CPU Execution |

---

## 2. Synchronization Fix Analysis
In `sync_demo.py`, unsynchronized execution leads to race conditions due to non-atomic read-modify-write sequences across threads. By introducing a Mutex Lock around the critical section, atomic execution is enforced, guaranteeing identical expected final values ($200,000$).

---

## 3. Deadlock Analysis & Resource Allocation Graph (RAG)

### Scenario
3 Processes ($P_1, P_2, P_3$) and 3 Resources ($R_1, R_2, R_3$).

### Four Necessary Coffman Conditions
1. **Mutual Exclusion:** Resources cannot be shared simultaneously.
2. **Hold and Wait:** Processes holding assigned resources request additional resources.
3. **No Preemption:** Resources cannot be forcibly taken from processes.
4. **Circular Wait:** Closed chain of dependencies where $P_1$ waits for $P_2$, $P_2$ for $P_3$, and $P_3$ for $P_1$.

### Resource Allocation Graph (Edges)
```text
R1 -> P1 (Allocated)
P1 -> R2 (Requested)
R2 -> P2 (Allocated)
P2 -> R3 (Requested)
R3 -> P3 (Allocated)
P3 -> R1 (Requested)
