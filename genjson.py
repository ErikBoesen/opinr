import random
import json

issues = [
    'Net Neutrality',
    'Social Network Regulation',
    'Education Policy',
    'Presidential Administration',
    'Congressional Term Limits',
    'Lobbying Regulation',
    'Tobacco Regulation',
    'Climate Change',
    'Hate Speech Laws',
    'Russian Interference in 2016 US Presidential Election',
    'Immigration',
    'Police Brutality',
    'Defense Investment',
    'Border Wall',
    'US—China Foreign Policy',
    'Budget Cuts',
    'Veteran Affairs',
    'Marriage Equality',
    'Transgender Bathrooms',
    'Transportation Funding',
    'Womens\' Rights',
    'Gender Wage Gap',

]

data = [
    {
        'id': 5+index,
        'slug': '',
        'title': issue,
        'articles': [
            {
                'source': '',
                'lean': random.random() * 20 - 10,
                'url': ''
            } for i in range(0, random.randint(5, 20))
        ]
    } for index, issue in enumerate(issues)
]

print(json.dumps(data)[1:-1])
