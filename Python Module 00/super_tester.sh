#!/bin/bash

# Cores
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}🔧 Preparando Ambiente...${NC}"

# Ativar venv
source matrix_env/bin/activate

# Instalar requisitos se necessário
pip install -q flake8 mypy

# Correr o Super Tester
python3 super_tester.py

deactivate