#!/bin/sh

until $(curl --output /dev/null --silent --head http://apollo:8080/apollo/annotator/index ); do
    echo "$(date) - waiting for apollo..."
    sleep 5
done

echo "Connected, registering user ${ADMIN_USERNAME}"

curl 'http://apollo:8080/apollo/login/registerAdmin' \
	--connect-timeout 2 \
	 -H 'Content-type: application/x-www-form-urlencoded' \
	 --data 'data={"operation":"register", "username":"'${ADMIN_USERNAME}'", "password":"'${ADMIN_PASSWORD}'", "rememberMe":false, "firstName":"'${ADMIN_FIRST_NAME}'", "lastName":"'${ADMIN_LAST_NAME}'"}'
