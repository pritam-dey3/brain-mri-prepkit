inp_folder=/home/tapan/Documents/AI/AlzheimerClassification/data/TADPOLE_LMCI/LMCI/
reg_folder=/home/tapan/Documents/AI/AlzheimerClassification/data/TADPOLE_LMCI/LMCI_reg_v2
skull_strip_folder=/home/tapan/Documents/AI/AlzheimerClassification/data/TADPOLE_LMCI/LMCI_wo_skull_v2

echo "starting registration..."
python3 registration.py $inp_folder $reg_folder

echo "starting skull stripping..."
python3 skull_stripping.py $reg_folder $skull_strip_folder