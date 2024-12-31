#!/bin/bash

is_ffmpeg=$(command -v ffmpeg)

sudo apt update

if [ -z "$is_ffmpeg" ]; then
	echo "Se detecto que no tiene instalado ffmpeg, por lo cual se procederá con su instalación"
	sudo apt install -y ffmpeg
	if [ -z "$is_ffmpeg" ]; then
		echo "El comando ffmpeg se instalo correctamente"
	else
		echo "El comando ffmpeg no se instalo correctamente"
	fi
fi

# Create and active Virtual Environment for this project
python3 -m venv q-web-mult
source q-web-mult/bin/activate

pip install -r requirements.txt
