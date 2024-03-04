terraform {
  required_version = ">=1.3.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">=5.38.0"
    }
  }
}

provider "aws" {
  region  = "us-east-1"
  profile = "default"
}

variable "bucketToCreate" {
  type = string
}

module "s3" {
  source         = "./modules/s3"
  bucketToCreate = var.bucketToCreate
}

output "s3BucketName" {
  value = module.s3.s3BucketName
}
