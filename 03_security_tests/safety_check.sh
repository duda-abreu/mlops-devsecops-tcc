#!/bin/bash
echo "Rodando Safety"
pip freeze > requirements.txt
safety check -r requirements.txt
