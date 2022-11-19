#!/usr/bin/env python3

from aws_cdk import core
from demo_cdkapp.cdkpipeline_stack import CdkPipelineStack

app = core.App()
#deploy the pipelinestack referencing the lambda app within the stack
CdkPipelineStack(app, "CdkPipelineStack", env={'region': 'us-east-1'})

#best practice to tag all stacks the same way at entry point
core.Tags.of(app).add('acctype', 'dev')
app.synth()