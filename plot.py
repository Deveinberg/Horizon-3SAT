import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

booleans_list = [6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Function to load data from a file
def load_data(filename):
        with open(filename, 'r') as file:
            data = [float(line.strip()) for line in file]
        return np.array(data)
plt.style.use('seaborn-whitegrid')

def plot_counts_errorbars():
    # Dictionary to store data by the number of booleans
    data_dict = {}
    for b in [6,8,10,11,12,13,14,15,16,17,18,19,20]:
        data = load_data(f'Solutions/3SAT_COUNTS_{b}_booleans.txt')
        data_dict[b] = data

    # Calculate mean and standard deviation
    booleans = sorted(data_dict.keys())
    means = [np.mean(data_dict[b]) for b in booleans]
    std_devs = [np.std(data_dict[b]) for b in booleans]

    # Plotting
    plt.errorbar(booleans, means, yerr=std_devs, fmt='o', capsize=5)
    plt.xlabel('Number of Booleans')
    plt.ylabel('Number of Iterations')
    plt.title('Iterations vs Number of Booleans (Schöning)')
    plt.grid(True)
    plt.savefig('Figures/schöning-counts.png', dpi=300)

#plot_counts_errorbars()

def plot_sample_size():
    def count_lines(filename):
        try:
            with open(filename, 'r') as file:
                return sum(1 for line in file)
        except FileNotFoundError:
            print(f'File {filename} not found.')
            return 0

    # Initialize dictionaries to store data by the number of booleans
    solutions_dict = {}
    problems_dict = {}
    booleans_list = [6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # Load data for each number of booleans from Solutions folder
    for b in booleans_list:
        solutions_data = load_data(f'Solutions/3SAT_COUNTS_{b}_booleans.txt')
        solutions_dict[b] = solutions_data

    # Count lines for each number of booleans from Problems folder
    for b in booleans_list:
        problems_count = count_lines(f'Problems/3SAT_{b}_booleans.txt')
        problems_dict[b] = problems_count

    # Calculate sample sizes
    solutions_sizes = {b: len(data) for b, data in solutions_dict.items()}
    problems_sizes = {b: problems_dict[b] for b in booleans_list}

    # Extract booleans and their corresponding sample sizes
    booleans = sorted(solutions_sizes.keys())
    solutions_sizes_list = [solutions_sizes[b] for b in booleans]
    problems_sizes_list = [problems_sizes[b] for b in booleans]

    # Plotting the bar plot with overlapping bars
    bar_width = 0.35
    index = np.arange(len(booleans))

    fig, ax = plt.subplots()
    bar1 = ax.bar(index, problems_sizes_list, bar_width, label='Problems', color='lightcoral', alpha=0.9)
    bar2 = ax.bar(index, solutions_sizes_list, bar_width, label='Solutions', color='skyblue', alpha=0.9)

    ax.set_xlabel('Number of Booleans')
    ax.set_ylabel('Sample Size')
    ax.set_title('Sample Size of Problems and Solutions for Different Number of Booleans')
    ax.set_xticks(index)
    ax.set_xticklabels(booleans)
    ax.legend()

    plt.grid(axis='y')
    plt.savefig("Figures/sample_size_schoning.png", dpi=300)

#plot_sample_size()

def plot_schoning_cpu_times():
    # Load the CPU times data
    cpu_times_path = 'Solutions/CPU_times.txt'
    cpu_times_data = pd.read_csv(cpu_times_path, sep=';', header=None, names=['Booleans', 'CPU Time'])

    # Clean and process the data
    cpu_times_data['Booleans'] = cpu_times_data['Booleans'].str.extract('(\d+)').astype(int)
    cpu_times_data['CPU Time'] = cpu_times_data['CPU Time'].astype(float)

    # Function to map CPU times to colors
    def get_color_gradient(values, cmap_name='coolwarm'):
        norm = plt.Normalize(min(values), max(values))
        cmap = plt.get_cmap(cmap_name)
        return [cmap(norm(value)) for value in values]

    # Get the colors for each CPU time
    colors = get_color_gradient(cpu_times_data['CPU Time'], cmap_name='coolwarm')

    # Plotting the data as a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(cpu_times_data['Booleans'], cpu_times_data['CPU Time'], color=colors)

    plt.xlabel('Number of Booleans')
    plt.ylabel('CPU Time (seconds)')
    plt.title('Averaged CPU Times for the Schöning Algorithm to Successfully Execute')
    plt.grid(axis='y')
    plt.xticks(cpu_times_data['Booleans'])
    plt.savefig("Figures/schoning_CPU_times.png", dpi=300)

plot_schoning_cpu_times()