import threading
import subprocess
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369
# made by skid12369

# Number of times to run main.py
total_runs = 1000000
runs_per_thread = 10
# made by skid12369
def run_main():
    # Run 'python main.py' in the subprocess
    subprocess.run(['python', 'backend.py'])

def run_in_threads():
    runs_done = 0
    threads = []

    # Run the script until it has been run 1000 times
    while runs_done < total_runs:
        for _ in range(runs_per_thread):
            if runs_done >= total_runs:
                break
            thread = threading.Thread(target=run_main)
            thread.start()
            threads.append(thread)
            runs_done += 1

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

    print(f"main.py ran {runs_done} times")

# Usage
run_in_threads()
