import heapq

class VectorClock:
    def __init__(self, id, clock=None):
        if clock is None:
            clock = [0] * (id + 1)
        elif len(clock) < id + 1:
            clock = [0] * (id + 1) + clock[len(clock):id+1]
        self.clock = clock
        self.id = id

    def __repr__(self):
        return f'Vetor[{self.id}:{",".join(str(x) for x in self.clock)}]'

    def __eq__(self, other):
        if isinstance(other, VectorClock):
            return self.clock == other.clock
        return False

    def __lt__(self, other):
        if isinstance(other, VectorClock):
            for i in range(min(len(self.clock), len(other.clock))):
                if self.clock[i] < other.clock[i]:
                    return True
                elif self.clock[i] > other.clock[i]:
                    return False
            if len(self.clock) < len(other.clock):
                return True
            return False
        return False

    def update(self, other):
        if isinstance(other, VectorClock) and other.id != self.id and len(other.clock) > len(self.clock):
            self.clock += [0] * (len(other.clock) - len(self.clock))
        for i in range(len(other.clock)):
            self.clock[i] = max(self.clock[i], other.clock[i])

def simulate_events(events):
    clocks = {i: VectorClock(i) for i in range(len(events))}
    event_names = {0: 'EXPLORER', 1: 'POWERPOINT', 2: 'CHROME', 3: 'WI-FI', 4: 'IMPRESSÃO'}
    for event in events:
        sender, receiver, timestamp = event
        clocks[sender].update(clocks[receiver])
        clocks[receiver].clock[receiver] = max(clocks[receiver].clock[receiver], timestamp)
        clocks[sender].clock[sender] = max(clocks[sender].clock[sender], timestamp + 1)
        print(f'{event_names[sender]} precede com causalidade o {event_names[receiver]}:')
        for process_id, clock in clocks.items():
            action = f'{event_names[process_id]} enviou {clock.clock[process_id]} eventos, '
            if process_id != receiver:
                action += f'{event_names[receiver]} recebeu 0 evento'
            else:
                action += f'{event_names[receiver]} recebeu {clock.clock[receiver]} eventos'
            print(f'    Processo {process_id}: {clock} - {action}')
        print()

if __name__ == '__main__':
    events = [(0, 1, 1), (1, 0, 2), (1, 2, 3), (0, 2, 4)]
    heapq.heapify(events)
    simulate_events(events)
