variable "region" {
  description = "AWS region where resources will be deployed"
  type        = string
  default     = "us-east-1"
}

variable "initial_string" {
  description = "Initial dynamic string value"
  type        = string
  default     = "The saved string is dynamic string"
}