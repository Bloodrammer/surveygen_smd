

from PIL import Image, ImageDraw, ImageFont
import logging
import logging.config
import warnings
import traceback
from datetime import datetime
logger = logging.getLogger(__name__)

TNM = './fonts/times-new-roman.ttf'
TNM_bold = './fonts/times-new-roman-bold.ttf'

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
        return sequence


class Survey:
    """This class provides tools for creating surveys in PNG format, and can
    also work with parsed SimpleMarkdown sequences."""
    def __init__(
            self,
            dpi=300,
            inch_size=(8.27, 11.69),
            inch_margin=(1, 0.5),
            font_size=12
    ):
        """Create an empty A4 sheet with 300 dpi resolution by default.

        :param dpi: dots per inch
        :param inch_size: sheet size in inches, tuple (x,y)
        :param inch_margin: offset in inches, tuple (x,y)
        :param font_size: int

        """
        self.dpi = dpi
        self.inch_size = inch_size
        self.inch_margin = inch_margin
        self.font_size = font_size * self.dpi // 72
        self.font = ImageFont.truetype(
            font=TNM, size=self.font_size)
        self.bold_font = ImageFont.truetype(
            font=TNM_bold, size=self.font_size)
        self.x_margin, self.y_margin = int(
            inch_margin[0] * dpi), int(inch_margin[1] * dpi)
        self.survey = Image.new('RGB', tuple(int(x * dpi)
                                             for x in inch_size), color=(255, 255, 255))
        self.draw = ImageDraw.Draw(self.survey)
        self.question_count = 1
        self.current_pos = [self.x_margin, self.y_margin]

        self.reserved_names = {
            'AO_Solar_System': './images/solar.png'
        }

    def _draw_grid(self):
        """Function for debugging.

        Create a grid with (self.font_size,self.font_size) step bounded
        by the margin.

        """
        self.draw.rectangle(
            (1,
             1,
             self.survey.size[0] - 1,
             self.survey.size[1] - 1),
            outline=0)
        grid_font = ImageFont.truetype(
            font=TNM_bold, size=10)
        self.draw.rectangle((self.x_margin, self.y_margin, self.survey.size[0] -
                             self.x_margin, self.survey.size[1] - self.y_margin), outline=0)

        for i in range(self.y_margin + self.font_size,
                       self.survey.size[1] - self.y_margin, self.font_size):
            self.draw.line(
                (self.x_margin +
                 1,
                 i,
                 self.survey.size[0] -
                 self.x_margin -
                 1,
                 i),
                fill=(
                    100,
                    255,
                    255))
            self.draw.text((self.x_margin, i), str(i), font=grid_font, fill=0)

        for i in range(self.x_margin + self.font_size,
                       self.survey.size[0] - self.x_margin, self.font_size):
            self.draw.line(
                (i,
                 self.y_margin +
                 1,
                 i,
                 self.survey.size[1] -
                 self.y_margin -
                 1),
                fill=(
                    100,
                    255,
                    255))

    def paste_image(self, pasted_name, alignment='center', resize=None):
        """Paste the input image onto the survey in the current position.

        :param pasted_name: image path or a reserved name.
        :param alignment: 'left','center','right'
        :param resize: default size if None, resize to (x,y) if tuple(x,y)

        """
        if pasted_name in self.reserved_names.keys():
            pasted = Image.open(self.reserved_names[pasted_name])
        else:
            try:
                pasted = Image.open(pasted_name)
            except Exception as e:
                print(e.message, e.args)
        if resize:
            try:
                pasted = pasted.resize(
                    (resize[0] * pasted.size[0], resize[1] * pasted.size[1]))
            except Exception as e:
                print(e.message, e.args)
        align = {
            'left': self.current_pos,
            'center': (int((self.survey.size[0] - pasted.size[0]) / 2), self.current_pos[1]),
            'right': (self.survey.size[0] - self.current_pos[0] - pasted.size[0], self.current_pos[1])

        }
        start = align[alignment]

        self.survey.paste(pasted,
                          box=(start[0], start[1],
                               start[0] + pasted.size[0], start[1] + pasted.size[1])
                          )
        self.current_pos[1] += pasted.size[1] // self.font_size * \
            self.font_size

    def __paste_image_by_var(self, pasted, alignment='center'):
        """Function for debugging. Paste the input image onto the survey in the
        current position.

        :param pasted: PIL.Image() variable
        :param alignment: 'left','center','right'

        """
        align = {
            'left': self.current_pos,
            'center': (int((self.survey.size[0] - pasted.size[0]) / 2), self.current_pos[1]),
            'right': (self.survey.size[0] - self.current_pos[0] - pasted.size[0], self.current_pos[1])

        }
        start = align[alignment]

        self.survey.paste(pasted,
                          box=(start[0], start[1],
                               start[0] + pasted.size[0], start[1] + pasted.size[1])
                          )
        self.current_pos[1] += pasted.size[1] // self.font_size * \
            self.font_size

    def field_with_gap(self, text):
        """Place the text and 20 underscores onto the survey in the current
        position.

        :param text: string

        """
        self.draw.text(
            self.current_pos,
            text + '_' * 20,
            font=self.bold_font,
            fill=0)
        self.current_pos[0] = (self.survey.size[0] + self.current_pos[0]) / 2 if \
            (self.survey.size[0] + self.current_pos[0]) / 2 < (self.survey.size[0] - self.current_pos[0]) else \
            self.x_margin

    def next_row(self):
        """Emulates '\n' on the survey."""
        self.current_pos = [
            self.x_margin,
            self.current_pos[1] +
            self.font_size]

    def draw_checkbox(self, i):
        """Draw a checkbox with a capital letter within and offsets along
        x-axis by 3*self.font_size.

        :param i: letter number in the alphabet - 1

        """
        self.draw.rectangle(
            [self.current_pos[0] + int(0.06 * self.font_size),
             self.current_pos[1] + int(0.06 * self.font_size),
             self.current_pos[0] + self.font_size - int(0.06 * self.font_size),
             self.current_pos[1] + self.font_size - int(0.06 * self.font_size)],
            outline=0)
        self.draw.text(
            [self.current_pos[0] + int(0.16 * self.font_size),
             self.current_pos[1] - int(0.06 * self.font_size),
             self.current_pos[0] + self.font_size,
             self.current_pos[1] + self.font_size],
            chr(ord('A') + i),
            font=self.font, fill=0)
        self.current_pos[0] += 3 * self.font_size

    def draw_radiobox(self, i):
        """Draw a radiobox with a capital letter within and offsets along
        x-axis by 3*self.font_size.

        :param i: letter number in the alphabet - 1

        """
        self.draw.ellipse(
            [self.current_pos[0],
             self.current_pos[1],
             self.current_pos[0] + self.font_size,
             self.current_pos[1] + self.font_size],
            outline=0)
        self.draw.text(
            [self.current_pos[0] + int(0.16 * self.font_size),
             self.current_pos[1] - int(0.06 * self.font_size),
             self.current_pos[0] + self.font_size,
             self.current_pos[1] + self.font_size],
            chr(ord('A') + i),
            font=self.font, fill=0)
        self.current_pos[0] += 3 * self.font_size

    def question(self,
                 q,
                 answers,
                 multiple='radio',
                 reset_count=False,
                 ):
        """Number and draw the question and the answers on the survey in the
        current position.

        :param q: question text
        :param answers: answers in string format
        :param multiple: 'radio','multiple'
        :param reset_count: Resets self.question_count to 1 if True.

        """
        if reset_count:
            self.question_count = 1
        self.draw.text(
            self.current_pos,
            "{}. {}".format(
                self.question_count,
                q),
            font=self.font,
            fill=0)

        self.question_count += 1
        self.next_row()
        self.next_row()
        for i, ans in enumerate(answers):
            if multiple == 'multiple':
                self.draw_checkbox(i)
            elif multiple == 'radio':
                self.draw_radiobox(i)
            else:
                raise ValueError(
                    '\'choice\' argument in function question() can only equal \'multiple\' and \'radio\'')
            self.draw.text(
                self.current_pos,
                "{}".format(ans),
                font=self.font,
                fill=0)
            self.current_pos[0] += int((self.survey.size[0] -
                                        2 * self.x_margin) / 4)
            if i % 2:
                self.next_row()
        self.next_row()

    def render(self, sequence):
        """Render the parsed SimpleMarkdown sequence onto the empty sheet.

        :param sequence: parsed SimpleMarkdown sequence.

        """
        for i in sequence:
            # print(i['text'],draw.multiline_textsize(i['text'],font=font))
            if i['type'] == 'newline':
                self.next_row()
                self.draw.text(
                    self.current_pos,
                    i['text'],
                    font=self.font,
                    fill=0)
            elif i['type'] == 'question':
                self.question(i['text'], i['answers'], multiple=i['choice'])
            elif i['type'] == 'gap':
                self.field_with_gap(i['text'])
            elif i['type'] == 'image':
                self.paste_image(i['text'])
            else:
                self.draw.text(
                    self.current_pos,
                    i['text'],
                    font=self.font,
                    fill=0)

    def save(self, output_folder='', filename=None):
        """Save the survey in the .PNG format.

        :param output_folder: output folder
        :param filename: filename

        """
        del self.draw
        if not filename:
            name = ''.join([output_folder, "Survey_{}.png".format(
                datetime.strftime(datetime.today(), "%m-%d-%y"))])
        else:
            name = ''.join([output_folder, "/processed_",
                            filename.split('/')[-1].split('.')[-2], '.png'])
        self.survey.save(name, 'PNG')


def survey_pipeline(filename, output_folder=''):
    """SimpleMarkdown rendering pipeline. Parses the input file, renders it on
    an image and saves it in .PNG format.

    :param filename: text file name
    :param output_folder: output folder

    """
    sequence = parse(filename)
    result = Survey()
    result.render(sequence)
    result.save(output_folder, filename)


if __name__ == '__main__':
    filename = str(input("Enter the filename:"))
    survey_pipeline(filename)
