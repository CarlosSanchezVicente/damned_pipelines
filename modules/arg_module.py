import argparse

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Choose your repository')
    help_message = 'You have two options: Option 1: "lab_name" show only the pull request relate to a particular lab \
        Opcion 2: "all" show all the pull request'
    parser.add_argument('-p', '--parameter', help=help_message, type=str)
    args = parser.parse_args()
    return args
