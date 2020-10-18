# TODO: Add space to allow multi choice definition

def parse_results_command(cmd):

    code = cmd[0]

    if code not in 'sctdrqh':
        print("Insert a valid code")
        return None, None

    try:
        choice = int(cmd[1:])
    except ValueError:
        choice = None

    return code, choice