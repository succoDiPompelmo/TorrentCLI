from PyInquirer import style_from_dict, Token, prompt, Separator

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

questions = [
    {
        'type': 'input',
        'message': 'What are you searching ?',
        'name': 'search_text',
        'validate': lambda x: True if x else "You must insert a search text"
    },
    {
        'type': 'input',
        'message': 'How many torrents to display ?',
        'name': 'search_count',
        'default': '20',
        'validate': lambda x: True if x.isdigit() else "Insert a positive whole number"
    },
    {
        'type': 'checkbox',
        'message': 'Select search engine',
        'name': 'search_engine',
        'choices': [
            Separator('= Search Engine Available ='),
            {
                'name': 'Tpb',
                'checked': True
            },
            {
                'name': 'Snowfl',
                'checked': True
            }
        ],
    }
]

def make_inquiry():
    answer = prompt(questions, style=style)
    return answer['search_engine'], answer['search_text'], int(answer['search_count'])