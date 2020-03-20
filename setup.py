import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Math Game",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": [("sound_files/begin_digits.wav", "sound_files/begin_digits.wav"),
                                             ("sound_files/you_chose.wav", "sound_files/you_chose.wav"),
                                             ("sound_files/count_0_to_10.wav", "sound_files/count_0_to_10.wav"),
                                             ("sound_files/find_number.wav", "sound_files/find_number.wav"),
                                             ("sound_files/find_the_digit.wav", "sound_files/find_the_digit.wav"),
                                             ("sound_files/found_digit.wav", "sound_files/found_digit.wav"),
                                             ("sound_files/found_number.wav", "sound_files/found_number.wav"),
                                             ("sound_files/intro.wav", "sound_files/intro.wav"),
                                             ("sound_files/not_right.wav", "sound_files/not_right.wav"),
                                             ("sound_files/numbers_from_digits.wav", "sound_files/numbers_from_digits.wav"),
                                             ("sound_files/only_10_digits.wav", "sound_files/only_10_digits.wav"),
                                             ("sound_files/rec_digits_learn_count.wav", "sound_files/rec_digits_learn_count.wav"),
                                             ("sound_files/say_together.wav", "sound_files/say_together.wav"),
                                             ("sound_files/try_again.wav", "sound_files/try_again.wav"),
                                             ("sound_files/very_good.wav", "sound_files/very_good.wav"),
                                             ("sound_files/the_number.wav", "sound_files/the_number.wav"),
                                             ("sound_files/looks_like.wav", "sound_files/looks_like.wav"),
                                             ("sound_files/button.wav", "sound_files/button.wav"),
                                             ("sound_files/click_the.wav", "sound_files/click_the.wav"),
                                             ("sound_files/for_letters.wav", "sound_files/for_letters.wav"),
                                             ("sound_files/for_numbers.wav", "sound_files/for_numbers.wav"),
                                             ("sound_files/numbers_or_letters.wav", "sound_files/numbers_or_letters.wav"),
                                             ("sound_files/colors/blue.wav", "sound_files/colors/blue.wav"),
                                             ("sound_files/colors/green.wav", "sound_files/colors/green.wav"),
                                             ("sound_files/colors/orange.wav", "sound_files/colors/orange.wav"),
                                             ("sound_files/colors/purple.wav", "sound_files/colors/purple.wav"),
                                             ("sound_files/colors/red.wav", "sound_files/colors/red.wav"),
                                             ("sound_files/colors/yellow.wav", "sound_files/colors/yellow.wav"),
                                             ("sound_files/numbers/zero.wav", "sound_files/numbers/zero.wav"),
                                             ("sound_files/numbers/one.wav", "sound_files/numbers/one.wav"),
                                             ("sound_files/numbers/two.wav", "sound_files/numbers/two.wav"),
                                             ("sound_files/numbers/three.wav", "sound_files/numbers/three.wav"),
                                             ("sound_files/numbers/four.wav", "sound_files/numbers/four.wav"),
                                             ("sound_files/numbers/five.wav", "sound_files/numbers/five.wav"),
                                             ("sound_files/numbers/five.wav", "sound_files/numbers/five.wav"),
                                             ("sound_files/numbers/six.wav", "sound_files/numbers/six.wav"),
                                             ("sound_files/numbers/seven.wav", "sound_files/numbers/seven.wav"),
                                             ("sound_files/numbers/eight.wav", "sound_files/numbers/eight.wav"),
                                             ("sound_files/numbers/nine.wav", "sound_files/numbers/nine.wav"),
                                             ("sound_files/numbers/ten.wav", "sound_files/numbers/ten.wav"),
                                             ("sound_files/numbers/eleven.wav", "sound_files/numbers/eleven.wav"),
                                             ("sound_files/numbers/twelve.wav", "sound_files/numbers/twelve.wav"),
                                             ("sound_files/numbers/thirteen.wav", "sound_files/numbers/thirteen.wav"),
                                             ("sound_files/numbers/fourteen.wav", "sound_files/numbers/fourteen.wav"),
                                             ("sound_files/numbers/fifteen.wav", "sound_files/numbers/fifteen.wav"),
                                             ("sound_files/numbers/sixteen.wav", "sound_files/numbers/sixteen.wav"),
                                             ("sound_files/numbers/seventeen.wav", "sound_files/numbers/seventeen.wav"),
                                             ("sound_files/numbers/eighteen.wav", "sound_files/numbers/eighteen.wav"),
                                             ("sound_files/numbers/nineteen.wav", "sound_files/numbers/nineteen.wav"),
                                             ("sound_files/numbers/twenty.wav", "sound_files/numbers/twenty.wav"),
                                             ("sound_files/alphabet/begin_sing.wav", "sound_files/alphabet/begin_sing.wav"),
                                             ("sound_files/alphabet/find_letter.wav", "sound_files/alphabet/find_letter.wav"),
                                             ("sound_files/alphabet/learn_alphabet.wav", "sound_files/alphabet/learn_alphabet.wav"),
                                             ("sound_files/alphabet/sing_alphabet.wav", "sound_files/alphabet/sing_alphabet.wav"),
                                             ("sound_files/alphabet/alphabet_song.wav", "sound_files/alphabet/alphabet_song.wav"),
                                             ("sound_files/alphabet/letters/a.wav", "sound_files/alphabet/letters/a.wav"),
                                             ("sound_files/alphabet/letters/b.wav", "sound_files/alphabet/letters/b.wav"),
                                             ("sound_files/alphabet/letters/c.wav", "sound_files/alphabet/letters/c.wav"),
                                             ("sound_files/alphabet/letters/d.wav", "sound_files/alphabet/letters/d.wav"),
                                             ("sound_files/alphabet/letters/e.wav", "sound_files/alphabet/letters/e.wav"),
                                             ("sound_files/alphabet/letters/f.wav", "sound_files/alphabet/letters/f.wav"),
                                             ("sound_files/alphabet/letters/g.wav", "sound_files/alphabet/letters/g.wav"),
                                             ("sound_files/alphabet/letters/h.wav", "sound_files/alphabet/letters/h.wav"),
                                             ("sound_files/alphabet/letters/i.wav", "sound_files/alphabet/letters/i.wav"),
                                             ("sound_files/alphabet/letters/j.wav", "sound_files/alphabet/letters/j.wav"),
                                             ("sound_files/alphabet/letters/k.wav", "sound_files/alphabet/letters/k.wav"),
                                             ("sound_files/alphabet/letters/l.wav", "sound_files/alphabet/letters/l.wav"),
                                             ("sound_files/alphabet/letters/m.wav", "sound_files/alphabet/letters/m.wav"),
                                             ("sound_files/alphabet/letters/n.wav", "sound_files/alphabet/letters/n.wav"),
                                             ("sound_files/alphabet/letters/o.wav", "sound_files/alphabet/letters/o.wav"),
                                             ("sound_files/alphabet/letters/p.wav", "sound_files/alphabet/letters/p.wav"),
                                             ("sound_files/alphabet/letters/q.wav", "sound_files/alphabet/letters/q.wav"),
                                             ("sound_files/alphabet/letters/r.wav", "sound_files/alphabet/letters/r.wav"),
                                             ("sound_files/alphabet/letters/s.wav", "sound_files/alphabet/letters/s.wav"),
                                             ("sound_files/alphabet/letters/t.wav", "sound_files/alphabet/letters/t.wav"),
                                             ("sound_files/alphabet/letters/u.wav", "sound_files/alphabet/letters/u.wav"),
                                             ("sound_files/alphabet/letters/v.wav", "sound_files/alphabet/letters/v.wav"),
                                             ("sound_files/alphabet/letters/w.wav", "sound_files/alphabet/letters/w.wav"),
                                             ("sound_files/alphabet/letters/x.wav", "sound_files/alphabet/letters/x.wav"),
                                             ("sound_files/alphabet/letters/y.wav", "sound_files/alphabet/letters/y.wav"),
                                             ("sound_files/alphabet/letters/z.wav", "sound_files/alphabet/letters/z.wav"),
                                             ("images/numbers_highlight.png", "images/numbers_highlight.png"),
                                             ("images/spritesheet_numbers_plain.png", "images/spritesheet_numbers_plain.png"),
                                             ("images/abc.png", "images/abc.png"),
                                             ("images/abc_highlight.png", "images/abc_highlight.png"),
                                             ("images/abc_lower.png", "images/abc_lower.png"),
                                             ("images/abc_lower_highlight.png", "images/abc_lower_highlight.png"),
                                             ("images/skip_arrows.png", "images/skip_arrows.png")]}},
    executables=executables
)


