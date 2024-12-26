import boto3
from botocore.exceptions import ClientError
from read_file import return_list

client = boto3.client("bedrock-runtime", region_name="sa-east-1")

model_id = "mistral.mistral-7b-instruct-v0:2"

user_message = """ You will receive a list of fiscal documents that are formatted as a list with the columns fiscal document number, client name, description. You should separate the fiscal documents in two groups one group will be from the documents that contains dependents or childs in its description column, the other group will contain documents that doesnt contain the description.
An dependent or a child is a human name followed by CPF or birth date (DN or data de nascimento) that differentiate from the client name column.
The group that contains the dependent should be returned as: fiscal document number|kid or dependent name|birth date|CPF, if some of these fields doesnt exist it should be placed a NULL value in it.

YOU SHOULD NOT RETURN A CODE

List:
"""

user_message += return_list("/home/fsv/Downloads/171.csv")
conversation = [
    {
        "role":"user",
        "content":[{"text":user_message}]
    }
]

try:
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens":512, "temperature": 0.5, "topP": 0.9},
    )

    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)
except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason {e}")
    exit(1)
