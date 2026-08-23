# Automated Containerized Deployment Pipeline on AWS

![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-ECS%20%7C%20ECR%20%7C%20CodePipeline-FF9900?logo=amazonaws&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Automated-success)
![IAM](https://img.shields.io/badge/IAM-Least--Privilege-blueviolet)
![Status](https://img.shields.io/badge/Status-Live%20on%20AWS-brightgreen)

An end-to-end CI/CD pipeline that takes a containerized application from source code to a live, auto-deployed service on AWS.

[Overview](#overview) • [Architecture](#architecture) • [Project Structure](#project-structure) • [Skills Demonstrated](#skills-demonstrated)

---

## Overview

A single git push triggers a fully automated chain: Docker image builds, pushes to a private registry, and deploys onto ECS Fargate.

```
GitHub push -> CodeBuild (build + push image) -> ECR -> CodePipeline -> ECS Fargate (rolling deploy)
```

This is a fully deployed, working pipeline — every stage below ran on a live AWS account, not a simulation.

## Architecture

| Stage | Service | Purpose |
|---|---|---|
| Source | GitHub | Version control, pipeline trigger |
| Registry | Amazon ECR | Private Docker image storage |
| Orchestration | Amazon ECS (Fargate) | Serverless container hosting |
| CI | AWS CodeBuild | Automated image build and push |
| CD | AWS CodePipeline | End-to-end deployment automation |
| Networking | Docker (bridge/host/none) | Container network isolation modeling |

## Project Structure

- [nginx-ecr-image/](./nginx-ecr-image) — Dockerfile and image build fundamentals, pushed to ECR
- [ecs-fargate-deployment/](./ecs-fargate-deployment) — ECS cluster, task definition, and Fargate service setup
- [codepipeline-cd/](./codepipeline-cd) — Full CI/CD pipeline: CodeBuild + CodePipeline + automated ECS rollout
- [docker-networking-modes/](./docker-networking-modes) — Bridge, host, and none networking mode analysis

Each folder contains its own README with implementation details and a troubleshooting log specific to that stage.

## Skills Demonstrated

- Docker image authoring, debugging, and multi-stage build workflows
- AWS IAM least-privilege role design across five distinct services
- Container orchestration on ECS Fargate (cluster, task definitions, rolling deployments)
- CI/CD pipeline design connecting GitHub, CodeBuild, and CodePipeline
- buildspec.yml authoring for automated build environments
- Docker networking modes and their container isolation implications

## Notable Problems Solved

This project was not built by following instructions cleanly — every stage surfaced a real issue that had to be diagnosed and fixed.

- Corrected Dockerfile syntax errors that silently broke the build context
- Resolved IAM permission gaps across ECR, ECS, CodeBuild, and CodePipeline — each service requiring its own explicit grant
- Debugged a CodeBuild failure caused by a Dockerfile living outside the build context root
- Rewrote a corrupted buildspec.yml into a working CI configuration

## Tech Stack

Docker, AWS ECR, AWS ECS, AWS Fargate, AWS CodeBuild, AWS CodePipeline, AWS IAM, Nginx, GitHub
