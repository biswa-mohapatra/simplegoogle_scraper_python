echo [$(date)] : "START"
echo [$(date)] : "CREATING CONDA ENVIROMENT WITH PYTHON=3.7"
export _VERSION_ = 3.7
conda create --prefix ./env python=3.7 -y
echo [$(date)] : "ACTIVATE ENVIROMENT"
source activate ./env
echo [$(date)] : "INSTALLING DEV REQUIREMENTS"
pip install -r requirements_dev.txt
echo [$(date)] : "END"