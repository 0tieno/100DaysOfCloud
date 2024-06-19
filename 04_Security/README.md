# AWS Config Overview

## Introduction

AWS Config is a service that enables you to assess, audit, and evaluate the configuration of your AWS resources. This module provides an overview of AWS Config, its features, and how it can help improve security configuration and compliance in your AWS environment.

## Features of AWS Config

- **Resource Discovery**: AWS Config helps you discover existing AWS resources and their configurations.
- **Configuration History**: It allows you to determine how a resource was configured at any point in time.
- **Compliance Auditing**: You can use AWS Config to ensure your resources comply with security policies and standards.
- **Security Analysis**: AWS Config aids in analyzing the security configurations of your resources.
- **Resource Change Tracking**: Track changes to your resources and their configurations over time.
- **Troubleshooting**: Facilitates troubleshooting by providing detailed configuration data and history.

## How AWS Config Improves Security and Compliance

AWS Config helps ensure that the resources in your AWS account comply with your security policies by:

- **Creating Rules**: You can create AWS Config rules to define your desired configurations and compliance policies.
- **Monitoring Compliance**: AWS Config continuously monitors your resources against these rules.
- **Alerting on Violations**: If a rule is violated, AWS Config will alert you, enabling prompt action to correct the issue.

### Example Scenario

**Question**: How can you check and ensure that the resources in your AWS account comply with your security policies?

**Answer**: Use AWS Config. Create a rule, and AWS Config will alert you if and when it is violated.

## Capabilities of AWS Config

- **Discover Existing Resources**: Identify and document existing AWS resources.
- **Configuration Snapshot**: View how a resource was configured at any point in time.
- **Compliance Notifications**: Receive alerts if an AWS Config rule is violated when a resource’s configuration is changed.

# Security Life Cycle: Response

## Incident Investigation Process

1. Identify the incident.
2. Contain the incident.
3. Eradicate the root cause.
4. Recover from the incident.
5. Review and document the incident.

## Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP)

### Purpose

- **BCP**: Describes how to run the business in a reduced capacity during an incident.
- **DRP**: Describes how to recover from an outage or data loss and return to normal operations as quickly as possible.

### Key Parameters of DRP

- **Recovery Time Objective (RTO)**: The maximum acceptable amount of time to restore business operations.
- **Recovery Point Objective (RPO)**: The maximum acceptable amount of data loss measured in time.

## Conclusion

AWS Config is an essential service for maintaining the security and compliance of your AWS resources. By leveraging its features, you can ensure your resources are correctly configured, continuously monitored, and promptly alerted if any compliance issues arise.

# AWS Security Resources and Best Practices

## Security Resources

Different types of available security resources include the following:
- **AWS Account Teams**: Dedicated teams to provide guidance and support.
- **AWS Support Plans**: Various support levels for technical assistance.
- **AWS Professional Services and AWS Partner Network (APN)**: Professional consulting and partner solutions.
- **AWS Advisories and Bulletins**: Updates and notifications on security issues.
- **AWS Auditor Learning Path**: Educational resources for auditing AWS environments.

## AWS Compliance

AWS Cloud compliance ensures robust controls for security and data protection:
- Customers operate within a secure AWS-controlled environment.
- AWS supports multiple security standards and compliance certifications globally.

## Best Practices

### AWS Account Security
- **AWS Account Root User**: Identified by email address; has full admin access.
  - Do not share root user credentials.
  - Delete root user access keys after use.

### IAM Best Practices
- **IAM Users**: Create individual IAM users for organizational members.
- **Multi-Factor Authentication (MFA)**: Enable MFA for enhanced account security.

### AWS CloudTrail
- **Logging and Billing**: Activate AWS CloudTrail for logging and billing reports.

## AWS Trusted Advisor

### Overview
AWS Trusted Advisor offers real-time guidance for resource optimization and security:
- Provides recommendations across five categories: Cost optimization, Performance, Security, Fault tolerance, and Service limits.

### Security Checks
Examples of Trusted Advisor security checks include:
- Ensuring security groups restrict access appropriately.
- Monitoring IAM permissions to control resource access.
- Activating MFA for the root account.
- Reviewing S3 bucket permissions to avoid public access.



