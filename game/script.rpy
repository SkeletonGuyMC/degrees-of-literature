## script.rpy

# This is the main script that Ren'Py calls upon to start
# your mod's story!

label start:

    # This label configures the anticheat number for the game after Act 1.
    # It is recommended to leave this as-is and use the following in your script:
    #   $ persistent.anticheat = renpy.random.randint(X, Y)
    #   X - The minimum number | Y - The maximum number
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    ## Names of the Characters
    # These variables set up the names of the characters in the game.
    # To add a character, use the following example below:
    #   $ mi_name = "Mike".
    # Don't forget to add the character to 'definitions.rpy'!
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ mu_name = "Mom"
    $ t_name = "Naoki"
    $ l_name = "Lemon"

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None

    # These variables controls whether the player can skip dialogue or transitions.
    $ allow_skipping = True
    $ config.allow_skipping = True

    ## The Main Part of the Script
    # This is where your script code is called!
    # 'persistent.playthrough' controls the playthrough number the player is on i.e (Act 1, 2, 3, 4)
    if persistent.playthrough == 0:

        # This variable sets the chapter number to X depending on the chapter
        # your player is experiencing ATM.
        $ chapter = 0

        # This call statement calls your script label to be played.
        call mod_passport

image mother 1b = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/b.png")
image mother 1c = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/c.png")
image mother 1a = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/a.png")
image mother 1d = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/d.png")
image mother 1e = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/e.png")
image mother 1f = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/f.png")
image mother 1g = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/g.png")
image mother 1h = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/h.png")
image mother 1i = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/i.png")
image mother 1j = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/j.png")
image mother 1k = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/k.png")
image mother 1l = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/l.png")
image mother 1m = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/m.png")
image mother 1n = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/n.png")
image mother 1o = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/o.png")
image mother 1p = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/p.png")
image mother 1q = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/q.png")
image mother 1r = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/r.png")
image mother 1s = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/s.png")
image mother 1t = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/t.png")
image mother 1u = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/u.png")
image mother 1v = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/v.png")
image mother 1w = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/w.png")
image mother 1x = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/x.png")
image mother 1y = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/y.png")
image mother 1ja = im.Composite((960, 960), (0, 0), "mod_assets/jayden/1b.png", (0, 31), "mod_assets/jayden/ja.png")

