# plot_results.py
import pandas as pd
import matplotlib.pyplot as plt

def plot():
    df = pd.read_csv("experiment_results.csv")
    # Convert types
    df['load_factor'] = df['load_factor'].astype(float)

    # 1) Insert time vs load_factor for each (table, hf)
    for metric in ['insert_time_s', 'succ_find_time_s', 'unsucc_find_time_s', 'delete_time_s']:
        plt.figure(figsize=(10,6))
        for (table, hf), sub in df.groupby(['table', 'hf']):
            sub_sorted = sub.sort_values('load_factor')
            plt.plot(sub_sorted['load_factor'], sub_sorted[metric], marker='o', label=f"{table}/{hf}")
        plt.xlabel("Load factor")
        plt.ylabel(metric)
        plt.title(f"{metric} vs Load factor")
        plt.legend(fontsize='small', ncol=2)
        plt.grid(True)
        plt.tight_layout()
        fname = f"{metric}_vs_load.png"
        plt.savefig(fname)
        print("Saved", fname)
        plt.close()

    # 2) Collisions histogram by hf
    for hf, sub in df.groupby('hf'):
        plt.figure(figsize=(8,4))
        # create bars per table+lf
        labels = sub['table'] + "@" + sub['load_factor'].astype(str)
        plt.bar(labels, sub['collisions'])
        plt.xticks(rotation=45, ha='right')
        plt.title(f"Collisions for {hf}")
        plt.tight_layout()
        fname = f"collisions_{hf}.png"
        plt.savefig(fname)
        print("Saved", fname)
        plt.close()

if __name__ == "__main__":
    plot()
