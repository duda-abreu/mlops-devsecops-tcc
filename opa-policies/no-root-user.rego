package docker.security

deny[msg] if input.User == "root" {
  msg = "Uso de usuário root não permitido na imagem Docker"
}