image lemon 2a = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/a.png")
image lemon 2b = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/b.png")
image lemon 2c = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/c.png")
image lemon 2d = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/d.png")
image lemon 2e = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/e.png")
image lemon 2e2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/e2.png")
image lemon 2f = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/f.png")
image lemon 2f2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/f2.png")
image lemon 2g = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/g.png")
image lemon 2g2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/g2.png")
image lemon 2h = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/h.png")
image lemon 2i = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/i.png")
image lemon 2j = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/j.png")
image lemon 2k = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/k.png")
image lemon 2l = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/l.png")
image lemon 2m = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/m.png")
image lemon 2n = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/n.png")
image lemon 2o = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/o.png")
image lemon 2p = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/p.png")
image lemon 2q = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/q.png")
image lemon 2q2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/q2.png")
image lemon 2r = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/r.png")
image lemon 2s = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/s.png")
image lemon 2s2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/s2.png")
image lemon 2t = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/t.png")
image lemon 2u = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/u.png")
image lemon 2v = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/v.png")
image lemon 2w = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/w.png")
image lemon 2x = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/x.png")
image lemon 2y = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/y.png")
image lemon 2z = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/z.png")
image lemon 2shock = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2l.png", (0, 0), "mod_assets/lemon/2r.png", (0, 0), "mod_assets/lemon/shock.png")
image lemon 1a = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/a.png")
image lemon 1b = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/b.png")
image lemon 1c = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/c.png")
image lemon 1d = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/d.png")
image lemon 1e = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/e.png")
image lemon 1e2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/e2.png")
image lemon 1f = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/f.png")
image lemon 1f2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/f2.png")
image lemon 1g = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/g.png")
image lemon 1g2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/g2.png")
image lemon 1h = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/h.png")
image lemon 1i = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/i.png")
image lemon 1j = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/j.png")
image lemon 1k = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/k.png")
image lemon 1l = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/l.png")
image lemon 1m = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/m.png")
image lemon 1n = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/n.png")
image lemon 1o = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/o.png")
image lemon 1p = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/p.png")
image lemon 1q = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/q.png")
image lemon 1q2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/q2.png")
image lemon 1r = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/r.png")
image lemon 1s = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/s.png")
image lemon 1s2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/s2.png")
image lemon 1t = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/t.png")
image lemon 1u = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/u.png")
image lemon 1v = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/v.png")
image lemon 1w = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/w.png")
image lemon 1x = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/x.png")
image lemon 1y = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/y.png")
image lemon 1z = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/z.png")
image lemon shock = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1l.png", (0, 0), "mod_assets/lemon/1r.png", (0, 0), "mod_assets/lemon/shock.png")
image lemon 1ba = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/a.png")
image lemon 1bb = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/b.png")
image lemon 1bc = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/c.png")
image lemon 1bd = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/d.png")
image lemon 1be = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/e.png")
image lemon 1be2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/e2.png")
image lemon 1bf = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/f.png")
image lemon 1bf2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/f2.png")
image lemon 1bg = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/g.png")
image lemon 1bg2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/g2.png")
image lemon 1bh = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/h.png")
image lemon 1bi = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/i.png")
image lemon 1bj = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/j.png")
image lemon 1bk = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/k.png")
image lemon 1bl = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/l.png")
image lemon 1bm = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/m.png")
image lemon 1bn = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/n.png")
image lemon 1bo = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/o.png")
image lemon 1bp = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/p.png")
image lemon 1bq = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/q.png")
image lemon 1bq2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/q2.png")
image lemon 1br = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/r.png")
image lemon 1bs = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/s.png")
image lemon 1bs2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/s2.png")
image lemon 1bt = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/t.png")
image lemon 1bu = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/u.png")
image lemon 1bv = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/v.png")
image lemon 1bw = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/w.png")
image lemon 1bx = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/x.png")
image lemon 1by = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/y.png")
image lemon 1bz = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/z.png")
image lemon bshock = im.Composite((960, 960), (0, 0), "mod_assets/lemon/1cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/shock.png")
image lemon 2ba = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/a.png")
image lemon 2bb = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/b.png")
image lemon 2bc = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/c.png")
image lemon 2bd = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/d.png")
image lemon 2be = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/e.png")
image lemon 2be2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/e2.png")
image lemon 2bf = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/f.png")
image lemon 2bf2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/f2.png")
image lemon 2bg = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/g.png")
image lemon 2bg2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/g2.png")
image lemon 2bh = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/h.png")
image lemon 2bi = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/i.png")
image lemon 2bj = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/j.png")
image lemon 2bk = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/k.png")
image lemon 2bl = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/l.png")
image lemon 2bm = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/m.png")
image lemon 2bn = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/n.png")
image lemon 2bo = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/o.png")
image lemon 2bp = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/p.png")
image lemon 2bq = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/q.png")
image lemon 2bq2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/q2.png")
image lemon 2br = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/r.png")
image lemon 2bs = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/s.png")
image lemon 2bs2 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/s2.png")
image lemon 2bt = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/t.png")
image lemon 2bu = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/u.png")
image lemon 2bv = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/v.png")
image lemon 2bw = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/w.png")
image lemon 2bx = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/x.png")
image lemon 2by = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/y.png")
image lemon 2bz = im.Composite((960, 960), (0, 0), "mod_assets/lemon/2cl.png", (0, 0), "mod_assets/lemon/2cr.png", (0, 0), "mod_assets/lemon/z.png")
image lemon 3a = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/a.png")
image lemon 3b = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/b.png")
image lemon 3c = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/c.png")
image lemon 3d = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/d.png")
image lemon 3e = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/e.png")
image lemon 3f = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/f.png")
image lemon 3g = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/g.png")
image lemon 3h = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/h.png")
image lemon 3i = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/i.png")
image lemon 3j = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/j.png")
image lemon 3k = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/k.png")
image lemon 3l = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/l.png")
image lemon 3m = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/m.png")
image lemon 3n = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/n.png")
image lemon 3o = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/o.png")
image lemon 3p = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/p.png")
image lemon 3q = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/q.png")
image lemon 3r = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/r.png")
image lemon 3s = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/s.png")
image lemon 3t = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/t.png")
image lemon 3u = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/u.png")
image lemon 3v = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/v.png")
image lemon 3w = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/w.png")
image lemon 3x = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/x.png")
image lemon 3y = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/y.png")
image lemon 3z = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3.png", (0, 0), "mod_assets/lemon/z.png")
image lemon 3ba = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/a.png")
image lemon 3bb = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/b.png")
image lemon 3bc = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/c.png")
image lemon 3bd = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/d.png")
image lemon 3be = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/e.png")
image lemon 3bf = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/f.png")
image lemon 3bg = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/g.png")
image lemon 3bh = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/h.png")
image lemon 3bi = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/i.png")
image lemon 3bj = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/j.png")
image lemon 3bk = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/k.png")
image lemon 3bl = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/l.png")
image lemon 3bm = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/m.png")
image lemon 3bn = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/n.png")
image lemon 3bo = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/o.png")
image lemon 3bp = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/p.png")
image lemon 3bq = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/q.png")
image lemon 3br = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/r.png")
image lemon 3bs = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/s.png")
image lemon 3bt = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/t.png")
image lemon 3bu = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/u.png")
image lemon 3bv = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/v.png")
image lemon 3bw = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/w.png")
image lemon 3bx = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/x.png")
image lemon 3by = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/y.png")
image lemon 3bz = im.Composite((960, 960), (0, 0), "mod_assets/lemon/3b.png", (0, 0), "mod_assets/lemon/z.png")
image lemon 4 = im.Composite((960, 960), (0, 0), "mod_assets/lemon/4cl.png", (0, 0), "mod_assets/lemon/1cr.png", (0, 0), "mod_assets/lemon/g.png")

