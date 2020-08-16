#    _                                                            _ 
# __| |__________________________________________________________| |__
#(__   __________________________________________________________   __)
#   | | This takes a list of DAT files in the working directory  | |   
#   | |             and feeds each through OGP2SA.py             | |   
#   | |                                                          | |   
# __| |__________________________________________________________| |__
#(__   __________________________________________________________   __)
#   !_!                                                          !_!

ls *.DAT > dat_files.log
sed -i '' 's/ /\\ /g' dat_files.log
sed -i '' 's/.*/python OGP2SA.py &/' dat_files.log
source dat_files.log
rm dat_files.log
