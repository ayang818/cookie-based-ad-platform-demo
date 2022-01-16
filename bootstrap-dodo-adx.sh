docker build -t "cookie-based-ad-platform:1.0" .
echo 'suc build backend'
docker rm -fv "ad-platform-demo"
echo "suc delete backend"
docker run -d --name "ad-platform-demo" -p 5050:80 cookie-based-ad-platform:1.0
echo 'suc run backend'