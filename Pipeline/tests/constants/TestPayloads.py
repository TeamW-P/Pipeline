# Stores all payloads for use in testing

# STRING INPUT

STRING_INPUT_SUCCESS = {'dataset': 'ALL',
                        'sequence': 'UUUUUUAAGGAAGAUCUGGCCUUCCCACAAGGGAAGGCCAAAGAAUUUCCUU',
                        'score_threshold': '0',
                        'sample_size': '1000',
                        'theta': '1',
                        'lambda': '0.35',
                        'window_length': '200',
                        'step_size': '100',
                        'modules': '',
                        'constraints': '',
                        'get_graphs': '1',
                        'pdb': '1'}

STRING_INPUT_INCORRECT_DATASET = {'dataset': 'BAD',
                                  'sequence': 'UUUUUUAAGGAAGAUCUGGCCUUCCCACAAGGGAAGGCCAAAGAAUUUCCUU'}

# FILE INPUT

FILE_INPUT_SEQUENCE_NO_SS = {'dataset': 'ALL',
                             'secondary_structure_infile': '0',
                             'score_threshold': '0',
                             'sample_size': '1000',
                             'theta': '1',
                             'lambda': '0.35',
                             'window_length': '200',
                             'step_size': '100',
                             'modules': '',
                             'constraints': '',
                             'aln': '0',
                             'get_graphs': '1',
                             'pdb': '1'}

FILE_INPUT_INCORRECT_DATASET = {'dataset': 'SPECIAL',
                                'secondary_structure_infile': '0',
                                'score_threshold': '0',
                                'sample_size': '1000',
                                'theta': '1',
                                'lambda': '0.35',
                                'window_length': '200',
                                'step_size': '100',
                                'modules': '',
                                'constraints': '',
                                'get_graphs': '1',
                                'pdb': '1'}

# GRAPH RETRIEVAL

GRAPH_RETRIEVAL_SUCCESS = {'dataset': 'ALL',
                           'modules': '["36", "48"]'
                           }
GRAPH_RETRIEVAL_EMPTY_MODULES = {'dataset': 'ALL',
                                 'modules': '[]'}
GRAPH_RETRIEVAL_BAD_DATASET = {'dataset': 'ILLEGAL',
                               'modules': '["36", "48"]'}
GRAPH_RETRIEVAL_INVALID_MODULE = {'dataset': 'ALL',
                                  'modules': '["36", "1000"]'}
