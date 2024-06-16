# Introduction to Computing

- [Introduction to Computing](#introduction-to-computing)
  - [Learning Objectives](#learning-objectives)
  - [Building blocks of the digital world](#building-blocks-of-the-digital-world)
  - [Computing terms](#computing-terms)
  - [Basic Computing Concepts](#basic-computing-concepts)
  - [Development Team Roles](#development-team-roles)
  - [What Is Cloud Computing?](#what-is-cloud-computing)
  - [Advantages of Cloud Computing](#advantages-of-cloud-computing)
  - [What Is AWS?](#what-is-aws)
  - [AWS Pricing](#aws-pricing)
  - [AWS Global Infrastructure](#aws-global-infrastructure)
  - [AWS Services and Service Categories](#aws-services-and-service-categories)
  - [Shared Responsibility Model](#shared-responsibility-model)
  - [Amazon S3](#amazon-s3)
  - [Amazon EC2](#amazon-ec2)

## Learning Objectives

You will learn how to do the following:
- Express the value of technology.
- Define basic computing terms.

## Building blocks of the digital world

Building blocks of the digital world: Applications, computers, and networks run the digital world.

## Computing terms

An application is a set of instructions that runs on a computer to perform a specific task.
- A computer program is written as code in a programming language.
- Computer programs are generally called software.

### Types of Applications:
- **Web application**: Runs in a web server or application server and is accessed from a web browser
- **Mobile app**: Runs in and is accessed from a mobile device 
- **Desktop application**: Runs in and is accessed from a desktop computer
- **Internet of Things (IoT) application**: Runs in and is accessed from an appliance or specialized device that is connected to the internet

### Main Hardware Components Inside a Computer:
- CPU
- Memory
- Storage drive
- Network card

### Main Software Components:
- OS
- Applications

A computer network connects multiple devices to share data and resources.

# Basic Computing Concepts

## Learning Objectives

You will learn how to do the following:
- Describe servers and data centers.
- Discuss computing technology that makes cloud computing possible.
- Describe how software is developed.

## Servers and Data Centers

### What is a Server?

A server is a computer that provides data or services to other computers.
- A server provides a response to a request from a client computer over a network.
- Server hardware typically differs from desktop hardware to support the following:
  - More memory and multiple CPUs
  - Redundant power supplies and network interfaces
  - Smaller form factor

### Examples of Servers:
- Web server
- Database server
- Mail server

### Where Does a Server Reside?

Servers reside in a data center. A data center hosts all of an organization’s computer and networking equipment, including the following:
- Servers
- Storage devices
- Network devices (routers, switches, and hubs)
- Cooling equipment
- Uninterruptable power supplies (UPS)

### Who Owns the Data Center?

#### Traditional On-Premises Model
- You own the data center and host it at your location.
- You buy, install, configure, and manage all of the hardware and software in your own facility.
- You hire the staff who are responsible for managing and maintaining the data center.
- You use your own data center resources.

#### Cloud Model
- A cloud services provider owns the data center.
- The cloud services provider buys the hardware and infrastructure software for its own facility.
- The cloud services provider hires the personnel to support the data center.
- You pay to use the cloud service provider’s data center resources.

## Virtual Machines

### What is a Virtual Machine (VM)?

A virtual machine (VM) is a software-based computer.
- A VM runs on a physical computer, which is called a host.
- A software layer, which is called a hypervisor, provides access to the resources of the physical computer (CPU, memory, disk, and network) to the VM.
- The VM runs its own operating system (OS) and interacts with the host through the hypervisor.
- Multiple VMs can be provisioned on a single host.

### Benefits of VMs
- **Cost Savings**: Running multiple VMs on a single physical machine reduces the need to buy a new computer.
- **Efficiency**: Running multiple VMs on a single physical computer increases its utilization.
- **Flexibility**: You can copy a VM image on the same physical host or move it to a different host to duplicate the VM’s computing environment.

## Software Development Life Cycle

### Phases of Software Development
1. **Plan**: What is the problem and what resources do you need to solve it?
2. **Analyze**: What do you want from a solution?
3. **Design**: How will you build what you want?
4. **Develop**: Build what you designed.
5. **Test**: Did you get what you want?
6. **Implement**: Start to use what you built.
7. **Maintain**: Improve what you built.

# Development Team Roles

## Learning Objectives

You will learn how to do the following:
- Identify the different roles in a software development team.
- Identify the responsibilities of the project manager.
- Identify the responsibilities of the analyst.
- Identify the responsibilities of the quality assurance role.
- Identify the responsibilities of the software developer.
- Identify the responsibilities of the database administrator.

### Job Titles for Development Team Roles
- Project manager
- Analyst
- Quality assurance
- Software developer
- Database administrator

### Project Manager
- Is responsible for developing a project plan
- Recruits staff to fulfill other roles
- Leads and manages the project team
- Assigns tasks to different team members
- Determines a timeline for the project
- Provides updates to upper management

### Analyst
- Is sometimes called the business analyst or requirements analyst
- Defines the purpose for each project
- Gathers requirements from leadership, clients, and users
- Organizes requirements into tasks for developers and quality assurance (QA) to use for implementation and testing

### Quality Assurance
- Creates a list of tests that verify function, usability, efficiency, maintainability, and portability for each new requirement
- Maintains the list of tests that are needed to verify the behavior for each previously released feature
- Runs all tests and investigates any failures
- Documents the steps to replicate bugs or issues in the application for the developer
- Assists in creating the acceptance criteria, which are the performance criteria that are used to measure successful completion of the application

### Software Developer
- Writes code to implement the requirements gathered by the analyst
- Fixes bugs identified by the quality assurance team
- Participates in design and code reviews
- Collaborates with other developers and team members

### Database Administrator
- Maintains the data that is needed in the application
- Is responsible for planning, maintaining, and configuring access to that data and for ensuring the availability of enough computing resources to make an application work correctly
- Secures the data in the database
- Backs up data (and restores data as needed)
- Is responsible for database performance and optimization

### Effective Software Teams
- Translate goals into a clear definition of work.
- Prototype and iterate over designs.
- Use version control software to keep track of changes.
- Document important decisions and any required project knowledge.
- Encourage two-way feedback.
- Use time wisely.

# What Is Cloud Computing?

## Learning Objectives

You will learn how to do the following:
- Define cloud computing.
- Describe different service models of cloud computing.
- Distinguish between cloud deployment models.

## Understanding Cloud Computing

### What is Cloud Computing?

- Cloud computing is the on-demand delivery of compute power, database, storage, applications, and other IT resources.
- These resources are delivered through a cloud services platform through the internet with pay-as-you-go pricing.

### Traditional Computing Model

#### Infrastructure as Hardware
- Hardware solutions are physical, and they require the following:
  - Space
  - Staff
  - Physical security
  - Planning
  - Upfront costs
- You must guess at theoretical maximum peaks:
  - Is there enough resource capacity?
  - Do you have sufficient storage?
- What if your needs change?
  - You must go through the time, effort, and costs that are needed to make all necessary changes

### Cloud Service Models
- **IaaS (Infrastructure as a Service)**: More control over IT resources
- **PaaS (Platform as a Service)**
- **SaaS (Software as a Service)**: Less control over IT resources

## Cloud Computing Deployment Models
- **Cloud**
- **Hybrid**
- **Private (On-Premises) Cloud**

### Cloud Infrastructure Compared with On-Premises Infrastructure

#### Cloud
- No upfront investment
- Low ongoing costs
- Focus on innovation
- Flexible capacity
- Speed and agility
- Global reach on demand

#### Hybrid
- Large initial purchase
- Labor, patches, and upgrade cycles
- Systems administration
- Fixed capacity
- Long procurement cycle and setup
- Limited geographic regions

### What Can You Do in the Cloud?
- Application hosting
- Backup and storage
- Content delivery
- Websites
- Enterprise IT
- Databases

# Advantages of Cloud Computing

## Learning Objectives

At the core of the lesson, you will learn how to do the following:
- Identify the advantages of cloud computing.
- Analyze the difference between fixed expense and variable expense.
- Summarize the concept of economics of scale.

You will discuss the following:
- The benefits of cloud computing
- The advantages of moving to the cloud

### Key terms:
- **Fixed expense**: Funds that a company uses to acquire, upgrade, and maintain physical assets, such as property, industrial buildings, or equipment
- **Variable expense**: An expense that the person who bears the cost can alter or avoid
- **Economies of scale**

### How does cloud computing benefit you?

Cloud computing gives you access to servers, storage, databases, and a broad set of application services over the internet. Cloud storage is a good example of cloud computing. Cloud storage gives you the option to free up memory (space) on your computer or mobile device. Imagine a situation where your mobile device runs out of memory when you want to download and save a new song, photo, or video.

### If you have a business, how can cloud computing benefit your business?

Cloud computing or cloud services providers like Amazon Web Services (AWS) provide rapid access to flexible and low-cost IT resources. With cloud computing, you don’t need to make large upfront investments in hardware. As a business owner, you don’t need to purchase a physical location, servers, storage, or databases.

### Why are so many companies interested in moving to the cloud?

Companies are moving to the cloud because it presents many benefits, including cost savings because you pay only for the resources that you use.

### Advantages of Cloud Computing

#### Advantage 1: You can trade fixed expense for variable expense.
Cloud computing allows businesses to convert their capital expenses (CapEx) to operating expenses (OpEx), meaning they only pay for IT resources as they consume them.

#### Advantage 2: You can benefit from massive economies of scale.
By using cloud computing, businesses can benefit from the aggregated demand of numerous customers, leading to lower costs due to bulk purchasing.

#### Advantage 3: Reduce guessing about capacity.
Cloud computing eliminates the guesswork in determining the capacity needs. Businesses can scale up or down as their needs change.

#### Advantage 4: Increase your speed and agility.
Cloud services enable rapid deployment of IT resources, which means businesses can respond quickly to changing demands.

#### Advantage 5: Stop spending money on running and maintaining data centers.
With cloud computing, businesses do not need to invest in or maintain their own data centers.

#### Advantage 6: Go global in minutes.
Cloud services allow businesses to easily deploy applications in multiple regions around the world, providing lower latency and better experiences for customers.

# What Is AWS?

## Learning Objectives

You will learn how to do the following:
- Explain, in general, what a web service is.
- Explore the main services that Amazon Web Services (AWS) offers.
- Examine ways to access AWS services.
- Navigate the AWS documentation website.

### Web Services

What are web services?
A web service is any piece of software that makes itself available over the internet. It uses a standardized format, either Extensible Markup Language (XML) or JavaScript Object Notation (JSON), for the request and the response of an application programming interface (API) interaction.

### AWS Services

AWS is a secure cloud services provider with many services to help businesses scale and grow. These products are delivered over the internet. As a result, you have on-demand access to the compute, storage, network, database, and other IT resources that you might need for your projects. You also have the tools to manage them.

#### Choosing a Service

The service that you select depends on your business goals and technology requirements.

### Three Ways to Interact with AWS

#### AWS Management Console
- The console includes an easier-to-use graphical interface.
- You can access the console on a mobile app.

#### AWS Command Line Interface (AWS CLI)
- With the AWS CLI, you have access to services by discrete commands or scripts.

#### AWS Software Development Kits (SDKs)
- Access services directly from your code (such as Java, Python, and others).

### AWS Documentation
Find user guides, developer guides, API references, tutorials, and more.

#### Summary
- AWS is a cloud services provider. AWS offers a broad set of global cloud-based products—which are also known as services—that are designed to work together.
- AWS offers many service categories, and each category has many services to choose from.
- Choose a service that is based on your business goals and technology requirements.
- You can interact with AWS services in three different ways.
- Use the AWS documentation as your main resource for help.

# AWS Pricing

## Learning Objectives

You will learn how to do the following:
- Describe the Amazon Web Services (AWS) pricing model.
- Explain the advantages of the AWS pricing model.
- Describe the AWS Free Tier offer.
- Explain the concept of total cost of ownership (TCO).
- Identify the purpose of the AWS Pricing Calculator.

### AWS Pricing Model

#### Three Fundamental Drivers of Cost with AWS

- **Compute**: Calculated either by the hour or the second. Varies by instance type (Linux only).
- **Storage**: Charged typically per GB.
- **Data Transfer**: Outbound is aggregated and charged. Inbound has no charge (with some exceptions). Charged typically per GB.

#### How Do You Pay for AWS?
- **Pay for What You Use**: Pay only for the services that you consume with no large upfront expenses.
- **Pay Less When You Reserve**: Reserved Instances are available in three options:
  - All Upfront Reserved Instance (AURI) provides the largest discount.
  - Partial Upfront Reserved Instance (PURI) provides lower discounts.
  - No Upfront Payments Reserved Instance (NURI) provides smaller discounts.
- **Pay Less When You Use More**: As usage increases, pricing per unit decreases.
- **Pay Even Less as AWS Grows**: AWS continuously reduces prices as it grows.

# AWS Global Infrastructure

## Learning Objectives

You will learn how to do the following:
- Describe the AWS Global Infrastructure and its features.
- Identify the difference between Amazon Web Services (AWS) Regions, Availability Zones, and points of presence (PoPs).

### Key Terms
- **Elastic infrastructure**: Infrastructure that dynamically adapts to capacity.
- **Scalable infrastructure**: Infrastructure that adjusts to accommodate growth.
- **Fault tolerance**: The ability of a system to continue operating properly in the presence of a failure.

### AWS Global Infrastructure

The AWS Global Infrastructure is designed and built to deliver a flexible, reliable, scalable, and secure cloud computing environment with high-quality global network performance.

#### AWS Data Centers

The foundation for the AWS infrastructure is the data centers. Data centers usually have specific characteristics, such as the following:
- They are a location where the actual physical data resides and data processing occurs.
- They house physical servers (typically 50,000 to 80,000 servers).
- They are online.
  - All data centers are online.
  - No data center is cold (or not being used).
- Data centers contain AWS custom network equipment, such as the following:
  - Multi-original design manufacturer (ODM) sourced hardware.
  - Amazon custom network protocol stack.

#### AWS Availability Zones

- Each Availability Zone is made up of one or more data centers.
- Availability Zones are designed for fault isolation.
- Availability Zones are interconnected with other Availability Zones by using high-speed private links.
- You choose your Availability Zones.
- AWS recommends replicating across Availability Zones for resiliency.

#### AWS Regions

- An AWS Region is a geographical area.
- Each Region is made up of two or more Availability Zones.
- AWS has 24 Regions worldwide.
- You activate and control data replication across Regions.
- Communication between Regions uses AWS backbone network connections infrastructure.

#### Points of Presence

AWS provides a global network of 216 PoP locations.
- The PoPs consist of 205 edge locations and 11 Regional edge caches.
- PoPs are used with Amazon CloudFront, a global content delivery network (CDN) that delivers content to end users with reduced latency.
- Regional edge caches are used for content with infrequent access.

### AWS Infrastructure Features

- **Elastic and Scalable**:
  - Elastic infrastructure dynamically adapts to capacity.
  - Scalable infrastructure adjusts to accommodate growth.
- **Fault-tolerant**:
  - Continues operating properly in the presence of a failure.
  - Includes built-in redundancy of components.
- **Highly Available**:
  - High level of operational performance with reduced downtime.

# AWS Services and Service Categories

## Learning Objectives

At the core of the lesson, you will learn how to identify AWS services and service categories.

### AWS Service Categories

#### AWS Cost Management
- **AWS Cost and Usage Report**
- **AWS Budgets**
- **AWS Cost Explorer**

#### Compute
- **Amazon Elastic Compute Cloud (Amazon EC2)**
- **Amazon EC2 Auto Scaling**
- **AWS Elastic Beanstalk**
- **AWS Lambda**

#### Containers
- **Amazon Elastic Container Service (Amazon ECS)**
- **Amazon Elastic Container Registry (Amazon ECR)**
- **Amazon Elastic Kubernetes Service (Amazon EKS)**

#### Database
- **Amazon Relational Database Service (Amazon RDS)**
- **Amazon Aurora**
- **Amazon Redshift**
- **Amazon DynamoDB**

#### Management and Governance
- **AWS Management Console**
- **AWS Config**
- **Amazon CloudWatch**
- **AWS Auto Scaling**
- **AWS Command Line Interface (AWS CLI)**
- **AWS Trusted Advisor**
- **AWS Well-Architected Tool**
- **AWS CloudTrail**

#### Networking and Content Delivery
- **Amazon Virtual Private Cloud (Amazon VPC)**
- **Elastic Load Balancing**
- **Amazon CloudFront**
- **AWS Transit Gateway**
- **Amazon Route 53**
- **AWS Direct Connect**
- **AWS Client VPN**

#### Security, Identity, and Compliance
- **AWS Identity and Access Management (IAM)**
- **AWS Organizations**
- **Amazon Cognito**
- **AWS Artifact**
- **AWS Key Management Service (AWS KMS)**
- **AWS Shield**

#### Storage
- **Amazon Simple Storage Service (Amazon S3)**
- **Amazon Elastic Block Store (Amazon EBS)**
- **Amazon Elastic File System (Amazon EFS)**
- **Amazon Simple Storage Service Glacier**

# Shared Responsibility Model

## Learning Objectives

You will learn how to do the following:
- Describe AWS Cloud security and the shared responsibility model.
- Identify the security responsibilities of Amazon Web Services (AWS) compared with the security responsibilities of the customer.

### AWS Security Responsibilities: Security OF the Cloud

- **Physical security of data centers**:
  - Controlled, need-based access.
- **Hardware and software infrastructure**:
  - Storage decommissioning, host operating system (OS) access logging, and auditing.
- **Network infrastructure**:
  - Intrusion detection.
- **Virtualization infrastructure**:
  - Instance isolation.

### Customer Security Responsibilities: Security IN the Cloud

- **Amazon Elastic Compute Cloud (Amazon EC2) instance OS**:
  - Including patching and maintenance.
- **Applications**:
  - Passwords, role-based access, and others.
- **Security group configuration**:
  - OS-based or host-based firewalls, including intrusion detection or prevention systems.
- **Network configurations**:
  - Account management, login and permission settings for each user.

### Service Characteristics and Security Responsibility

#### Infrastructure as a Service (IaaS)

- The customer has more flexibility over configuring networking and storage settings.
- The customer is responsible for managing more aspects of the security.
- The customer configures the access controls.

#### Platform as a Service (PaaS)

- The customer doesn’t need to manage the underlying infrastructure.
- AWS handles the operating system, database patching, firewall configuration, and disaster recovery (DR).
- The customer can focus on managing code or data.

#### Software as a Service (SaaS)

- Software is centrally hosted.
- It is licensed on a subscription model or pay-as-you-go basis.
- Services are typically accessed through a web browser, mobile app, or application programming interface (API).
- Customers don’t need to manage the infrastructure that supports the service.

# Amazon S3

## Amazon Simple Storage Service (Amazon S3)

### Learning Objectives

You will learn how to do the following:
- Describe the purpose and benefits of Amazon Simple Storage Service (Amazon S3).
- Explain the basic pricing that Amazon S3 uses.

### Amazon S3

#### Managed Cloud Storage Solution

- Data is stored as objects in buckets.
- Storage is virtually unlimited:
  - A single object can be up to 5 TB.
- Amazon S3 is designed for 11 9s (99.999999999 percent) of durability.
- Customers have granular access to bucket and objects.

### Amazon S3 Features

- You can virtually store as many objects as you want.
- By default, your data is private, and you can optionally encrypt it.
- Data is stored redundantly.
- You can retrieve data anytime from anywhere over the internet.
- Bucket names must be unique across all existing bucket names in Amazon S3.

### Access the Data Anywhere

- **AWS Management Console**
- **AWS CLI**
- **AWS SDKs**
- **REST endpoints**

### Redundancy in Amazon S3: How Data Is Redundantly Stored in a Region

When you create a bucket in Amazon S3, it is associated with a specific AWS Region. Whenever you store data in the bucket, it is redundantly stored across multiple AWS facilities in your selected Region.

### Seamless Scaling

Amazon S3 is designed for seamless scaling. Amazon S3 automatically manages the storage behind your bucket even when your data grows. Because of this system, you can get started immediately and have your data storage grow with your application needs.

### Common Use Cases for Amazon S3

- Storage for application assets.
- Static web hosting.
- Backup and disaster recovery (DR).
- Staging area for big data.

### Amazon S3 Pricing

#### Pay for Only What You Use

- **GBs per month**
- **Transfer out to other Regions**
- **PUT, COPY, POST, LIST, and GET requests**

#### You Do Not Have to Pay for the Following:

- **Transfer in to Amazon S3**
- **Transfer out from Amazon S3 to Amazon CloudFront or Amazon EC2 in the same Region**

# Amazon EC2

## Amazon Elastic Compute Cloud (Amazon EC2)

### Learning Objectives

You will learn how to do the following:
- Explain the features and uses of Amazon Elastic Compute Cloud (Amazon EC2).
- Launch an EC2 instance.
- Describe the pricing options for Amazon EC2.

### Example Uses of EC2 Instances

- Application server
- Web server
- Database server
- Game server
- Mail server
- Media server
- Catalog server
- File server
- Computing server
- Proxy server

### Amazon EC2 Overview

- Amazon EC2 provides virtual machines—referred to as EC2 instances—in the cloud.
- With Amazon EC2, you have full control over the guest operating system (OS)—either Microsoft Windows or Linux—on each instance.
- You can launch instances of any size into an Availability Zone anywhere in the world.
- Launch instances from Amazon Machine Images (AMIs).
- Launch instances with a few clicks or a line of code, and they are ready in minutes.
- You can control traffic to and from instances.

### Choices to Make by Using the Launch Instance Wizard

1. **AMI**
2. **Instance type**
3. **Network settings**
4. **IAM role**
5. **User data**
6. **Storage options**
7. **Tags**
8. **Security group**
9. **Key pair**

### Amazon EC2 Pricing Models: Benefits

#### On-Demand Instances

- Offer low cost and flexibility.
- Are good for large-scale, dynamic workloads.

#### Spot Instances

- Offer predictability, which helps ensure that compute capacity is available when needed.
- Save money on licensing costs.
- Help meet compliance and regulatory requirements.

#### Reserved Instances

- Help meet compliance and regulatory requirements.
- Offer lower cost.

#### Dedicated Hosts

- Save money on licensing costs.
- Help meet compliance and regulatory requirements.

### Amazon EC2 Pricing Models: Use Cases

#### Spiky Workloads

- On-Demand Instances
  - Short-term, spiky, or unpredictable workloads.
  - Application development or testing.

#### Time-Insensitive Workloads

- Spot Instances
  - Applications with flexible start and end times.
  - Applications that are feasible at only very low compute prices.
  - Users with urgent computing needs for large amounts of additional capacity.

#### Steady-State Workloads

- Reserved Instances
  - Steady-state or predictable usage workloads.
  - Applications that require reserved capacity, including disaster recovery (DR).
  - Users able to make upfront payments to reduce total computing costs even further.

#### Highly Sensitive Workloads

- Dedicated Hosts
  - Bring Your Own License (BYOL) model.
  - Compliance and regulatory restrictions.
  - Usage and licensing tracking.
  - Ability to control instance placement.

### Summary

- With Amazon EC2, you can run Microsoft Windows and Linux virtual machines in the cloud.
- An AMI provides the information that is needed to launch an EC2 instance.
- An EC2 instance type defines a configuration of CPU, memory, storage, and network performance characteristics.
- When you launch an EC2 instance, you must choose an AMI and an instance type. You must also specify key configuration parameters, including network, security, storage, and user data settings.
- Amazon EC2 pricing models include On-Demand Instances, Reserved Instances, Spot Instances, and Dedicated Hosts.
