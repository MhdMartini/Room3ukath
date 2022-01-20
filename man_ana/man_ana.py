from manim import *

poem = """
إنّي مضطرِبٌ مُنقَسِمٌ			مَفصولُ الذاتِ ومُتَّصِلُ

مكبوحُ الجأش ومُنفَجرٌ			مسلوخُ الجلدِ ومُبتهِلُ

مفقودُ الصَّبرِ ومُحتمِلٌ			ميؤوسُ الحالِ ومُؤتمِلُ

مسلولُ السَّيفِ ومُنغَمِدٌ			مسلوبُ العقلِ ومُعتَقِلُ

إنّي محروقٌ منطفئٌ         مَخنوقُ الرِّيحِ ومُشتعِلُ

مقبوضُ الغيثِ ومنهمِرٌ			مفتوحُ القلبِ ومُنقَفِلُ

صوفيُّ الرُّوحِ ومعتدِلٌ			مَرسوخُ الجَذْرِ ومُرتَحِلُ

فأنا كالدَّهرِ بأطباعي			منقوصُ الكُلِّ ومُكتمِلُ
"""

font_size = 32
line_spacing = 1.5
weight = HEAVY
color_main = GOLD_E
wait_int = 4.8
shift_mult = 6


class ManAna(Scene):
    def construct(self):
        # main loop: shift up, create down, shift up, wait
        text = Text(poem, font_size=font_size, line_spacing=line_spacing,
                    weight=weight, color=color_main, font="D050000L").shift(DOWN * shift_mult)
        self.play(FadeIn(text))

        n_verses = 8
        for i in np.arange(n_verses - 6):
            if i == 3:
                self.wait(wait_int)
            else:
                self.wait(wait_int)
            self.play(text.animate.shift(1.657 * UP))
        self.wait(2 * wait_int)
