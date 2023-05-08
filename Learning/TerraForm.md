TerraForm is a opensource tool used for provisioning infrastructure resources. It works as Infrastructure-as-code. It supports DevOps best practices for change management.

It is basically version-controlled configuration repo for infrastructure provisioning of test or prod server.

Install terraform:

        brew install terraform

Create some initial files required for terraform at a desired folder:

    .terraform-version
    main.tf
    variables.tf

    files with .tf are terraform files

To start with terraform, just run

        terraform init
    
in the folder structure you are required.

Declaratives required:

1. terraform - parent declarative.
2. backend - configurations related to backend 
3. required_providers - optional
4. provider - resources, generally cloud, configurations related to it.

Execution commands:

1. terraform init - initialize and install
2. terraform plan - Match changes against the previous state. It shows what are all changes will be applied.
3. terraform apply - apply changes to cloud. 
4. terraform destroy - Remove your stack from cloud