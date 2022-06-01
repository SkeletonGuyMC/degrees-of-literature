label fukuda_menu:
    hide screen textbutton_screen
    show screen textbutton_screen
    $ location = "Fukuda"
    if hour >= 6 and hour <= 19:
        scene bg residential_day
        with wipeleft_scene
        'Ah, home sweet home.'
    else:
        scene bg residential_night
        with wipeleft_scene
        'The street is empty, the silence only broken occasionally by passing cars.'
    label fukuda_options:
    menu:
        "I\'m on Fukuda Street, the street I live on."

        "Go Home":
            $ minute += 2
            jump home_menu

        "Knock On A Door":
            'placeholder'

        "Visit Sayori" if sayori_met == "True":
            'placeholder'

        "Visit Naoki" if trevor_met == "True":
            'placeholder'

        "More...":
            jump fukuda_menu2

label fukuda_menu2:
    menu:
        "Wait For A Bus ($1)":
            $ minute += 2
            jump bus_menu

        "Go Somewhere...":
            'placeholder'

        "Loation Description":
            jump fukuda_menu

        "Less...":
            jump fukuda_options

label home_menu:
    if hour >= 6 and hour <= 19:
        scene bg house
        with wipeleft_scene
    else:
        scene bg house_night
        with wipeleft_scene
    if hour >= 9 and hour <= 14 and not day == "Saturday" and not day == "Sunday" and school_break == "False":
        if skulduggeryrank == "B" or skulduggeryrank == "A" or skulduggeryrank == "S":
            jump sneakinhome
        else:
            $ sneakinhomesuccess = renpy.random.randint(0,4)
            if sneakinhomesuccess == 1:
                jump sneakinhomecaught
            else:
                jump sneakinhome

label sneakinhomecaught:
    'In my attempt to get inside and skip school, I am caught by my mom.'
    show mother 1m at t11 zorder 2
    mu "[player]? Why aren\'t you at school?!"
    mc 'Well, I-{nw}'
    mu 1r 'No excuses, you can\'t skip school!'
    show mother at thide zorder 1
    hide mother
    'Looks like there\'s no getting out of this one...'
    $ minute += 5
    $ fatigue += 1
    call faintcheck
    jump fukuda_menu

label sneakinhome:
    'I manage to get inside without being seen by mom.'
    'I hurry to my room.'
    $ fatigue += 1
    call faintcheck
    jump room_menu

label room_menu:
    scene bg bedroom
    with wipeleft_scene
    menu:
        "I am in my room. Not much else to say about it."

        "Sleep":
            scene dark
            with dissolve_scene
            "I lie down, and before long drift off to sleep..."
            $ hour += 8
            if hour >= 7 and hour <= 12 and not day == "Saturday" and not day == "Sunday" and school_break == "False":
                $ hour = 6
                $ minute = 30
                play music "mod_assets/alarm.mp3"
                $ fatigue -= 60
                $ comfort += 10
                "{i}Beep! Beep! Beep!{/i}"
                scene bg bedroom
                with dissolve_scene
                'My rest is rudely interrupted by my alarm.'
                'Even if I wanted to go back to sleep, I\'m wide awake now.'
                stop music
                'I dismiss my alarm, dragging myself out of bed, then get dressed for the day ahead.'
                jump room_menu
            else:
                '...'
                $ fatigue -= 95
                $ comfort += 20
                scene bg bedroom
                with dissolve_scene
                'I wake up, feeling refreshed and ready for the day.'
                'I get out of bed and get dressed for the day ahead.'
                jump room_menu

        "Play a Video Game":
            'I take my Nintendo Switch from the side of my bed and turn it on.'
            menu:
                "I play..."

                "Breath Of The Wild":
                    'I open Breath Of The Wild and play it for a while.'
                    'I enjoy this game.'
                    $ stress -= 7
                    $ comfort += 3
                    jump room_menu

                "Minecraft":
                    'I open Minecraft and work on my world for a while.'
                    'This is fun.'
                    $ stress -= 7
                    $ comfort += 3
                    jump room_menu
