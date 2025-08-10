package docker.security

deny[msg] {
  input.User == "root"
  msg = "Uso de usuário root não permitido na imagem Docker"
}
