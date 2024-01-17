import re

class Bible(object):
    '''
    Takes record strings and replaces abbreviated bible references with hyperlinked bible references
    '''

    # USCCB URL constant
    USCCB_BIBLE_URL = 'https://bible.usccb.org/bible/{}/{}'

    BIBLE_BOOKS = {
        'genesis': {
            'chapters': 50,
            'abbreviations': ['Gen', 'Ge', 'Gn']
        },
        'exodus': {
            'chapters': 40,
            'abbreviations': ['Exod', 'Exo', 'Ex']
        },
        'leviticus': {
            'chapters': 27,
            'abbreviations': ['Lev', 'Le', 'Lv']
        },
        'numbers': {
            'chapters': 36,
            'abbreviations': ['Num', 'Nu', 'Nm', 'Nb']
        },
        'deuteronomy': {
            'chapters': 34,
            'abbreviations': ['Deut', 'De', 'Dt']
        },
        'joshua': {
            'chapters': 24,
            'abbreviations': ['Josh', 'Jos', 'Jsh']
        },
        'judges': {
            'chapters': 21,
            'abbreviations': ['Judg', 'Jdg', 'Jg', 'Jdgs']
        },
        'ruth': {
            'chapters': 4,
            'abbreviations': ['Rth', 'Ru']
        },
        '1samuel': {
            'chapters': 31,
            'abbreviations': ['1 Sam', '1 Sa', '1S', 'I Sa', '1 Sm', '1Sa', '1Sam', '1st Sam', '1st Samuel', 'First Sam', 'First Samuel']
        },
        '2samuel': {
            'chapters': 24,
            'abbreviations': ['2 Sam', '2 Sa', '2S', 'II Sa', '2 Sm', '2Sa', 'II Sam', 'IISam', '2 Sam', '2Sam', '2nd Sam', '2nd Samuel', 'Second Sam', 'Second Samuel']
        },
        '1kings': {
            'chapters': 22,
            'abbreviations': ['1 Kgs', '1 Ki', '1K', 'I Kgs', '1Kgs', 'I Ki', '1Ki', '1Kin', '1st Kgs', '1st Kings', 'First Kgs', 'First Kings']
        },
        '2kings': {
            'chapters': 25,
            'abbreviations': ['2 Kgs', '2 Ki', '2K', 'II Kgs', '2Kgs', 'II Ki', '2Ki', '2Kin', '2nd Kgs', '2nd Kings', 'Second Kgs', 'Second Kings']
        },
        '1chronicles': {
            'chapters': 29,
            'abbreviations': ['1 Chron', '1 Ch', 'I Ch', '1Ch', '1 Chr', 'I Chr', '1Chr', 'I Chron', '1Chron', '1st Chron', '1st Chronicles', 'First Chron', 'First Chronicles']
        },
        '2chronicles': {
            'chapters': 36,
            'abbreviations': ['2 Chron', '2 Ch', 'II Ch', '2Ch', 'II Chr', '2Chr', 'II Chron', '2Chron', '2nd Chron', '2nd Chronicles', 'Second Chron', 'Second Chronicles']
        },
        'ezra': {
            'chapters': 10,
            'abbreviations': ['Ezr', 'Ez']
        },
        'nehemiah': {
            'chapters': 13,
            'abbreviations': ['Neh', 'Ne']
        },
        'tobit': {
            'chapters': 14,
            'abbreviations': ['Tobit', 'Tob', 'Tb']
        },
        'judith': {
            'chapters': 16,
            'abbreviations': ['Jdth', 'Jdt', 'Jth']
        },
        'esther': {
            'chapters': 10,
            'abbreviations': ['Esth', 'Es']
        },
        '1maccabees': {
            'chapters': 16,
            'abbreviations': ['1 Macc', '1 Mac', '1M', 'I Ma', '1Ma', 'I Mac', '1Mac', 'I Macc', '1Macc', 'I Maccabees', '1Maccabees', '1st Maccabees', 'First Maccabees']
        },
        '2maccabees': {
            'chapters': 15,
            'abbreviations': ['2 Macc', '2 Mac', '2M', 'II Ma', '2Ma', 'II Mac', '2Mac', 'II Macc', '2Macc', 'II Maccabees', '2Maccabees', '2nd Maccabees', 'Second Maccabees']
        },
        'job': {
            'chapters': 42,
            'abbreviations': ['Jb']
        },
        'psalms': {
            'chapters': 150,
            'abbreviations': ['Psalm', 'Pslm', 'Ps', 'Psa', 'Psm', 'Pss']
        },
        'proverbs': {
            'chapters': 31,
            'abbreviations': ['Prov', 'Pro', 'Pr', 'Prv']
        },
        'ecclesiastes': {
            'chapters': 12,
            'abbreviations': ['Eccles', 'Eccle', 'Ecc', 'Ec', 'Qoh']
        },
        'songofsongs': {
            'chapters': 8,
            'abbreviations': ['Song of Songs', 'Song', 'So', 'SOS', 'Canticle of Canticles', 'Canticles', 'Cant']
        },
        'wisdom': {
            'chapters': 19,
            'abbreviations': ['Wisd of Sol', 'Wis', 'Ws', 'Wisdom']
        },
        'sirach': {
            'chapters': 51,
            'abbreviations': ['Sirach', 'Sir', 'Ecclesiasticus', 'Ecclus']
        },
        'isaiah': {
            'chapters': 66,
            'abbreviations': ['Isa', 'Is']
        },
        'jeremiah': {
            'chapters': 52,
            'abbreviations': ['Jer', 'Je', 'Jr']
        },
        'lamentations': {
            'chapters': 5,
            'abbreviations': ['Lam', 'La']
        },
        'baruch': {
            'chapters': 6,
            'abbreviations': ['Baruch', 'Bar']
        },
        'ezekiel': {
            'chapters': 48,
            'abbreviations': ['Ezek', 'Eze', 'Ezk']
        },
        'daniel': {
            'chapters': 14,
            'abbreviations': ['Dan', 'Da', 'Dn']
        },
        'hosea': {
            'chapters': 14,
            'abbreviations': ['Hos', 'Ho']
        },
        'joel': {
            'chapters': 4,
            'abbreviations': ['Joe', 'Jl']
        },
        'amos': {
            'chapters': 9,
            'abbreviations': ['Am']
        },
        'obadiah': {
            'chapters': 1,
            'abbreviations': ['Obad', 'Ob']
        },
        'jonah': {
            'chapters': 4,
            'abbreviations': ['Jnh', 'Jon']
        },
        'micah': {
            'chapters': 7,
            'abbreviations': ['Micah', 'Mic', 'Mc']
        },
        'nahum': {
            'chapters': 3,
            'abbreviations': ['Nah', 'Na']
        },
        'habakkuk': {
            'chapters': 3,
            'abbreviations': ['Hab', 'Hb']
        },
        'zephaniah': {
            'chapters': 3,
            'abbreviations': ['Zeph', 'Zep', 'Zp']
        },
        'haggai': {
            'chapters': 2,
            'abbreviations': ['Haggai', 'Hag', 'Hg']
        },
        'zechariah': {
            'chapters': 14,
            'abbreviations': ['Zech', 'Zec', 'Zc']
        },
        'malachi': {
            'chapters': 3,
            'abbreviations': ['Mal', 'Ml']
        },
        'matthew': {
            'chapters': 28,
            'abbreviations': ['Matt', 'Mt']
        },
        'mark': {
            'chapters': 16,
            'abbreviations': ['Mrk', 'Mar', 'Mk', 'Mr']
        },
        'luke': {
            'chapters': 24,
            'abbreviations': ['Luk', 'Lk']
        },
        'john': {
            'chapters': 21,
            'abbreviations': ['John', 'Joh', 'Jhn', 'Jn']
        },
        'acts': {
            'chapters': 28,
            'abbreviations': ['Act', 'Ac']
        },
        'romans': {
            'chapters': 16,
            'abbreviations': ['Rom', 'Ro', 'Rm']
        },
        '1corinthians': {
            'chapters': 16,
            'abbreviations': ['1 Cor', '1 Co', 'I Co', '1Co', 'I Cor', '1Cor', 'I Corinthians', '1Corinthians', '1st Cor', '1st Corinthians', 'First Cor', 'First Corinthians']
        },
        '2corinthians': {
            'chapters': 13,
            'abbreviations': ['2 Cor', '2 Co', 'II Co', '2Co', 'II Cor', '2Cor', 'II Corinthians', '2Corinthians', '2nd Corinthians', 'Second Corinthians']
        },
        'galatians': {
            'chapters': 6,
            'abbreviations': ['Gal', 'Ga']
        },
        'ephesians': {
            'chapters': 6,
            'abbreviations': ['Ephes', 'Eph']
        },
        'philippians': {
            'chapters': 4,
            'abbreviations': ['Phil', 'Php', 'Pp']
        },
        'colossians': {
            'chapters': 4,
            'abbreviations': ['Col', 'Co']
        },
        '1thessalonians': {
            'chapters': 5,
            'abbreviations': ['1 Thess', '1 Th', 'I Th', '1Th', 'I Thes', '1Thes', 'I Thess', '1Thess', 'I Thessalonians', '1Thessalonians', '1st Thess', '1st Thessalonians', 'First Thess', 'First Thessalonians']
        },
        '2thessalonians': {
            'chapters': 3,
            'abbreviations': ['2 Thess', '2 Th', 'II Th', '2Th', 'II Thes', '2Thes', 'II Thess', '2Thess', 'II Thessalonians', '2Thessalonians', '2nd Thess', '2nd Thessalonians', 'Second Thess', 'Second Thessalonians']
        },
        '1timothy': {
            'chapters': 6,
            'abbreviations': ['1 Tim', '1 Ti', 'I Ti', '1Ti', 'I Tim', '1Tim', 'I Timothy', '1Timothy', '1st Tim', '1st Timothy', 'First Tim', 'First Timothy']
        },
        '2timothy': {
            'chapters': 4,
            'abbreviations': ['2 Tim', '2 Ti', 'II Ti', '2Ti', 'II Tim', '2Tim', 'II Timothy', '2Timothy', '2nd Tim', '2nd Timothy', 'Second Tim', 'Second Timothy']
        },
        'titus': {
            'chapters': 3,
            'abbreviations': ['Titus', 'Tit', 'Ti']
        },
        'philemon': {
            'chapters': 1,
            'abbreviations': ['Philem', 'Phm', 'Pm']
        },
        'hebrews': {
            'chapters': 13,
            'abbreviations': ['Hebrews', 'Heb']
        },
        'james': {
            'chapters': 5,
            'abbreviations': ['James', 'Jas', 'Jm']
        },
        '1peter': {
            'chapters': 5,
            'abbreviations': ['1 Pet', '1 Pe', 'I Pe', '1Pe', 'I Pet', '1Pet', 'I Pt', '1 Pt', '1Pt', '1 P', '1P', 'I Peter', '1Peter', '1st Peter', 'First Peter']
        },
        '2peter': {
            'chapters': 3,
            'abbreviations': ['2 Pet', '2 Pe', 'II Pe', '2Pe', 'II Pet', '2Pet', 'II Pt', '2 Pt', '2Pt', '2 P', '2P', 'II Peter', '2Peter', '2nd Peter', 'Second Peter']
        },
        '1john': {
            'chapters': 5,
            'abbreviations': ['1 John', '1 Jn', 'I Jn', '1Jn', 'I Jo', '1Jo', 'I Joh', '1Joh', 'I Jhn', '1 Jhn', '1Jhn', '1 J', '1J', 'I John', '1John', '1st John', 'First John']
        },
        '2john': {
            'chapters': 1,
            'abbreviations': ['2 John', '2 Jn', 'II Jn', '2Jn', 'II Jo', '2Jo', 'II Joh', '2Joh', 'II Jhn', '2 Jhn', '2Jhn', '2 J', '2J', 'II John', '2John', '2nd John', 'Second John']
        },
        '3john': {
            'chapters': 1,
            'abbreviations': ['3 John', '3 Jn', 'III Jn', '3Jn', 'III Jo', '3Jo', 'III Joh', '3Joh', 'III Jhn', '3 Jhn', '3Jhn', '3 J', '3J', 'III John', '3John', '3rd John', 'Third John']
        },
        'jude': {
            'chapters': 1,
            'abbreviations': ['Jude', 'Jud', 'Jd']
        },
        'revelation': {
            'chapters': 22,
            'abbreviations': ['Rev', 'Re', 'The Revelation']
        },
    }

    def __init__(self):
        self.matching_list, self.response_list = self._generate_lists()

    def _generate_lists(self):
        """Generates a parallel matching list and response list for linkification"""

        matching_list = []
        response_list = []
        for book, book_obj  in self.BIBLE_BOOKS.items():
            for chapter in range(book_obj['chapters'],0,-1):
                abbreviations = [string.lower() for string in book_obj['abbreviations']]
                abbreviations_mod1 = [string + "." for string in abbreviations]
                abbreviations.extend(abbreviations_mod1)
                abbreviations.append(book)
                for abbreviation in abbreviations:
                    response_string='<a href={}>response_string</a>'.format(self.USCCB_BIBLE_URL.format(book,chapter),book,str(chapter))
                    response_list.append(response_string)
                    matching_string = '{} {}'.format(abbreviation, str(chapter))
                    matching_list.append(matching_string)
        return matching_list, response_list

    def linkify(self, record_string):
        """Replaces substrings in a record string based on matching and response lists."""

        for i, match in enumerate(self.matching_list):
            if match in record_string.lower():
                initial_response_string = self.response_list[i]
                final_response_string = initial_response_string.replace('>response_string<','>{}<'.format(match.capitalize()))
                record_string = re.sub(match, final_response_string, record_string, flags=re.IGNORECASE)
        record_string = record_string.replace('***', ' ')
        return record_string
