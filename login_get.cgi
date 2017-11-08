#!/bin/bash
falhou(){
echo "<h2>Deu merda</h2>"
}
administrador(){
echo "<h1> administrador logou</h1>"
exit 0
}
tecnico(){
echo "<h1> tecnico logou </h1>"
exit 0
}
usuario(){
echo "<h1> pagina do usuário</h1>"
}
passou(){
[[ $1 == "administrador" ]] && administrador
[[ $1 == "tecnico" ]] && tecnico
[[ $1 == "usuario" ]] && usuario
}
verifica(){
USER=$1
PASS=$2
SENHA=$(cat passwd | grep ^$USER: | cut -d":" -f2)
[[ $PASS == $SENHA ]] && passou $USER || falhou
}
read login
USER=$(echo $login | cut -d"&" -f1 | cut -d"=" -f2 )
PASS=$(echo $login | cut -d"&" -f2 | cut -d"=" -f2 )
echo content-type: text/html
echo
[[ $(cat passwd | cut -d":" -f1 | grep ^$USER$) ]] && verifica $USER $PASS || falhou
