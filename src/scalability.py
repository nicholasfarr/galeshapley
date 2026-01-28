import datetime
import random
import matplotlib.pyplot as plt
from stablematching import stable_matching
from verifier import verifier

"""Measure the running time of your matching engine on an increasingly 
larger number of hospitals/students, i.e., n = 1, 2, 4, 8, 16, 32, 64, 128, 256, 512 
and graph the running time as a line graph when n on the x-axis and 
the running time on the y-axis.  Do the same for the verified.  
What is the trend that you notice? Note: 
How you measure the running time is up to you 
(there are multiple ways of doing this) and will likely depend 
on which programming language you choose."""



def main():
    ns = [2**i for i in range(0, 10)]
    times_matching = []
    times_verifying = []

    for n in ns:
        input_file = setup_simulation(n)

        start_time = datetime.datetime.now()
        hospitals, students, pairings = stable_matching(input_file)
        end_time = datetime.datetime.now()
        times_matching.append((end_time - start_time).total_seconds())

        start_time = datetime.datetime.now()
        verifier(hospitals, students, pairings)
        end_time = datetime.datetime.now()
        times_verifying.append((end_time - start_time).total_seconds())

    plt.plot(ns, times_matching, label='Matching Time') 
    plt.plot(ns, times_verifying, label='Verifying Time')
    plt.xlabel('Number of Hospitals/Students (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Running Time of Stable Matching and Verifier Engines')
    plt.legend()
    plt.grid(True)
    plt.savefig('out/scalability_plot.png')

    plt.xscale('log', base=2)
    plt.yscale('log')
    plt.savefig('out/scalability_plot_log.png')
    return



def setup_simulation(n):
    # creates an .in file with corresponding preferences and returns the str path
    with open('data/sim_{}.in'.format(n), 'w') as file:
        file.write('{}\n'.format(n))
        for i in range(1, n+1):
            prefs = list(range(1, n+1))
            random.shuffle(prefs)
            file.write(' '.join(map(str, prefs)) + '\n')
        for i in range(1, n+1):
            prefs = list(range(1, n+1))
            random.shuffle(prefs)
            file.write(' '.join(map(str, prefs)) + '\n')
    file.close()
    
    return 'data/sim_{}.in'.format(n)


if __name__ == "__main__":
    main()