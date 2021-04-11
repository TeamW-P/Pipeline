# Stores all payloads for use in testing

# STRING INPUT

STRING_INPUT_FULL = {'dataset': 'ALL',
                        'sequence': 'UUUUUUAAGGAAGAUCUGGCCUUCCCACAAGGGAAGGCCAAAGAAUUUCCUU',
                        'score_threshold': '0',
                        'sample_size': '1000',
                        'lambda': '0.35',
                        'window_length': '200',
                        'step_size': '100',
                        'modules': '',
                        'constraints': '',
                        'vernal': '1',
                        'rnamigos': '1'}

STRING_INPUT_BP_ONLY = {'dataset': 'ALL',
                        'sequence': 'UUUUUUAAGGAAGAUCUGGCCUUCCCACAAGGGAAGGCCAAAGAAUUUCCUU',
                        'score_threshold': '0',
                        'sample_size': '1000',
                        'lambda': '0.35',
                        'window_length': '200',
                        'step_size': '100',
                        'modules': '',
                        'constraints': '',
                        'vernal': '0',
                        'rnamigos': '0'}
STRING_INPUT_NO_VERNAL = {'dataset': 'ALL',
                        'sequence': 'UUUUUUAAGGAAGAUCUGGCCUUCCCACAAGGGAAGGCCAAAGAAUUUCCUU',
                        'score_threshold': '0',
                        'sample_size': '1000',
                        'lambda': '0.35',
                        'window_length': '200',
                        'step_size': '100',
                        'modules': '',
                        'constraints': '',
                        'vernal': '0',
                        'rnamigos': '1'}
STRING_INPUT_NO_RNAMIGOS = {'dataset': 'ALL',
                        'sequence': 'UUUUUUAAGGAAGAUCUGGCCUUCCCACAAGGGAAGGCCAAAGAAUUUCCUU',
                        'score_threshold': '0',
                        'sample_size': '1000',
                        'lambda': '0.35',
                        'window_length': '200',
                        'step_size': '100',
                        'modules': '',
                        'constraints': '',
                        'vernal': '1',
                        'rnamigos': '0'}
STRING_INPUT_INCORRECT_DATASET = {'dataset': 'BAD',
                                  'sequence': 'UUUUUUAAGGAAGAUCUGGCCUUCCCACAAGGGAAGGCCAAAGAAUUUCCUU'}

# FILE INPUT

FILE_INPUT_FULL = {'dataset': 'ALL',
                        'score_threshold': '0',
                        'sample_size': '1000',
                        'lambda': '0.35',
                        'window_length': '200',
                        'step_size': '100',
                        'modules': '',
                        'constraints': '',
                        'vernal': '1',
                        'rnamigos': '1'}

FILE_INPUT_BP_ONLY = {'dataset': 'ALL',
                        'score_threshold': '0',
                        'sample_size': '1000',
                        'lambda': '0.35',
                        'window_length': '200',
                        'step_size': '100',
                        'modules': '',
                        'constraints': '',
                        'vernal': '0',
                        'rnamigos': '0'}
FILE_INPUT_NO_VERNAL = {'dataset': 'ALL',
                        'score_threshold': '0',
                        'sample_size': '1000',
                        'lambda': '0.35',
                        'window_length': '200',
                        'step_size': '100',
                        'modules': '',
                        'constraints': '',
                        'vernal': '0',
                        'rnamigos': '1'}
FILE_INPUT_NO_RNAMIGOS = {'dataset': 'ALL',
                        'score_threshold': '0',
                        'sample_size': '1000',
                        'lambda': '0.35',
                        'window_length': '200',
                        'step_size': '100',
                        'modules': '',
                        'constraints': '',
                        'vernal': '1',
                        'rnamigos': '0'}

# GRAPH RETRIEVAL

GRAPH_RETRIEVAL_SUCCESS = {'dataset': 'ALL',
                           'modules': '["36", "48"]'
                           }

# MODULE INFO

MODULE_INFO_RETRIEVAL_VALID_MODULES = "[\"36\", \"48\"]"
MODULE_INFO_RETRIEVAL_ALL_DATASET = "ALL"
