def namelist(lst):
    result = ''
    for i, dic in enumerate(lst):
        result += dic['name'];
        if i < len(lst) - 2:
            result += ", "
        elif i == len(lst) - 2:
            result += " & "
    print(result)


namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]) # returns 'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]) # returns 'Bart & Lisa'
namelist([ {'name': 'Bart'} ]) # returns 'Bart'
namelist([]) # returns ''
