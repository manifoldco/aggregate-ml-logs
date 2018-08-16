# Hello Observability For Machine Learning with Timber.io

Logging for machine learning is important. It provides observability into how your data processing, model training, evaluation, and artifact persistance is going. But its frought with questions: which logs are important, how do I log across multiple enviroments and frameworks, should I log experimental research and production training code? Enter Timber.io, by providing a dead simple logging interface for python let Timber.io collect and manage your training logs and provide once central place for machine learning observability.

This repo is the code that accompanies the [Machine Learning Observability with Timber.io]() post. As mentioned in the post, this project is powered by Manifold.co. If your not a user of manifold to manage your creditionals and provision third party services to power your research and experimentation read the [quick start guide here](https://docs.manifold.co/docs/quickstart-guide-6G2IZEjhD20oK6iISoQOE6).

Once you have manifold installed you can provision a free timber logging service and run the example like so:
```shell
$ manifold create --team datasci --project aggregate-ml-logs --product timber-logging
$ manifold run -- bash ./run-me.sh
```
