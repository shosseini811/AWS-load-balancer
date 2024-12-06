# AWS Load Balancer Demo

This project demonstrates a simple DevOps setup using AWS Application Load Balancer with a Flask application deployed using Terraform.

## Project Structure

```
.
├── app/
│   ├── app.py              # Flask application
│   ├── Dockerfile          # Docker configuration
│   └── requirements.txt    # Python dependencies
└── terraform/
    ├── main.tf            # Main Terraform configuration
    └── variables.tf       # Terraform variables
```

## Prerequisites

- AWS CLI configured with appropriate credentials
- Terraform installed (v1.0.0 or later)
- Docker installed (for building the application)
- Python 3.9 or later

## Setup Instructions

1. Configure AWS credentials:
   ```bash
   aws configure
   ```

2. Initialize Terraform:
   ```bash
   cd terraform
   terraform init
   ```

3. Build and test the Docker image locally:
   ```bash
   cd app
   docker build -t aws-lb-demo .
   docker run -p 5000:5000 aws-lb-demo
   ```

4. Deploy the infrastructure:
   ```bash
   cd terraform
   terraform plan
   terraform apply
   ```

## Architecture

This project sets up:
- A VPC with public subnets across 2 availability zones
- An Application Load Balancer
- Security groups for the load balancer
- A target group for the application
- A simple Flask application that returns the hostname

## Security Considerations

- The load balancer is configured with HTTP (port 80) for demonstration purposes. For production, configure HTTPS.
- Security groups are configured to allow only necessary traffic.
- The application runs in public subnets but can be moved to private subnets with NAT gateways for production.

## Cleanup

To destroy the infrastructure:
```bash
cd terraform
terraform destroy
```

## Contributing

Feel free to submit issues and enhancement requests!