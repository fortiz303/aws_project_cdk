from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_iam as iam,
    core
)

class CdkWorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='hello.handler',
        )
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )
#        queue = sqs.Queue(
#            self, "CdkWorkshopQueue",
#            visibility_timeout=core.Duration.seconds(300),
#        )
#
#        topic = sns.Topic(
#            self, "CdkWorkshopTopic"
#        )
#
#        topic.add_subscription(subs.SqsSubscription(queue))
