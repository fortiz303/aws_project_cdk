#!/usr/bin/env python3

from aws_cdk import core

from cdkworkshop.cdkworkshop_stack import CdkWorkshopStack


app = core.App()
CdkWorkshopStack(app, "cdkworkshop", env={'region': 'us-west-2'})

app.synth()

