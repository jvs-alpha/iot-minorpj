echo -e "Enter the server ip: \c"
read serverip
echo -e "Enter the node ip: \c"
read nodeip
echo -e "Enter the node name: \c"
read nodename
user_token=$(curl -u jvs:ggsafehouse http://$serverip:3001/login)
head="'Cookie: $user_token'"
data="'{"nodename":"$nodename","ip":"$nodeip"}'"
echo $head
#curl -X POST http://127.0.0.1:3000/user $head $data
curl -v -X POST \
  http://127.0.0.1:3000/user \
  -H 'Content-Type: application/json' \
  -H $head \
  -H 'Postman-Token: e341759e-ec69-4e9e-b660-e5079fef912c' \
  -H 'cache-control: no-cache' \
  -d $data
