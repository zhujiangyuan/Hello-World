g_default_path = 'D:\\Applications'
g_input_path = ''
g_work_path = '\\dev\\src\\'
g_full_work_path = ''
g_project_order_list = []
g_project_order_file_name = '\\auto_build_project_order.txt'
g_build_chain_file_name = '\\build_chain.txt'
g_hg_command_pull = 'hg pull'
g_hg_command_update = 'hg update'
g_gradlew_command = '\\gradlew.bat fAD cR bR'

import sys
import os

# Get input path
arg_num = len(sys.argv)
if(0 == arg_num):
   g_input_path = g_default_path
else:
   g_input_path = g_default_path
g_full_work_path = g_input_path + g_work_path

# Read project order from file
project_order_file_path = os.getcwd() + g_project_order_file_name
openfile= open(project_order_file_path)
while True:
    line = openfile.readline()
    if len(line) == 0:
        break
    else:
        g_project_order_list.append(line)
openfile.close()

#Red build chain
g_build_chain_list = []
openfile= open(os.getcwd() + g_build_chain_file_name)
while True:
    line = openfile.readline()
    if len(line) == 0:
        break
    else:
        g_build_chain_list.append(line)
openfile.close()

#Get all projects

class Poject:
    ''' This class represents each projec. '''
    def __init__ (self, project_name, project_full_path):
        self.project_name = project_name
        self.project_full_path = project_full_path

g_unordered_project_list = []

dirpath, dirnames, filenames = os.walk(g_full_work_path)
for dirpath, dirnames, filenames in  os.walk(g_full_work_path):
    for each_dirname in dirnames:
        full_path = dirpath + each_dirname
        each_project = Poject (each_dirname, full_path)
        g_unordered_project_list.append(each_project)
       

#for poject in g_unordered_project_list:
#   print(poject.project_full_path)

#Sort project
g_ordered_project_list =[]
for project_name in g_build_chain_list:
    for project_name_need_complie in g_unordered_project_list:
        if(project_name_need_complie == project_name) :
           g_ordered_project_list.append(project_name_need_complie)
        
# Update Source code
for project in g_ordered_project_list:
    os.chdir(project.project_full_path)
    os.popen(g_hg_command_pull)
    os.popen(g_hg_command_update)
    
# Run gradle command
for project in g_ordered_project_list:
    gradlew_cmd = project.project_full_path + g_gradlew_command
    os.popen(gradlew_cmd)


