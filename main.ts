input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 6))
})
basic.showString("Hei")
music.playSoundEffect(music.createSoundEffect(
WaveShape.Noise,
5000,
1,
255,
255,
500,
SoundExpressionEffect.None,
InterpolationCurve.Linear
), SoundExpressionPlayMode.UntilDone)
basic.forever(function () {
	
})
