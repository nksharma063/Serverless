# Serverless

## Assignment 1
### After writing the script, scroll down to the "Function execution" section and set up a test event to manually invoke the Lambda function. You can create a test event with an empty JSON object {}.

    Click the "Test" button to manually trigger your Lambda function.

    Step 4: Manual Invocation and Testing

    After saving your function, manually trigger it by clicking the "Test" button in the Lambda console.

    Monitor the Lambda function's execution to ensure it runs successfully.

    After the Lambda function execution is complete, go to the EC2 dashboard and confirm that the instances' states have changed according to their tags. The instance tagged as Auto-Stop       should be stopped, and the instance tagged as Auto-Start should be started.

## Assignment 2
    After writing the script, scroll down to the "Function execution" section and set up a test event to manually invoke the Lambda function. You can create a test event with an empty JSON object {}.
    Click the "Test" button to manually trigger your Lambda function.
    After saving your function, manually trigger it by clicking the "Test" button in the Lambda console.
    Monitor the Lambda function's execution to ensure it runs successfully.
    After the Lambda function execution is complete, go to the S3 dashboard and confirm that only files newer than 30 days remain in the bucket. The files older than 30 days should have     been deleted.

## Assignment 3
    Go to the AWS CloudWatch console.

    In the navigation pane, select "Rules" under "Events."

    Click the "Create rule" button.

    In the "Event Source" section, choose the service responsible for the event. For this example, select "Event Source" as "Schedule."

    Choose "Fixed rate of" and set the rate to 1 day. This will trigger the Lambda function once a day.

    In the "Targets" section, click "Add target."

    Select your Lambda function from the list of available targets.

    Click the "Configure details" button.

    Provide a name for your rule and, if needed, a description.

    Finally, click the "Create rule" button to create the CloudWatch Events rule

