# Deadlock Project
1. Implement 'detect' function in Deadlock-Project/main.py file.

# Scheduler Project:
1. Implement function 'perform_schedule' function in Scheduler-Project/simulator/schedulers/{fcfs, rr, sjf, srtf}. 
2. Note: fcfs: First Come First Serve, rr:Round Robin, sjf: Shortest Job First, srtf: Shortest Remaining Time First 
3. For installation run `pip install -r requirements.txt` to install the required python packages.
4. To run: `python -m simulator <filename>`
5. Note input file should have the format for each line: `<process id> <arriving time> <burst time>`
6. The program will write a line in the following format every time the CPU performs a context switch: `(<timestamp>, <process id>)` and lastly output the average waiting time: `Average waiting time <waiting time>` he outputs will be written in a file with the name of the scheduler and stored in the folder called `schedules`.

<p align="center">
  <img src="https://user-images.githubusercontent.com/57441828/119667443-97400a00-be36-11eb-9f58-814e9d9a25ef.gif" />
</p>
