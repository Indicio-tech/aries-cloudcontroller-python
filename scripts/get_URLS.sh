#script to get notebook URLs
for i in `docker ps --format "table {{.Names}}" | grep notebook`; do token=$(docker logs  $i 2>&1 | grep "127.0.0.1):8888/" | cut -d"=" -f2 | head -1); echo "$i - http://127.0.0.1:8888/?token=$token"; done