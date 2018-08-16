from keras.models import Sequential
from keras.layers import Dense, Dropout

from ml_logs.data import read_traces, scale_traces
from ml_logs import env
from ml_logs.logs import logger


def train_nn(x_train, y_train):
    logger.info('Training Simple Keras NN')

    model = Sequential()
    model.add(Dense(1, kernel_initializer='normal'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

    for step in range(10000):
        cost = model.train_on_batch(x_train, y_train)
    
    return model

def evaluate_nn(model, x_test, y_test):
    score, acc = model.evaluate(x_test, y_test)
    logger.info('Simple Keras NN: Test score: %d', score)
    logger.info('Simple Ketas NN: Test accuracy: %d', acc)

if __name__ == '__main__':
    logger.info('Training: %s:%d', env.JOB, env.SAMPLE_SIZE)
    traces = read_traces(env.SAMPLE_SIZE)
    x_train, y_train, x_test, y_test = scale_traces(traces)
    model = train_nn(x_train, y_train)
    evaluate_nn(model, x_test, y_test)