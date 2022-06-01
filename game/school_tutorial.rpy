
# this screen shows the ingame UI and updates your stats.
screen textbutton_screen():
    vbox:
        textbutton "Stats" action [Show(screen="stats_screen")]
        textbutton "Social" action [Show(screen="social_screen")]
        textbutton "Journal" action [Show(screen="journal_screen")]
        textbutton "Music" action [Show(screen="music_screen")]
        if minute < 10:
            text "[hour]:0[minute]" xpos 1150 ypos -145
        else:
            text "[hour]:[minute]" xpos 1150 ypos -145
        text "[day]" xpos 1150 ypos -150
        text "[date][th] of" xpos 1150 ypos -155
        text "[month]" xpos 1150 ypos -160
        if date == 1 or date == 21:
            $ th = "st"
        elif date == 2 or date == 22:
            $ th = "nd"
        elif date == 3 or date == 23:
            $ th = "rd"
        else:
            $ th = "th"
        if minute >= 60:
            $ minute -= 60
            $ hour += 1
        if hour >= 24:
            $ date += 1
            $ daynumber += 1
            $ hour -= 24
            $ daycount += 1
        if daynumber >= 8:
            $ daynumber -= 7
            $ weekcount += 1
        $ functioningdate = date
        if date >= 28:
            $ monthnumber += 1
            $ monthcount += 1
        if daynumber == 1:
            $ day = "Sunday"
        elif daynumber == 2:
            $ day = "Monday"
        elif daynumber == 3:
            $ day = "Tuesday"
        elif daynumber == 4:
            $ day = "Wednesday"
        elif daynumber == 5:
            $ day = "Thursday"
        elif daynumber == 6:
            $ day = "Friday"
        elif daynumber == 7:
            $ day = "Saturday"
        if monthnumber == 1:
            $ month = "January"
        elif monthnumber == 2:
            $ month = "February"
        elif monthnumber == 3:
            $ month = "March"
        elif monthnumber == 4:
            $ month = "April"
        elif monthnumber == 5:
            $ month = "May"
        elif monthnumber == 6:
            $ month = "June"
        elif monthnumber == 7:
            $ month = "July"
        elif monthnumber == 8:
            $ month = "August"
        elif monthnumber == 9:
            $ month = "September"
        elif monthnumber == 10:
            $ month = "October"
        elif monthnumber == 11:
            $ month = "November"
        elif monthnumber == 12:
            $ month = "December"
        if monthnumber >= 13:
            $ monthnumber = 1
            $ yearcount += 1
        if minute <= -1:
            $ minute = 0
        if hour <= -1:
            $ hour = 0
        if fatigue >= 101:
            $ fatigue = 100
        if comfort >= 101:
            $ comfort = 100
        if health >= 101:
            $ health = 100
        if stress >= 100:
            $ stress = 100
        if fatigue <= -1:
            $ fatigue = 0
        if comfort <= -1:
            $ comfort = 0
        if health <= -1:
            $ health = 0
        if stress <= -1:
            $ stress = 0
        if s_love >= 101:
            $ s_love = 100
        if m_love >= 101:
            $ m_love = 100
        if n_love >= 101:
            $ n_love = 100
        if y_love >= 100:
            $ y_love = 100
        if s_love <= -1:
            $ s_love = 0
        if m_love <= -1:
            $ m_love = 0
        if n_love <= -1:
            $ n_love = 0
        if y_love <= -1:
            $ y_love = 0
        if l_love <= -1:
            $ l_love = 0
        if l_love >= 101:
            $ l_love = 100
        if l_addiction <= -1:
            $ l_addiction = 0
        if l_addiction >= 101:
            $ l_addiction = 100
        if l_jealousy <= -1:
            $ l_jealousy = 0
        if l_jealousy >= 101:
            $ l_jealousy = 100
        if s_happiness >= 101:
            $ s_happiness = 100
        if m_awareness >= 101:
            $ m_awareness = 100
        if n_trust >= 101:
            $ n_trust = 100
        if y_confidence >= 100:
            $ y_confidence = 100
        if s_happiness <= -1:
            $ s_happiness = 0
        if m_awareness <= -1:
            $ m_awareness = 0
        if n_trust <= -1:
            $ n_trust = 0
        if y_confidence <= -1:
            $ y_confidence = 0
        if s_jealousy >= 101:
            $ s_jealousy = 100
        if m_jealousy >= 101:
            $ m_jealousy = 100
        if n_jealousy >= 101:
            $ n_jealousy = 100
        if y_jealousy >= 100:
            $ y_jealousy = 100
        if s_jealousy <= -1:
            $ s_jealousy = 0
        if m_jealousy <= -1:
            $ m_jealousy = 0
        if n_jealousy <= -1:
            $ n_jealousy = 0
        if y_jealousy <= -1:
            $ y_jealousy = 0
        if physique >= 100:
            if not physiquerank == "S":
                $ physique -= 100
                if physiquerank == "F":
                    $ physiquerank = "D"
                elif physiquerank == "D":
                    $ physiquerank = "C"
                elif physiquerank == "C":
                    $ physiquerank = "B"
                elif physiquerank == "B":
                    $ physiquerank = "A"
                elif physiquerank == "A":
                    $ physiquerank = "S"
            else:
                $ physique = 100

        if intelligence >= 100:
            if not intelligencerank == "S":
                $ intelligence -= 100
                if intelligencerank == "F":
                    $ intelligencerank = "D"
                elif intelligencerank == "D":
                    $ intelligencerank = "C"
                elif intelligencerank == "C":
                    $ intelligencerank = "B"
                elif intelligencerank == "B":
                    $ intelligencerank = "A"
                elif intelligencerank == "A":
                    $ intelligencerank = "S"
            else:
                $ intelligence = 100

        if social >= 100:
            if not socialrank == "S":
                $ social -= 100
                if socialrank == "F":
                    $ socialrank = "D"
                elif socialrank == "D":
                    $ socialrank = "C"
                elif socialrank == "C":
                    $ socialrank = "B"
                elif socialrank == "B":
                    $ socialrank = "A"
                elif socialrank == "A":
                    $ socialrank = "S"
            else:
                $ social = 100

        if skulduggery >= 100:
            if not skulduggeryrank == "S":
                $ skulduggery -= 100
                if skulduggeryrank == "F":
                    $ skulduggeryrank = "D"
                elif skulduggeryrank == "D":
                    $ skulduggeryrank = "C"
                elif skulduggeryrank == "C":
                    $ skulduggeryrank = "B"
                elif skulduggeryrank == "B":
                    $ skulduggeryrank = "A"
                elif skulduggeryrank == "A":
                    $ skulduggeryrank = "S"
            else:
                $ skulduggery = 100

        if hour >= 9 and hour <= 14 and not day == "Saturday" and not day == "Sunday" and school_break == "False":
            $ schoolinsession = 1
        else:
            $ schoolinsession = 0


