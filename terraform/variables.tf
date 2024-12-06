variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-west-2"
}

data "aws_availability_zones" "available" {
  state = "available"
}
