from random import randint
import xlrd


def load_nouns():
    noun = ""
    list_of_nouns = []
    nouns_book = xlrd.open_workbook("nouns.xls")
    sh = nouns_book.sheet_by_index(0)
    for rx in range(sh.nrows):
        noun = sh.cell_value(rx, 0)
        list_of_nouns.append(noun)
    return list_of_nouns


def load_verbs():
    verb = ""
    list_of_verbs = []
    verbs_book = xlrd.open_workbook("verbs.xls")
    sh = verbs_book.sheet_by_index(0)
    for rx in range(sh.nrows):
        noun = sh.cell_value(rx, 0)
        list_of_verbs.append(noun)
    return list_of_verbs


class Components:

    def __init__(self):
        self.det = ['the', 'their', 'a', 'this', 'Kurt\'s', 'our', 'any', 'seven']
        self.aux = ['can', 'will', 'be', 'does', 'could', 'dare', 'may', 'might', 'must', 'should', 'would', 'has']
        self.n = load_nouns()
        self.v = load_verbs()

    def get_det(self):
        return self.det[randint(0, len(self.det) - 1)]

    def get_aux(self):
        return self.aux[randint(0, len(self.aux) - 1)]

    def get_n(self):
        return self.n[randint(0, len(self.n) - 1)]

    def get_v(self):
        return self.v[randint(0, len(self.v) - 1)]
