import matplotlib.pyplot as plt
import pandas as pd


def main():
    # time_report = matrix_multiplication_python()
    # print(time_report.time) # 15.631019115447998
    plot_benchmarks(base_python_time=15.631019115447998)


def plot_benchmarks(filepath='time_benchmarks.csv',
                    base_python_time: float = 15.631019115447998):
    data = pd.read_csv(filepath, names=['Name', 'Cores', 'Time'])
    data = data.sort_values('Time', ascending=False)

    speedup = base_python_time / data['Time']
    instances = data['Name']
    times = data['Time']

    # Creating subplots
    fig, ax1 = plt.subplots(figsize=(15, 6))

    # Plotting time vs instance
    ax1.barh(instances, times, color='skyblue')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Instance')
    ax1.set_title('Time vs Instance')
    ax1.set_xlim(0, times.max() * 0.8)
    ax1.grid(axis='x')  # optional: add gridlines along x-axis

    # Create a twin Axes for speedup
    ax2 = ax1.twinx()
    ax2.set_ylabel('Speedup')

    # Remove y-axis ticks and tick labels
    ax2.yaxis.set_ticks([])

    # Add speedup labels on the left y-axis
    for i, (instance, sp) in enumerate(zip(instances, speedup)):
        ax1.text(times.max(), i, f'SpeedUp: {sp:.2f}', ha='right', va='center',
                 fontsize=13, color='red')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
