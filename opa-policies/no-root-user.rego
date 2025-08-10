package docker.security

deny {
  input.User == "root"
}

deny_msg[msg] {
  deny
  msg = "Uso de usuário root não permitido na imagem Docker"
}
