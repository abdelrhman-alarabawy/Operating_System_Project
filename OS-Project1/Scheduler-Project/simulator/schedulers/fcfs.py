from simulator.schedulers.scheduler import Scheduler

class FCFS(Scheduler):
    """First Come First Serve (FCFS) scheduler."""

    def __init__(self):
        super().__init__()

    def perform_schedule(self):
        """
        We simply sort the processes by the time that they come in by, and
        only change process as the processes finish their execution on the
        CPU.
        """
        # TODO: Implement here your code.
        if self.q:
            self.active = self.q[0]
            del self.q[0]
        else:
            self.active = None
        
        return self.active
        
                
                