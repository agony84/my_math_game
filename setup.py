import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Math Game",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": [("sound_files/begin_digits.wav", "sound_files/begin_digits.wav"),
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
                                             ("images/numbers_highlight.png", "images/numbers_highlight.png"),
                                             ("images/spritesheet_numbers_plain.png", "images/spritesheet_numbers_plain.png")]}},
    executables=executables
)


