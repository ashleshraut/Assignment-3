class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.start_time = -1

def fcfs(processes):
    procs = [Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in processes]
    # Tie-breaking rule: sorted by arrival_time, then pid order
    procs.sort(key=lambda x: (x.arrival_time, x.pid))
    
    current_time = 0
    for p in procs:
        if current_time < p.arrival_time:
            current_time = p.arrival_time
        p.start_time = current_time
        p.completion_time = current_time + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
        current_time = p.completion_time
        
    return procs

def sjf_non_preemptive(processes):
    procs = [Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in processes]
    n = len(procs)
    completed = 0
    current_time = 0
    visited = [False] * n
    result = []
    
    while completed < n:
        eligible = []
        for i in range(n):
            if procs[i].arrival_time <= current_time and not visited[i]:
                eligible.append(procs[i])
                
        if not eligible:
            current_time += 1
            continue
            
        # Tie-breaking rule: shortest burst_time, then arrival_time, then pid
        eligible.sort(key=lambda x: (x.burst_time, x.arrival_time, x.pid))
        selected = eligible[0]
        
        # Find index in original procs list
        idx = next(i for i, p in enumerate(procs) if p.pid == selected.pid)
        visited[idx] = True
        
        selected.start_time = current_time
        selected.completion_time = current_time + selected.burst_time
        selected.turnaround_time = selected.completion_time - selected.arrival_time
        selected.waiting_time = selected.turnaround_time - selected.burst_time
        current_time = selected.completion_time
        completed += 1
        result.append(selected)
        
    return result

def round_robin(processes, quantum=2):
    procs = {p.pid: Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in processes}
    all_pids = sorted(list(procs.keys()))
    
    # Sort processes by arrival time
    arrival_sorted = sorted(procs.values(), key=lambda x: (x.arrival_time, x.pid))
    
    current_time = 0
    ready_queue = []
    unarrived = list(arrival_sorted)
    completed_procs = []
    
    while len(completed_procs) < len(processes):
        # Add newly arrived processes to queue
        newly_arrived = [p for p in unarrived if p.arrival_time <= current_time]
        for p in newly_arrived:
            ready_queue.append(p)
            unarrived.remove(p)
            
        if not ready_queue:
            if unarrived:
                current_time = unarrived[0].arrival_time
                continue
            else:
                break
                
        curr = ready_queue.pop(0)
        
        exec_time = min(quantum, curr.remaining_time)
        curr.remaining_time -= exec_time
        current_time += exec_time
        
        # Check arrivals during execution
        newly_arrived_during = [p for p in unarrived if p.arrival_time <= current_time]
        for p in newly_arrived_during:
            ready_queue.append(p)
            unarrived.remove(p)
            
        if curr.remaining_time > 0:
            ready_queue.append(curr)
        else:
            curr.completion_time = current_time
            curr.turnaround_time = curr.completion_time - curr.arrival_time
            curr.waiting_time = curr.turnaround_time - curr.burst_time
            completed_procs.append(curr)
            
    return completed_procs

def print_metrics(algorithm_name, processes):
    print(f"\n================ {algorithm_name} ================")
    print("PID\tArrival\tBurst\tCompletion\tWaiting\tTurnaround")
    total_wait = 0
    total_tat = 0
    for p in sorted(processes, key=lambda x: x.pid):
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t\t{p.waiting_time}\t{p.turnaround_time}")
        total_wait += p.waiting_time
        total_tat += p.turnaround_time
    n = len(processes)
    print(f"Average Waiting Time: {total_wait / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")

if __name__ == "__main__":
    dataset = [
        Process(pid=1, arrival_time=0, burst_time=8, priority=3),
        Process(pid=2, arrival_time=1, burst_time=4, priority=1),
        Process(pid=3, arrival_time=2, burst_time=9, priority=4),
        Process(pid=4, arrival_time=3, burst_time=2, priority=2),
        Process(pid=5, arrival_time=4, burst_time=5, priority=5),
    ]
    
    print_metrics("First-Come, First-Served (FCFS)", fcfs(dataset))
    print_metrics("Shortest Job First (SJF Non-Preemptive)", sjf_non_preemptive(dataset))
    print_metrics("Round Robin (Quantum = 2)", round_robin(dataset, quantum=2))
