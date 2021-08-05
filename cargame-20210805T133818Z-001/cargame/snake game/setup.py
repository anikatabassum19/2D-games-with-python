import cx_Freeze

executables = [cx_Freeze.Executable('snako.py')]

cx_Freeze.setup(
    name = ('snako'),
    options = {'build_exe':{'packages':['pygame'],'include_files':['apple1.png','snake1.png','tail.png','background.jpg','background2.png','background3.jpg','bak_music.wav','buzzer.wav','icon.png','tail2.png']}},
    description = ('snako.py'),
    executables = executables
                )
