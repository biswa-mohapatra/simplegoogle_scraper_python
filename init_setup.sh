echo [$(date)] : "START"
echo [$(date)] : "CREATING CONDA ENVIROMENT WITH PYTHON=3.8"
export _VERSION_ = 3.8
conda create --prefix ./env python=3.8 -y
echo [$(date)] : "ACTIVATE ENVIROMENT"
source activate ./env
echo [$(date)] : "INSTALLING DEV REQUIREMENTS"
pip install -r requirements_dev.txt
echo [$(date)] : "END"