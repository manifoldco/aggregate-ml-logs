import tensorflow as tf

from ml_logs import env
from ml_logs.data import read_traces, scale_traces
from ml_logs.logs import logger


def train_lr(x_train, y_train):
    logger.info("Training TF Linear Regression Estimator")
    memory_col = tf.feature_column.numeric_column('memory')
    estimator = tf.estimator.LinearRegressor(feature_columns=[memory_col])

    # create training input function
    training_input_fn = tf.estimator.inputs.numpy_input_fn(x={'memory': x_train},
                                                        y=y_train,
                                                        batch_size=32,
                                                        shuffle=False,
                                                        num_epochs=1)
    estimator.train(training_input_fn, steps=2000)
    return estimator

def evaluate_lr(estimator, x_test, y_test):
    # create testing input function
    eval_input_fn = tf.estimator.inputs.numpy_input_fn(x={'memory': x_test},
                                                        y=y_test,
                                                        batch_size=32,
                                                        shuffle=False,
                                                        num_epochs=1)
    logger.info('TF Estimator average_loss was %d', estimator.evaluate(eval_input_fn)['average_loss'])

    

if __name__ == "__main__":
    logger.info('Training: %s:%d', env.JOB, env.SAMPLE_SIZE)
    traces = read_traces(env.SAMPLE_SIZE)
    x_train, y_train, x_test, y_test = scale_traces(traces)
    estimator = train_lr(x_train, y_train)
    evaluate_lr(estimator,x_test, y_test)