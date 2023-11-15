# IMPORTS LIBRARIES
import os
from dotenv import load_dotenv

# IMPORT FUNCTION FROM "module.py"
from modules import module as mod
from modules import arg_module as marg

# INI
# Import GITHUB token from '.env'
load_dotenv('.env')   # Con '../' lo que hacemos es salir de la carpeta de notebook, a la carpeta principal donde está el
                      # archivo main, que es donde está el archivo '.env'.
TOKEN = os.environ.get('API_TOKEN')

# Endpoint contruction
API_TOKEN = TOKEN   #API TOKEN (REMEMBER: do not push these to your repo)
USERNAME = 'CarlosSanchezVicente'   #USERNAME
BASE_URL = 'https://api.github.com/'
KEY = 'repos/'
OWNER = 'ih-datapt-mad/'
REPO = 'dataptmad0923_labs/'   #LAB_REPOSITORY
SEARCH = 'search/issues?q=repo:'+OWNER+REPO+'+type:pr+state:{}'
PULLS = 'pulls?page={}&per_page=100&state={}'
COMMITS = 'pulls/{}/commits'
STATE = 'open'

# Create list as input the funcions
field_list1 = ['number',
               'title',
               'state',
               'created_at',
               'updated_at',
               'closed_at',
               'html_url',
               'base.repo.full_name',
               'base.ref',
               'head.repo.full_name',
               'head.ref',
               'head.repo.pushed_at']
field_list2 = ['student_name',
               'number',
               'lab_name',
               'state',
               'lab_status',
               'created_at',
               'updated_at',
               'closed_at',
               'html_url',
               'base.repo.full_name',
               'base.ref',
               'head.repo.full_name',
               'head.ref',
               'head.repo.pushed_at']  
field_sort1 = ['lab_status',
               'lab_name',
               'student_name'] 
field_name1 = ['Student Name',
               'PR Number',
               'Lab Name',
               'PR Status',
               'Lab Status',
               'PR Created at',
               'PR Updated at',
               'PR Closed at',
               'PR URL',
               'base repository',
               'base',
               'head repository',
               'compare',
               'Pushed at']

# MAIN FUNCTION
def main():
    # Pipeline to extract the data, store this data in a dataframe 
    DF_PULLS = mod.get_pulls(BASE_URL, KEY, OWNER, REPO, PULLS, SEARCH, STATE, USERNAME, API_TOKEN, field_list1)
    DF_STATUS = mod.df_status(DF_PULLS, BASE_URL, KEY, OWNER, REPO, COMMITS, USERNAME, API_TOKEN, field_list2)
    DF_CSV = mod.create_csv(DF_STATUS, field_sort1, field_name1) 

    # Filter the dataframe if the user change the flag in the input
    #'''
    # Store the parser argumnent in a variable. Add '[' and ']' because in the dataframe the data are in this format: [lab_name]
    output_argp = '[' + marg.argument_parser().parameter + ']'

    # If argparser is equal than 'all' the output will be the complete dataframe
    if output_argp == 'all':
        return DF_CSV
    
    # If the user enters the specific lab name as an input
    else:
        # Create a filter with the rows that includes the specific lab
        filter_df = DF_CSV['Lab Name'] == output_argp
        # Evaluate if at least one element in condition is True. If True, it means that there is at least one row that meets the condition. If not
        # the return is a error message
        if filter_df.any():   
            return DF_CSV[filter_df]
        else:
            return 'Error: the name of the lab you typed was not found'

# MAIN EXECUTION
if __name__ == '__main__':
    DF_CSV = main()
    print(DF_CSV)