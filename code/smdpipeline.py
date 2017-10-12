import smdparser
import surveygen
import logging

logger = logging.getLogger(__name__)


def survey_pipeline(filename, output_folder=''):
    """SimpleMarkdown rendering pipeline. Parses the input file, renders it on
    an image and saves it in .PNG format.

    :param filename: text file name
    :param output_folder: output folder

    """
    logging.info(''.join(["=====", filename.split('/')[-1], '=====']))
    sequence = smdparser.parse(filename)
    result = surveygen.Survey()
    result.render(sequence)
    result.save(output_folder, filename)
    logging.info('Saved successfully!')


if __name__ == '__main__':
    filename = str(input("Enter the filename:"))
    survey_pipeline(filename)
