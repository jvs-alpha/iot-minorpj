echo -e "Enter the server ip: \c"
read serverip
echo -e "Enter the node ip: \c"
read nodeip
echo -e "Enter the node name: \c"
read nodename
user_token=$(curl -u jvs:ggsafehouse http://$serverip:3001/login)

curl -X POST \
  http://127.0.0.1:3000/user \
  -H 'Content-Type: application/json' \
  -H '$(token_read)' \
  -H 'Postman-Token: 24d087a5-a236-42be-9449-d214dfea7cdc' \
  -H 'cache-control: no-cache' \
  -d '{"nodename":"$nodename", "ip":"$(serverip)"}'
