import xlwt


class Style(object):

    def __init__(self, name, height, bold=False):
        style = xlwt.XFStyle()
        font = xlwt.Font()

        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font

