resource "aws_instance" "ExampleEc2" {
  ami = "ami-00c39f71452c08778"
  instance_type = "t2.micro"

    tags = {
        name = "My-First-ExampleEc2"
    }
}