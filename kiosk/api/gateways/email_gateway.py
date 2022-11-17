import boto3
from botocore.exceptions import ClientError
from domain.services.send_email import SendEmailEmailIGateway

"""
AWS Simple Email Service (SES)
"""


class AWSEmailGateway(SendEmailEmailIGateway):
    def send(
        self, recipient: str, sender: str, subject: str, body_text: str, body_html: str
    ):
        # todo Make env variable
        aws_region = "us-east-1"

        # The character encoding for the email.
        charset = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client("ses", region_name=aws_region)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    "ToAddresses": [
                        recipient,
                    ],
                },
                Message={
                    "Body": {
                        "Html": {
                            "Charset": charset,
                            "Data": body_html,
                        },
                        "Text": {
                            "Charset": charset,
                            "Data": body_text,
                        },
                    },
                    "Subject": {
                        "Charset": charset,
                        "Data": subject,
                    },
                },
                Source=sender,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            message = (
                f"Error: {e.response['Error']['Message']}.\n"
                f"Recipient, sender, subject: [{recipient, sender, subject}]"
            )
            raise Exception(message)
        else:
            print("Email sent! Message ID:"),
            print(response["MessageId"])
