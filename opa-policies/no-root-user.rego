package docker.security

# Regra para proibir o uso do usuário root (UID 0) na imagem Docker
deny[msg] {
  input.User == "root"
  msg := "Uso de usuário root não permitido na imagem Docker"
}
