
resource "aws_eip" "ExamEIP" {
    domain = "vpc"
    tags = {
        name = "My-First-ExamEIP"
    }
  
}