label school_tutorial:




    #adds important mechanics to the game.
    window hide
    $ sayori_dismissed = False
    $ natsuki_dismissed = False
    $ monika_dismissed = False
    $ yuri_dismissed = False
    $ naoki_dismissed = False
    $ lemon_dismissed = False
    $ physique = 0
    $ intelligence = 0
    $ social = 0
    $ skulduggery = 0
    $ combat = 0
    $ running = 0
    $ learning = 0
    $ gaming = 0
    $ publicspeaking = 0
    $ teamwork = 0
    $ theft = 0
    $ charisma = 0
    $ physiquerank = 'C'
    $ intelligencerank = 'C'
    $ socialrank = 'C'
    $ skulduggeryrank = 'C'
    $ health = 100
    $ fatigue = 0
    $ stress = 0
    $ comfort = 100
    $ mood = "Happy"
    $ monika_met = "False"
    $ sayori_met = "False"
    $ natsuki_met = "False"
    $ yuri_met = "False"
    $ trevor_met = "False"
    $ m_love = 0
    $ s_love = 0
    $ n_love = 0
    $ y_love = 0
    $ t_love = 0
    $ l_love = 0
    $ m_awareness = 25
    $ s_happiness = 50
    $ n_trust = 0
    $ y_confidence = 0
    $ t_suspicion = 0
    $ l_addiction = 15
    $ m_jealousy = 0
    $ s_jealousy = 0
    $ n_jealousy = 0
    $ y_jealousy = 0
    $ t_jealousy = 0
    $ l_jealousy = 0
    $ s_depression_known = "False"
    $ m_awareness_known = "False"
    $ n_abuse_known = "False"
    $ y_anxiety_known = "False"
    $ t_protective_known = "False"
    $ l_energy_known = "False"
    $ in_literature_club = "False"
    $ in_track_team = "False"
    $ in_debate_club = "False"
    $ japanesegrade = "D"
    $ mathsgrade = "D"
    $ historygrade = "D"
    $ sciencegrade = "D"
    $ musicgrade = "None"
    $ sportgrade = "None"
    $ programminggrade = "None"
    # $ englishgrade = "None"
    $ musictaken = "False"
    $ sporttaken = "False"
    $ programmingtaken = "False"
    # $ englishtaken = "False"
    $ day = "Tuesday"
    $ date = 11
    $ month = "April"
    $ school_break = "False"
    $ money = 0
    $ minute = 30
    $ hour = 7
    $ daynumber = 3
    $ monthnumber = 4
    # $ functioningdate = 11
    $ crimelevel = 0
    $ questing = "True"
    $ daycount = 1
    $ weekcount = 0
    $ monthcount = 0
    $ yearcount = 0
    $ th = "th"
    $ sayori_li = 0
    $ yuri_li = 0
    $ monika_li = 0
    $ naoki_li = 0
    $ natsuki_li = 0
    $ lemon_li = 0

    scene dark
    with dissolve_scene_full
    'A few days later...'
    scene bg bedroom
    with dissolve_scene
    window show
    show screen textbutton_screen
    play music "mod_assets/alarm.mp3"
    '{i}Beep! Beep! Beep!{/i}'
    'I am awoken by my alarm, which I\'d all but forgotten I\'d set yesterday.'
    '... And sometimes wish I didn\'t set at all, because Jesus Christ is it annoying.'
    'First day of the new school year, and first day at a new school.'
    'It\'s nothing special, and I\'ve been through it plenty of times but it still manages to make me a little anxious.'
    stop music
    'I hit the dismiss button on my alarm with an excessive amount of force, and get out of bed.'
    'I open my closet and take my school uniform, putting it on.'
    'I let out a yawn, now regretting staying up so late last night.{w=0.2} Can\'t change that now, though.'
    'I start to make my way downstairs, to the kitchen to get something to eat.'
    scene bg kitchen
    with wipeleft_scene
    show mother 1a at t11 zorder 2
    'When I walk into the kitchen, I\'m greeted by mom.{w=0.2} It smells like bacon in here, too.'
    mu 1b "Oh, look who decided to finally wake up."
    show mother 1a at t11 zorder 2
    mc "'Finally'?{w=0.2} This is the time I set my alarm for."
    mu 1b "Well it doesn\'t leave you with much time in the morning, does it?{w=0.2} Unless you catch the bus, I suppose."
    show mother 1a at t11 zorder 2
    mc "What do you mean?{w=0.2} The school isn\'t that far away if I remember right, and this is pretty early."
    mu 1c "It\'ll still take a little while to get to school, and to do everything in the morning.{w=0.2} You\'ll have to leave by around 8."
    mc "I can live with that.{w=0.2} Now, you\'re cooking bacon and eggs, I can tell.{w=0.2} Did you make any for me?"
    mu 1d "No."
    mu 1b "...{w=1.0} I\'m joking, I\'ll get you some in a second."

    $ minute = 25
    $ questing = "False"

    jump fukuda_menu
