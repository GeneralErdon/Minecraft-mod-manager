#!/bin/bash
set -o errexit

RUTA=$(pwd) # Establece la RUTA actual

if [ ! -d "env" ]; then # verifica la existencia del entorno virtual
    python3.11 -m virtualenv env
fi

$RUTA/env/bin/python -m pip install -r $RUTA/requirements.txt
$RUTA/env/bin/python -m flet pack $RUTA/main.py