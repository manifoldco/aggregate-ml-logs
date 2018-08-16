docker build -t ml_logs .

for sample_size in {1..100..5}; do
    for job in keras_job.py scikit-learn_job.py tensorflow_job.py; do
        docker run -e TIMBER_API_KEY=$TIMBER_API_KEY -e JOB=$job -e SAMPLE_SIZE=$sample_size ml_logs:latest ./ml_logs/training/$job
    done
done