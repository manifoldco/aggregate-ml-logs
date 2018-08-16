import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

def read_traces(sample_size):
    trace_dfs = [
        pd.read_csv(os.path.join('data', 'traces', trace_path), delimiter=';\t')
        for trace_path in os.listdir(os.path.join('data', 'traces'))[:sample_size]
    ]
    traces = pd.concat(trace_dfs)
    traces['Total network throughput [KB/s]'] = traces['Network received throughput [KB/s]'].add(traces['Network transmitted throughput [KB/s]'])
    return traces

def scale_traces(traces):
    sc = StandardScaler()
    x = sc.fit_transform(traces['Memory usage [KB]'].values.reshape(-1, 1))
    y = sc.fit_transform(traces['Total network throughput [KB/s]'].values.reshape(-1, 1))

    x_train = x[:int(len(x)/2)]
    y_train = y[:int(len(y)/2)]
    x_test = x[int(len(x)/2):]
    y_test = y[int(len(y)/2):]

    return x_test, y_test, x_train, y_train