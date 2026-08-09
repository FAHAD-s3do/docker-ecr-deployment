# Docker Image Build & AWS ECR Deployment

## Objectives
Build a custom Docker image from an Nginx base, and push it to a private AWS Elastic Container Registry (ECR) repository for centralized, cloud-based image storage and future orchestration (ECS/Fargate).

## Tools Used
- Docker (image build, tagging)
- AWS CLI v2
- AWS Elastic Container Registry (ECR)
- AWS IAM (scoped access credentials)
- Nginx (base image)

## Key Skills Demonstrated
- Writing and debugging a production Dockerfile
- Container image build, tag, and versioning workflow
- AWS IAM user/policy creation with least-privilege scoping (AmazonEC2ContainerRegistryFullAccess)
- AWS CLI authentication and ECR Docker login flow
- Pushing and verifying container images in a private cloud registry

## Troubleshooting Log
- **Bug — Dockerfile COPY syntax error:** Missing space between source (.) and destination path caused Docker to parse it as a single invalid argument. Fixed with explicit spacing: `COPY . /usr/share/nginx/html`.
- **Bug — Invalid CMD directive:** Original draft used "daemons off" (misspelled, missing semicolon) — an invalid Nginx directive that would crash the container on start. Corrected to "daemon off;".
- **Bug — Docker daemon permission denied:** Non-root user lacked docker group membership, blocking all Docker CLI commands. Resolved via usermod -aG docker $USER + session refresh.
- **Design fix — Port mismatch:** Lab spec used EXPOSE 8080, but the Nginx base image listens on port 80 by default. Corrected to EXPOSE 80 to match actual container behavior, with host mapping handled via -p 8080:80 at runtime.
