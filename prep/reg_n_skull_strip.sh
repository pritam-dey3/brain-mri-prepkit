inp_folder=/home/tapan/Documents/AI/AlzheimerClassification/data/TADPOLE_EMCI/EMCI/
reg_folder=/home/tapan/Documents/AI/AlzheimerClassification/data/TADPOLE_EMCI/EMCI_reg_v2
skull_strip_folder=/home/tapan/Documents/AI/AlzheimerClassification/data/TADPOLE_EMCI/EMCI_wo_skull_v2

echo "starting registration..."
python registration.py $inp_folder $reg_folder

echo "starting skull stripping..."
python skull_stripping.py $reg_folder $skull_strip_folder