image bg hallway = "mod_assets/hallway.png"
image living_room = "mod_assets/living_room.png"

image bg residential_night = "mod_assets/residential_night.png"
image bg house_night = "mod_assets/house_night.png"
image bg car_night = "mod_assets/only_used_like_once_lol.png"
image bg living_room_night = "mod_assets/living_room_night.png"
image bg bedroom_night = "mod_assets/bedroom_night.png"

# stats screen code
screen stats_screen():

    tag menu
    key "mouseup_1" action NullAction()
    key "space" action NullAction()
    key "enter" action NullAction()
    key "return" action NullAction()


    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Stats"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "{size=+10}{b}Stats{/b}\n{/size}"


            text _("{b}Current State{/b}\nHealth: [health]/100\nFatigue: [fatigue]/100\nStress: [stress]/100\nComfort: [comfort]/100\nMood: [mood]\n\n")

            text "{b}Attributes{/b}\nPhysique: [physiquerank] ([physique]%)\nIntelligence: [intelligencerank] ([intelligence]%)\nSocial: [socialrank] ([social]%)\nSkulduggery: [skulduggeryrank] ([skulduggery]%)\n\n"

            text "{b}Skills{/b}\nCombat: [combat]/200\nRunning: [running]/200\nLearning: [learning]/200\nGaming: [gaming]/200\nPublic Speaking: [publicspeaking]/200\nTeamwork: [teamwork]/200\nTheft: [theft]/200\nCharisma: [charisma]/200\n"

            textbutton "{size=+10}Close{/size}" action [Hide(screen="stats_screen")]

