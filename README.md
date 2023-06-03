**YC-On-Rails: Cloud-Based Startup Incubation Platform**

The goal is to create a robust, scalable and secure web application to provide services for startup founders. This application will allow startups to apply for funding, track progress, receive feedback, and collaborate with mentors.

**Objective:**

The main objective of this project is to build a secure, scalable, and maintainable infrastructure for the startup incubation platform using AWS, Docker, and Terraform, and develop the application using Ruby on Rails, Postgres, and React.

**Steps:**

1. **Platform Architecture Design:** Define the architecture of the platform in AWS. Determine which services are necessary and how they should interact. Define how the infrastructure will be deployed using Docker and Terraform.

2. **Infrastructure Deployment:** Use Terraform to write infrastructure as code for all required AWS services. Implement Docker for the deployment of the application. Use AWS ECS and RDS for container orchestration and database management respectively.

3. **Application Development:** Develop the application using Ruby on Rails for the backend and React for the frontend. The application should support user authentication, application submission, feedback mechanisms, and other features relevant for startup incubation.

4. **Shared Infrastructure:** Create shared infrastructure for email subscriptions and unsubscribes across different product teams. This could involve integrating with an email service like AWS SES and writing shared Ruby and TypeScript code for managing subscriptions.

5. **Performance Monitoring & Debugging:** Implement AWS CloudWatch to monitor the application and infrastructure. Debug any performance issues in the web application.

6. **Security Management:** Ensure the security of applications and data. Implement IAM for access management and work with external security auditors for penetration testing.

7. **Developer Experience:** Implement tools and practices that improve developer productivity and allow for quicker deployments. For example, simplifying the use of Webpack and JavaScript for faster deployments.

**Deliverables:**

1. **Infrastructure Code:** Terraform scripts for creating and managing the infrastructure on AWS. Dockerfiles for the application's containerization.

2. **Application Code:** Well-structured and documented Ruby on Rails and React codebase for the startup incubation platform.

3. **Documentation:** Comprehensive documentation of the infrastructure design, application architecture, deployment process, and developer tools. 

4. **Security Audit Report:** A report from a penetration testing exercise against your applications.


# Architecture

![image](https://github.com/LNshuti/yc-on-rails/assets/13305262/0f911326-ff4f-41ed-ad62-dcfbc6c928ca)
