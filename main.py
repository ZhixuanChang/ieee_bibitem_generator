import re
import codecs

class Article:
    """a class of article, which contains basic properties of an article.
    """
    def __init__(self, author, title, journal, type, vol, issue, year, pages=None, startPage=None):
        """construction function
        """
        self.author = author
        self.title = title
        self.journal = journal
        self.type = type
        self.vol = vol
        self.issue = issue
        self.year = year
        self.pages = pages
        self.startPage = startPage
    
    def set_author(self, author):
        self.author = author

    def set_title(self, title):
        self.title = title

    def set_journal(self, journal):
        self.journal = journal
    
    def set_type(self, type):
        self.type = type


def main():
    """main function
    """
    bib_file = 'reference.bib'
    article_list = []
    with codecs.open(bib_file, 'r', 'utf-8') as fip:
        lines = fip.readlines()
        # line = fip.readline()
        # while line != "":
        #     article = {
        #         'label': 'UNDEFINED',
        #         'author': 'UNDEFINED',
        #         'title': 'UNDEFINED',
        #         'journal': 'UNDEFINED',
        #         'type': 'UNDEFINED',
        #         'vol': -1,
        #         'issue': -1,
        #         'year': -1,
        #         'pages': 'UNDEFINED',
        #     }
        #     if '@article' in line:
        #         label = line[line.find('{') + 1 : ]
        #         label = label[ : label.find(',')]
        #         article['label'] = label
        #     line = fip.readline()
        #     while line != '}\r\n':
        #         if 'author =' in line:
        #             author = line[line.find('{') + 1 : ]
        #             author = author[ : author.find('}')]
        #             article['author'] = author
        #         elif 'title =' in line:
        #             title = line[line.find('{') + 1 : ]
        #             title = title[ : title.find('}')]
        #             article['title'] = title
        #         elif 'journal =' in line:
        #             journal = line[line.find('{') + 1 : ]
        #             journal = journal[ : journal.find('}')]
        #             article['journal'] = journal
        #         elif 'type =' in line:
        #             article_type = line[line.find('{') + 1 : ]
        #             article_type = article_type[ : article_type.find('}')]
        #             article['type'] = journal
        #         elif 'volume =' in line:
        #             vol = line[line.find('{') + 1 : ]
        #             vol = vol[ : vol.find('}')]
        #             article['vol'] = vol
        #         elif 'number =' in line:
        #             issue = line[line.find('{') + 1 : ]
        #             issue = issue[ : issue.find('}')]
        #             article['issue'] = issue
        #         elif 'year =' in line:
        #             year = line[line.find('{') + 1 : ]
        #             year = year[ : year.find('}')]
        #             article['year'] = year
        #         elif 'pages =' in line:
        #             pages = line[line.find('{') + 1 : ]
        #             pages = pages[ : pages.find('}')]
        #             article['pages'] = pages
        #         else:
        #             pass
        #         line = fip.readline()
        #     article_list.append(article)
    print(len(article_list))


if __name__ == '__main__':
    main()
