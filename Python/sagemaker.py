import sagemaker
from sagemaker.mxnet import MXNet

def main():
    model = "vicuna-7b-v1.5"
    prompt = "Once upon a time"
    mxnet_estimator = MXNet('train.py',
                        role='SageMakerRole',
                        instance_type='ml.p2.xlarge',
                        instance_count=1,
                        framework_version='1.2.1')

    algo = sagemaker.AlgorithmEstimator(
    algorithm_arn='arn:aws:sagemaker:us-west-2:1234567:algorithm/some-algorithm',
    role='SageMakerRole',
    instance_count=1,
    instance_type='ml.c4.xlarge')
if __name__ == "__main__":
    main()