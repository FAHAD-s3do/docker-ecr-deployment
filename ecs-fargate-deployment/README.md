# ECS Fargate Container Orchestration

## Objectives
Deploy and orchestrate a containerized Nginx application on AWS ECS using the Fargate launch type, building on a previously built and pushed Docker image in AWS ECR.

## Tools Used
- AWS ECS (Fargate launch type)
- AWS ECR (container image source)
- AWS IAM (task execution role, least-privilege scoping)
- AWS CloudWatch Logs
- AWS VPC (default subnet/security group networking)
- AWS CLI v2

## Key Skills Demonstrated
- ECS cluster provisioning (serverless, Fargate launch type)
- Task definition authoring (JSON) — container specs, port mappings, log configuration
- IAM role creation for ECS task execution (ecsTaskExecutionRole)
- Service orchestration with desired-count and rolling deployment strategy
- awsvpc networking mode configuration (subnet + security group + public IP assignment)
- End-to-end container lifecycle verification (PROVISIONING → RUNNING)

## Troubleshooting Log
- **Permission error — ECS cluster creation:** IAM user initially lacked `ecs:CreateCluster` permission. Resolved by attaching `AmazonECS_FullAccess` policy.
- **Permission error — IAM role creation:** IAM user lacked `iam:CreateRole` / `iam:AttachRolePolicy` permissions needed to create the ECS task execution role. Resolved by attaching `IAMFullAccess` (noted as an over-broad grant appropriate only for lab/learning context, not production least-privilege design).
- **Design consistency fix:** Container port set to `80` in the task definition to match the corrected Dockerfile from the prior image-build lab (Nginx default), avoiding a port-mapping mismatch at runtime.

## Local deployment configuration

The committed task definition is a template. Supply your own account and region locally:

```bash
export AWS_REGION=us-east-1
export AWS_ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
python3 ecs-fargate-deployment/render-task-definition.py
```

Run from the repository root. The generated `task-definition.json` is ignored by Git.
Review its image, execution role, and log group before registering it with ECS.
The build specifications derive the account from the active AWS identity; configure
`AWS_REGION` and optionally `ECR_REPOSITORY_NAME` in CodeBuild for your environment.
No static AWS credentials belong in this repository.
