######################################
#Author: Amy X. Guo 
#Institution: Duke University 
#Lab: Sue Jinks-Robertson Lab
######################################

python Barcode_in.py
python WinGen.py
python Ref_builder.py
python sorthat.py
python prep_input.py
cat input.in|variant_calling.sh
python ext_variant.py