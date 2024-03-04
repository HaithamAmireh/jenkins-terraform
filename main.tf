terraform {
  required_version = ">=1.3.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">=5.38.0"
    }
  }
}

module "s3" {
  source         = "./modules/s3"
  bucketToCreate = "bucket-via-jenkins"
}

output "s3BucketName" {
  value = module.s3.s3BucketName
}
