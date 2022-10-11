def on_gesture_shake():
    basic.show_number(randint(1, 6))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_string("Hei")
music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
        5000,
        1,
        255,
        255,
        500,
        SoundExpressionEffect.NONE,
        InterpolationCurve.LINEAR),
    SoundExpressionPlayMode.UNTIL_DONE)

def on_forever():
    pass
basic.forever(on_forever)
