class Question:

    def __init__(self, text, options, correct_option):

        self.text = text
        self.options = options
        self.correct_option = correct_option

questions = [
        Question("Who used to live in the same house as Nic does?",
                 ['Mayor','Hangman','Helmut Kohl'],'Hangman'),
        Question('In Freiburg there are Bächle - what was their purpose?',
                 ['Firefighting', 'Children to play', 'Water for the church'],
                 'Firefighting'),
        Question("""After which scientist is the institute Nic is working
        at named?""",
                 ['Ernst Mach', 'Heinrich Hertz','August Wöhler'], 'Ernst Mach'),
        Question("""What was the profession of a well known french man
        after which also a district of Freiburg is named?""",
        ['General','Advisor to Napoleon','Fortress constructor'],'Fortress constructor'),
        Question("""Which geometric shape is commonly associated with
        the aforementioned scientist?""",['Cup','Circle','Cone'],'Cone')
        ]
