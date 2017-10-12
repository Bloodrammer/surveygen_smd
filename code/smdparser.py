
import logging
import traceback
import warnings

logger = logging.getLogger(__name__)


def parse(filename):
    """Parse the text file with SimpleMarkdown into a list of dictionaries.
    Dictionary parameters: { 'type':
    ['question','image','newline','gap']+temporary types 'answer' and 'closer',
    'text': string,

        [FOR TYPE 'question' ONLY]:
        'answers': list of answers,
        'choice': ['multiple','radio']
    }
    :param filename: filename in string format
    :return: sequence: list of dictionaries

    """
    try:
        logger.info('Trying to open "{}"'.format(filename))
        with open(filename) as f:
            a = f.read()
        logger.info('Successfully opened "{}"'.format(filename))
    except Exception as e:
        logger.error('Exception raised when trying to open "{}": {}'.format(
            filename, e))
        logging.error(traceback.format_exc())
        return
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        logger.info('Trying to process "{}"'.format(filename))

        special_symbols = "[]<>#*\n|\t"
        sequence = []
        current_type = None
        questions = []
        esc = False
        types = {
            '*#': 'question',
            '[': 'image',
            '\n': 'newline',
            '|\t': 'answer',
            '<': 'gap',
            '>]': 'closer'
        }
        choice = {
            '*': 'multiple',
            '#': 'radio'
        }
        logger.info('Parsing...')
        for i in a:
            if i == "\\":
                esc = True
                continue
            if i not in special_symbols:
                if not sequence:
                    sequence.append({'type': None, 'text': ''})
                sequence[-1]['text'] = ''.join([sequence[-1]['text'], i])
            if i in special_symbols:
                if esc:
                    sequence[-1]['text'] = ''.join([sequence[-1]['text'], i])
                    esc = False
                    continue
                current_type = types[[x for x in types.keys() if i in x][0]]
                sequence.append({'type': current_type, 'text': ''})
                if current_type == 'question':
                    sequence[-1]['choice'] = choice[i]
                    questions.append({len(sequence) - 1: []})
                if current_type == 'answer':
                    questions[-1][max(questions[-1].keys())
                                  ].append(len(sequence) - 1)
        for i in reversed(questions):
            sequence[max(i.keys())]['answers'] = [sequence[x]
                                                  ['text'].strip() for x in list(i.values())[0]]

        sequence = [sequence[x] for x in range(len(sequence)) if
                    not (sequence[x]['type'] == 'newline'
                         and sequence[(x + 1) % len(sequence)]['type'] == 'answer') and
                    sequence[x]['type'] not in ['closer', 'answer']]
        for i in sequence:
            i['text'] = i['text'].strip()
        logger.info('Parsing finished successfully!')
        return sequence


if __name__ == '__main__':
    print('You are not supposed to use this module as a standalone file, try using smdpipeline.py instead.')
