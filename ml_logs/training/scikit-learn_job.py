import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from ml_logs import env
from ml_logs.data import read_traces
from ml_logs.logs import logger


def train_rfregressor(traces):
    logger.info('Training RandomForestRegressor')
    regressor = RandomForestRegressor(max_depth=10, random_state=1)
    regressor.fit([[t] for t in traces['Memory usage [KB]']], traces['Total network throughput [KB/s]'].values)

    logger.info('Random Forest Regressors score was: %d',
        regressor.score([[t] for t in traces['Memory usage [KB]']], traces['Total network throughput [KB/s]'].values)
    )

if __name__ == '__main__':
    logger.info('Training: %s:%d', env.JOB, env.SAMPLE_SIZE)
    traces = read_traces(env.SAMPLE_SIZE)
    train_rfregressor(traces)