label faint_sequence:

    stop music fadeout 2.0
    scene dark
    with dissolve_cg
    'Everything fades to black...'
    'You\'ve pushed yourself too far.'
    if infight == 1:
        jump faintevent0
    else:
        $ faintevent = renpy.random.randint(1,5)
        if faintevent == 1:
            jump faintevent1
        elif faintevent == 2:
            jump faintevent2
        elif faintevent == 3:
            jump faintevent3
        elif faintevent == 4:
            jump faintevent4
        elif faintevent == 5:
            jump faintevent5

label faintevent1:
    jump endgame

label faintevent2:
    jump endgame

label faintevent3:
    jump endgame

label faintevent4:
    jump endgame

label faintevent5:
    jump endgame

label faintevent0:
    jump endgame
