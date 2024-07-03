
resource "aws_iam_user" "user" {
  name = "Andres"
    tags = {
        name = "My-First-IAMUser"
    }
}