# social screen code
screen social_screen():

    tag menu
    key "mouseup_1" action NullAction()
    key "space" action NullAction()
    key "enter" action NullAction()
    key "return" action NullAction()

    if sayori_li == 1:
        $ s_relationshipname = "Sayori {color=#fc8ae3}(Dating){/color}"
    else:
        $ s_relationshipname = "Sayori"
    if monika_li == 1:
        $ m_relationshipname = "Monika {color=#fc8ae3}(Dating){/color}"
    else:
        $ m_relationshipname = "Monika"
    if natsuki_li == 1:
        $ n_relationshipname = "Natsuki {color=#fc8ae3}(Dating){/color}"
    else:
        $ n_relationshipname = "Natsuki"
    if yuri_li == 1:
        $ y_relationshipname = "Yuri {color=#fc8ae3}(Dating){/color}"
    else:
        $ y_relationshipname = "Yuri"
    if naoki_li == 1:
        $ t_relationshipname = "Naoki {color=#fc8ae3}(Dating){/color}"
    else:
        $ t_relationshipname = "Naoki"
    if lemon_li == 1:
        $ l_relationshipname = "Lemon {color=#fc8ae3}(Dating){/color}"
    else:
        $ l_relationshipname = "Lemon"

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Social"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "{size=+15}Social\n{/size}"

            text "{size=+5}{b}Relationships{/b}\n{/size}"

            if monika_met == "False" and sayori_met == "False" and natsuki_met == "False" and yuri_met == "False" and trevor_met == "False" and lemon_met == "False":
                text "No relationships (yet!).\n"

            if monika_met == "True":
                if monika_dismissed == True:
                    text "Monika {b}has been deleted{/b}.\n"
                elif m_awareness_known == "True":
                    text "{b}{color=#3BF761}[m_relationshipname]{/color}{/b}\nLove: [m_love]%\nAwareness: [m_awareness]%\nJealousy: [m_jealousy]%\n"
                else:
                    text "{b}{color=#3BF761}[m_relationshipname]{/color}{/b}\nLove: [m_love]%\nJealousy: [m_jealousy]%\n"

            if sayori_met == "True":
                if sayori_dismissed == True:
                    text "Sayori {b}is gone.{/b}\n"
                elif s_depression_known == "True":
                    text "{b}{color=#3BF7E5}[s_relationshipname]{/color}{/b}\nLove: [s_love]%\nHappiness: [s_happiness]%\nJealousy: [s_jealousy]%\n"
                else:
                    text "{b}{color=#3BF7E5}[s_relationshipname]{/color}{/b}\nLove: [s_love]%\nJealousy: [s_jealousy]%\n"

            if natsuki_met == "True":
                if natsuki_dismissed == True:
                    text "Natsuki {b}has gone missing.{/b}\n"
                elif n_abuse_known == "True":
                    text "{b}{color=#FC3BD5}[n_relationshipname]{/color}{/b}\nLove: [n_love]%\nTrust: [n_trust]%\nJealousy: [n_jealousy]%\n"
                else:
                    text "{b}{color=#FC3BD5}[n_relationshipname]{/color}{/b}\nLove: [n_love]%\nJealousy: [n_jealousy]%\n"

            if yuri_met == "True":
                if yuri_dismissed == True:
                    text "Yuri {b}is dead.{/b}\n"
                elif y_anxiety_known == "True":
                    text "{b}{color=#DC26F7}[y_relationshipname]{/color}{/b}\nLove: [y_love]%\nConfidence: [y_confidence]%\nJealousy: [y_jealousy]%\n"
                else:
                    text "{b}{color=#DC26F7}[y_relationshipname]{/color}{/b}\nLove: [y_love]%\nSanity: [y_jealousy]%\n"

            if trevor_met == "True":
                if naoki_dismissed == True:
                    text "{b}Something happened{/b} to Naoki.\n"
                elif t_protective_known == "True":
                    text "{b}[t_relationshipname]{/b}\nLove: [t_love]%\nSuspicion: [t_suspicion]%\nJealousy: [t_jealousy]%\n"
                else:
                    text "{b}[t_relationshipname]{/b}\nLove: [t_love]%\nJealousy: [t_jealousy]%\n"

            if lemon_met == "True":
                if lemon_dismissed == True:
                    text "Lemon {b}is in hospital{/b}\n"
                if lemon_energy_known == "True":
                    text "{b}[l_relationshipname]{/b}\nLove: [l_love]%\nAddiction: [l_addiction]%\nJealousy: [l_jealousy]%\n"
                else:
                    text "{b}[l_relationshipname]{/b}\nLove: [l_love]%\nJealousy: [l_jealousy]%\n"


            text "{size=+5}{b}School{/b}{/size}\n"

            text "{b}Club{/b}"
            if in_literature_club == "True":
                text "You are in the {b}Literature Club{/b}.\n"
            elif in_track_team == "True":
                text "You are in the {b}Track Team{/b}.\n"
            elif in_debate_club == "True":
                text "You are in the {b}Debate Club{/b}.\n"
            else:
                text "You are not in a club.\n"

            text "{b}Grades{/b}"
            text "Japanese: [japanesegrade]"
            text "Maths: [mathsgrade]"
            text "History: [historygrade]"
            text "Science: [sciencegrade]\n"

            text "{b}Electives{/b}"
            if musictaken == "True":
                text "Music: [musicgrade]"
            if sporttaken == "True":
                text "Sport: [sportgrade]"
            if programmingtaken == "True":
                text "Programming: [programminggrade]"
            if musictaken == "False" and sporttaken == "False" and programmingtaken == "False":
                text "You have not taken any electives."
            text "You can take new electives at the start of each semester.\n"

            text "{size=+5}{b}Other{/b}{/size}\n"

            text "{b}Crime{/b}"
            if crimelevel >= 75:
                text "The police {color=#E90000}have enough evidence to detain you, and are searching for you{/color}.\n"
            elif crimelevel >= 30:
                text "The police {color=#E90000}have enough evidence to detain you{/color}.\n"
            elif crimelevel >= 1:
                text "The police {color=#483DEE}have you on their records, but don\'t have enough evidence for an arrest{/color}.\n"
            elif crimelevel == 0:
                text "The police {color=#26E94D}consider you innocent{/color}.\n"

            text "{b}Social{/b}"
            text "Unfinished!\n"

            textbutton "{size=+10}Close{/size}" action [Hide(screen="social_screen")]

# journal code
screen journal_screen():

    tag menu
    key "mouseup_1" action NullAction()
    key "space" action NullAction()
    key "enter" action NullAction()
    key "return" action NullAction()

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

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Journal"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "{size=+15}{b}Journal{/b}\n{/size}"

            text "Your name is {b}[player]{/b}.\nYour pronouns are [he_capital]/[him_capital].\n"
            if school_break == "True":
                text "It is currently a school break.\n"
            else:
                text "You have school from Monday to Friday, from 8:30 to 15:30.\n"
            text "You have $[money] in savings.\n"
            text "It has been [daycount] days, [weekcount] weeks, [monthcount] months\nand [yearcount] years since you started.\n"

            textbutton "{size=+10}Close{/size}" action [Hide(screen="journal_screen")]

# music player code
screen music_screen():

    tag menu
    key "mouseup_1" action NullAction()
    key "space" action NullAction()
    key "enter" action NullAction()
    key "return" action NullAction()


    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Music"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "{size=+10}{b}Music{/b}\n{/size}"

            if questing == "True":
                text "Can\'t change music during a Quest!\n"
            else:
                text "Work in progress!\n"

            textbutton "{size=+10}Close{/size}" action [Hide(screen="music_screen")]
