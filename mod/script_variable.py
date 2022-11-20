def lang_code(compiler):
    lang = [['text/x-pascal', '3'],
            ['c', '4'],
            ['cpp', '10'],
            ['csharp', '16'],
            ['clojure', '18'],
            ['text/x-crystal', '19'],
            ['text/x-elixir', '20'],
            ['text/x-erlang', '21'],
            ['go', '22'],
            ['text/x-haskell', '23'],
            ['plaintext', '44'],
            ['java', '26'],
            ['javascript', '29'],
            ['text/x-ocaml', '31'],
            ['text/x-octave', '32'],
            ['pascal', '33'],
            ['python', '34'],
            ['ruby', '38'],
            ['rust', '42']]
    for elem in lang:
        if compiler.lower() in elem:
            return elem[1]


def c_id(language):
    if language == 'C':
        return 'IARE_C'
    elif language == 'C++':
        return 'IARE_CPP'
    elif language == 'P':
        return 'IARE_PY'
    elif language == 'Java':
        return 'IARE_JAVA'
    else:
        return ""


def c_id(language):
    if language == 'C':
        return 'IARE_C'
    elif language == 'C++':
        return 'IARE_CPP'
    elif language == 'P':
        return 'IARE_PY'
    elif language == 'Java':
        return 'IARE_JAVA'
    else:
        return ""
