# Continuous Deployment Pipeline: CodePipeline + CodeBuild + ECS

## Objectives
Automate the full software delivery lifecycle — from a GitHub commit to a live, running container on ECS Fargate — using AWS CodePipeline as the orchestrator, CodeBuild for CI, and ECS for automated rolling deployment.

## Tools Used
- AWS CodePipeline (Source, Build, Deploy stages)
- AWS CodeBuild (Docker image build + ECR push)
- AWS ECS (Fargate rolling deployment)
- AWS ECR (container registry)
- AWS IAM (least-privilege service roles for CodePipeline and CodeBuild)
- AWS S3 (pipeline artifact store)
- GitHub (source control + webhook trigger)
- Docker

## Key Skills Demonstrated
- End-to-end CI/CD pipeline design and implementation on AWS
- Multi-service IAM role architecture (separate scoped roles for CodePipeline and CodeBuild)
- buildspec.yml authoring and debugging for containerized builds
- Automated ECS rolling deployment via imagedefinitions.json
- GitHub source integration with OAuth-based webhook triggers
- Full-stack troubleshooting across IAM, CodeBuild, and container build context issues

## Troubleshooting Log
- **Bug — buildspec.yml syntax corruption:** Original lab spec contained a non-standard pipe character and an empty `REPOSITORY_URI` variable. Rewrote with the correct ECR login flow (`aws ecr get-login-password`) and a populated repository URI.
- **Bug — Artifact naming mismatch:** Original spec used a generic `"nodeapp"` container name in `imagedefinitions.json`, which would not match the actual ECS task definition's container name. Corrected to `"dockermastery-container"` to match the existing task definition.
- **Permission errors (recurring pattern):** Each new AWS service (CodePipeline, CodeBuild, IAM role creation) required explicitly attaching a scoped IAM policy to the working user, in addition to the service roles used by the pipeline itself — highlighting the AWS principle that human IAM users and service roles require independent permission grants.
- **Bug — Docker build context mismatch:** CodeBuild failed with `open Dockerfile: no such file or directory` because the Dockerfile lived in a subdirectory from a prior lab, while `docker build .` expected it at the repository root. Resolved by placing a root-level copy of the Dockerfile and index.html alongside buildspec.yml.
- **Result:** Pipeline achieved a fully automated rolling deployment — verified via ECS service deployment history showing the old task revision scaling to zero as the new revision (built entirely by the pipeline) scaled to running.
