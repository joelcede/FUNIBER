#!/bin/bash

ENV_NAME="venv"

if [ -d "$ENV_NAME" ]; then
    echo "La carpeta del entorno virtual ya existe: $ENV_NAME"
else
    # Crear el entorno virtual si no existe
    python3 -m venv $ENV_NAME
    PIP_EXEC="$ENV_NAME/bin/pip"
    # En Windows (Git Bash, Cygwin, o MSYS2), la ruta sería diferente
    OS="$(uname -s)"
    case "${OS}" in
        MINGW*|CYGWIN*|MSYS*)
            PIP_EXEC="$ENV_NAME/Scripts/pip"
            ;;
    esac

    $PIP_EXEC install colorama
    echo "Entorno virtual creado: $ENV_NAME"
    $PIP_EXEC list
fi

