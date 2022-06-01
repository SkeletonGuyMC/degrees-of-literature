label set_pronoun:
    menu:
        "My pronouns are..."
        "He/Him":
            $ he = "he"
            $ him = "him"
            $ are = "is"
            $ hes = "he's"
            python:
                finishPronouns()

            "Set Pronoun to He/Him."

        "She/Her":
            $ he = "she"
            $ him = "her"
            $ are = "is"
            $ hes = "she's"
            python:
                finishPronouns()

            "Set Pronoun to She/Her."

        "They/Them":
            $ he = "they"
            $ him = "them"
            $ are = "are"
            $ hes = "they're"
            python:
                finishPronouns()

            "Set Pronoun to They/Them."

    $ he_capital = he.capitalize()
    $ him_capital = him.capitalize()
    $ are_capital = are.capitalize()
    $ hes_capital = hes.capitalize()
    return

# The player enters their character's information and is introduced to the plot here.
label mod_passport:

    stop music fadeout 2.0
    scene dark
    with dissolve_scene_full
    mu "Hey, sleepyhead, wake up."
    scene white
    with dissolve_cg
    'I open my eyes after a moment of fighting the urge to just go back to sleep.'
    'The car light practically burns my retinas as I do so, and now I wish I\'d just kept sleeping.'
    'I look away from the light, and notice that it\'s already night time, we must\'ve been driving for the entire day.'
    scene bg car_night
    with dissolve_cg
    mu "You\'re like a sloth, I swear.{w=0.2} Come on."
    $ player = "Me"
    mc "{i}Yawn...{/i}{w=1.0} Alright, I\'m up.{w=0.2} So, are we there yet or did something stupid distract you again?"
    'I stretch my legs, trying to alleviate the discomfort of sitting in the same place for hours on end.'
    mu "Yep!"
    mc "Is that to actually arriving, or to the distraction?"
    mu "We\'re here, of course!{w=0.2} Why, what did you think it was?"
    mc "'Of course'?{w=0.2} Mom, last time you woke me up because a town we passed through had a big rock in the middle of it."
    mu "The rock was cool, shut up.{w=0.2} Anyways, we\'ve actually been here for about 10 minutes."
    mu "You just refused to wake up until now."
    mc "Oh.{w=0.2} Well, you\'re very easily entertained, and moving on, what do I do now?"
    'I step out of the car.'
    scene bg house_night
    with wipeleft_scene
    show mother 1a at t11 zorder 2
    mu "Well, now we need to unpack everything from the car, and I could use your help."
    mc "Alright, what should I take?{w=0.2} I was getting tired of sleeping anyway."
    mu 1b "Alrigh-{nw}"
    mu 1c "..."
    mu "Alright, questionable logic aside, can you grab some of the boxes in the back?"
    mu "I need to make a call, then I\'ll take some as well."
    mc "Got it."
    'I walk around to the back of the car, and pick up some of the smaller boxes.'
    'Despite initially misjudging how heavy these are, I manage to carry them to the door with relative ease.'
    show mother at thide zorder 1
    hide mother
    scene bg hallway
    with wipeleft_scene
    mc "{i}Sigh...{/i}{w=1.0} Alright, where do these go?"
    'I walk down the hallway, looking for somewhere to put these down.'
    scene bg living_room_night
    with wipeleft_scene
    'The room I walk into next is the living room, by the looks of things.'
    'Most of the furniture was moved ahead of time, it\'s just a few other things that aren\'t here yet.'
    'I put the boxes on a table, deciding this is a reasonable place to leave these for now.'
    'As I turn to go back to get more stuff, I hear the front door open.'
    show mother 1a at t11 zorder 2
    "Mom walks into the living room soon after, carrying a rather tall stack of boxes."
    mu "Are you in here?{w=0.2} I can\'t see past these."
    mc "Yeah, right next to you."
    mu "Where did you put the boxes?{w=0.2} Just on that table over there is fine."
    mc "I already put them there, I was going to get more now."
    mu "Oh, good.{w=0.2} Just get as many as you can, and I\'ll take the rest."
    mu "Your room is the first door on the right upstairs, by the way.{w=0.2} You can take your stuff up there when you\'re done."
    mc "Alright."
    show mother at thide zorder 1
    hide mother
    scene dark
    with wipeleft_scene
    'We finish unpacking the car soon enough, and I pick out my stuff from the boxes.'
    'I walk upstairs, and follow my mom\'s directions to my room.{w=0.2} I gently open the door and walk inside.'
    scene bg bedroom_night
    with wipeleft_scene
    'I can\'t see very well, since it\'s so dark, but I don\'t know where the light switch is.'
    'For a few moments my arm flails on the wall aimlessly until I feel a switch.'
    scene bg bedroom
    'I flick the switch, and the light comes on.{w=0.2} Obviously.'
    'At first glance, it\'s not a bad room, it\'s big enough for me and looks nice too.'
    'I sit down on my bed, which is one of the few things that\'s new and hasn\'t been moved from the old house.'
    'It\'s softer than my old one, which I don\'t have any complaints about.'
    'I\'m not left in peace for long, though.{w=0.2} Looks like that\'s one thing that won\'t be changing.'
    show mother 1a at t11 zorder 2
    mu "I forgot something, sorry!{w=0.2} It\'s important."
    mc "Okay, what is it?"
    mu "School form for your new school.{w=0.2} Which, come to think of it, I probably should\'ve given to you earlier."
    mc "Eh, better late than never.{w=0.2} Hand it over and I\'ll fill it out quickly then."
    'She hands me the form and a pencil, and I read over it and answer most of the questions.'
    'They aren\'t particularly difficult questions, and I get through them easily.'
    'It doesn\'t take too long either, and soon enough I\'m left with just a few more questions to fill out.'
    'My name...'
    show screen name_input(message="Please enter your name", ok_action=Function(FinishEnterName))
    '...'
    'I write [player] Takahashi.{w=0.2} Next question.'
    'My gender.'
    call set_pronoun
    'After filling out a couple more questions, the form is done.'
    mc "Alright, done.{w=0.2} Go do, uh, whatever you need to do with it."
    mu "Thanks.{w=0.2} Now you should get some sleep, it\'s late."
    mc "I already got enough of that.{w=0.2} I\'d say 12 hours, at the very least today."
    mu "Oh, right.{w=0.2} Still, you\'ll need to get into a routine."
    mc "It can wait, at least for today."
    mu "Alright, I\'m going to sleep though.{w=0.2} Don\'t stay up too late."
    mc "Okay."

    jump school_tutorial


    call school_tutorial
