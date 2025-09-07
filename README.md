# Python AWS Serverless Backend

This project is a backend service built with Python and AWS Lambda using the Serverless Framework. It demonstrates how to create, deploy, and manage serverless functions and APIs on AWS.

## Features

- AWS Lambda functions written in Python
- REST API endpoints via API Gateway
- Rate limiting and usage plans
- Easy deployment with Serverless Framework
- Example function: `hello` endpoint

## Prerequisites

- Node.js and npm
- Python 3.10+
- AWS account and credentials
- Serverless Framework (`npm install -g serverless`)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Madan1500/python-aws-serverless-learning.git
   cd python-aws-serverless-learning
   ```
2. Install dependencies:
   ```bash
   npm install
   pip install -r requirements.txt
   ```
3. Configure AWS credentials (via `aws configure` or environment variables).

## Deployment

Deploy your backend to AWS Lambda:

```bash
serverless deploy
```

## Usage

Invoke the example endpoint:

```bash
curl https://<api-id>.execute-api.<region>.amazonaws.com/dev/hello
```

## Project Structure

- `handler.py` - Lambda function code
- `serverless.yml` - Serverless Framework configuration
- `requirements.txt` - Python dependencies
- `.github/workflows/` - CI/CD pipeline

## License

MIT
