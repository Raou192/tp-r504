docker run -d \
	--name tp2-app \
	--network net-tp4 \
	-p 5001:5000 \
	--mount type=bind,src=/home/fi25-pinel/srvapp_1.py,dst=/srv/app_1.py \
	im-tp2
