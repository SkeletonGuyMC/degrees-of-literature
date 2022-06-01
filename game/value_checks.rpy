label faintcheck:
    if fatigue >= 100 or stress >= 100:
        jump faint_sequence
    else:
        return

label intcheck:
    if intrequirement = "D":
        if intelligencerank == "D" or intelligencerank == "C" or intelligencerank == "B" or intelligencerank == "A" or intelligencerank == "S":
            $ intcheckpass = 1
            return
        else:
            $ intcheckpass = 0
            return
    elif intrequirement = "C":
        if intelligencerank == "C" or intelligencerank == "B" or intelligencerank == "A" or intelligencerank == "S":
            $ intcheckpass = 1
            return
        else:
            $ intcheckpass = 0
            return
    elif intrequirement = "B":
        if intelligencerank == "B" or intelligencerank == "A" or intelligencerank == "S":
            $ intcheckpass = 1
            return
        else:
            $ intcheckpass = 0
            return
    elif intrequirement = "A":
        if intelligencerank == "A" or intelligencerank == "S":
            $ intcheckpass = 1
            return
        else:
            $ intcheckpass = 0
            return
    elif intrequirement = "S":
        if intelligencerank == "S":
            $ intcheckpass = 1
            return
        else:
            $ intcheckpass = 0
            return

label phycheck:
    if phyrequirement = "D":
        if physiquerank == "D" or physiquerank == "C" or physiquerank == "B" or physiquerank == "A" or physiquerank == "S":
            $ phycheckpass = 1
            return
        else:
            $ phycheckpass = 0
            return
    elif phyrequirement = "C":
        if physiquerank == "C" or physiquerank == "B" or physiquerank == "A" or physiquerank == "S":
            $ phycheckpass = 1
            return
        else:
            $ phycheckpass = 0
            return
    elif phyrequirement = "B":
        if physiquerank == "B" or physiquerank == "A" or physiquerank == "S":
            $ phycheckpass = 1
            return
        else:
            $ phycheckpass = 0
            return
    elif phyrequirement = "A":
        if physiquerank == "A" or physiquerank == "S":
            $ phycheckpass = 1
            return
        else:
            $ phycheckpass = 0
            return
    elif phyrequirement = "S":
        if physiquerank == "S":
            $ phycheckpass = 1
            return
        else:
            $ phycheckpass = 0
            return

label soccheck:
    if socrequirement = "D":
        if socialrank == "D" or socialrank == "C" or socialrank == "B" or socialrank == "A" or socialrank == "S":
            $ soccheckpass = 1
            return
        else:
            $ soccheckpass = 0
            return
    elif socrequirement = "C":
        if socialrank == "C" or socialrank == "B" or socialrank == "A" or socialrank == "S":
            $ soccheckpass = 1
            return
        else:
            $ soccheckpass = 0
            return
    elif socrequirement = "B":
        if socialrank == "B" or socialrank == "A" or socialrank == "S":
            $ soccheckpass = 1
            return
        else:
            $ soccheckpass = 0
            return
    elif socrequirement = "A":
        if socialrank == "A" or socialrank == "S":
            $ soccheckpass = 1
            return
        else:
            $ soccheckpass = 0
            return
    if socrequirement = "S":
        if socialrank == "S":
            $ soccheckpass = 1
            return
        else:
            $ soccheckpass = 0
            return

label skulcheck:
    if skulrequirement = "D":
        if skulduggeryrank == "D" or skulduggeryrank == "C" or skulduggeryrank == "B" or skulduggeryrank == "A" or skulduggeryrank == "S":
            $ skulcheckpass = 1
            return
        else:
            $ skulcheckpass = 0
            return
    elif skulrequirement = "C":
        if skulduggeryrank == "C" or skulduggeryrank == "B" or skulduggeryrank == "A" or skulduggeryrank == "S":
            $ skulcheckpass = 1
            return
        else:
            $ skulcheckpass = 0
            return
    elif skulrequirement = "B":
        if skulduggeryrank == "B" or skulduggeryrank == "A" or skulduggeryrank == "S":
            $ skulcheckpass = 1
            return
        else:
            $ skulcheckpass = 0
            return
    elif skulrequirement = "A":
        if skulduggeryrank == "A" or skulduggeryrank == "S":
            $ skulcheckpass = 1
            return
        else:
            $ skulcheckpass = 0
            return
    elif skulrequirement = "S":
        if skulduggeryrank == "S":
            $ skulcheckpass = 1
            return
        else:
            $ skulcheckpass = 0
            return
