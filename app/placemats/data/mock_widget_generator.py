from app.placemats.data.mock_data import *


def generate_mock_widgets(term=None):
    return [
        {
            'type': 'adj_matrix',
            'status': 'complete',
            'name': 'Question 1 (Adjacency List)',
            'description': '',
            'data': ADJ_MATRIX_DATA
        }, {
            'type': 'budget',
            'status': 'complete',
            'name': 'Question 2 (Budget viewer)',
            'description': '',
            'data': {
                'budget_array_data': BUDGET_DATA_ARRAY,
                'category_data': BUDGET_CAT_DATA,
                'category_list': BUDGET_CAT_LIST
            }
        }, {
            'type': 'collapsible',
            'status': 'complete',
            'name': 'Question 3 (Collapsible layout)',
            'description': '',
            'data': COLLAPSIBLE_DATA
        }, {
            'type': 'concept_map',
            'status': 'complete',
            'name': 'Question 4 (Concept map)',
            'description': '',
            'data': {
                'source1': CONCEPT_MAP_1,
                'source2': CONCEPT_MAP_2,
                'source3': CONCEPT_MAP_3,
                'source4': CONCEPT_MAP_4
            }
        }, {
            'type': 'hierarchical',
            'status': 'complete',
            'name': 'Question 5 (Hierarchical layout)',
            'description': '',
            'data': {
                'source1': HIERARCHICAL_DATA_1,
                'source2': HIERARCHICAL_DATA_2
            }
        }, {
            'type': 'word_cloud',
            'status': 'complete',
            'name': 'Question 6 (Time series)',
            'description': '',
            'data': TIME_SERIES_DATA
        }, {
            'type': 'world_map',
            'status': 'complete',
            'name': 'Question 7 (World map)',
            'description': '',
            'data': WORLD_MAP_DATA
        }
    ]
