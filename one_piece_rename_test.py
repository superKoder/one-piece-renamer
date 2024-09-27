import unittest

from one_piece_rename import convert_episode, convert_filename


class OnePieceRenameTests(unittest.TestCase):

    def test_convert_episode(self):

        # Season 1 has 8 episodes, from 1 to 8
        self.assertEqual(convert_episode(1), "S01E01")
        self.assertEqual(convert_episode(2), "S01E02")
        self.assertEqual(convert_episode(8), "S01E08")

        # Season 2 has 22 episodes, from 9 to 30
        self.assertEqual(convert_episode(9), "S02E01")
        self.assertEqual(convert_episode(30), "S02E22")

        # Season 3 has 17 episodes, from 31 to 47
        self.assertEqual(convert_episode(31), "S03E01")
        self.assertEqual(convert_episode(47), "S03E17")

        # Season 7 has 39 episodes, from 92 to 130
        self.assertEqual(convert_episode(92), "S07E01")
        self.assertEqual(convert_episode(130), "S07E39")

        # Season 13 has 100 episodes, from 382 to 481
        self.assertEqual(convert_episode(382), "S13E01")
        self.assertEqual(convert_episode(481), "S13E100")

        # Season 21 has 194 episodes, from 891 to 1084
        self.assertEqual(convert_episode(891), "S21E01")
        self.assertEqual(convert_episode(1084), "S21E194")

    def test_improved_filename(self):

        # Simple, made-up test cases
        self.assertEqual(convert_filename(
            "one.piece.1.mkv"), "One Piece S01E01.mkv")
        self.assertEqual(convert_filename(
            "One Piece 1.mkv"), "One Piece S01E01.mkv")
        self.assertEqual(convert_filename(
            "one.piece.12.mkv"), "One Piece S02E04.mkv")
        self.assertEqual(convert_filename(
            "One Piece 12.mkv"), "One Piece S02E04.mkv")
        self.assertEqual(convert_filename(
            "one.piece.123.mkv"), "One Piece S07E32.mkv")
        self.assertEqual(convert_filename(
            "One Piece 123.mkv"), "One Piece S07E32.mkv")

        # Real-word examples that need renaming
        self.assertEqual(convert_filename("One Piece - 758 (1080p FUNI WEB-DL -KS-).mkv"),
                         "One Piece S18E13 (1080p FUNI WEB-DL -KS-).mkv")
        self.assertEqual(convert_filename("One Piece 758 (1080p FUNI WEB-DL -KS-).mkv"),
                         "One Piece S18E13 (1080p FUNI WEB-DL -KS-).mkv")

        # Real-word examples that don't need renaming
        self.assertEqual(convert_filename("One Piece S03E10 (1080p FUNI WEB-DL -KS-).mkv"),
                         "One Piece S03E10 (1080p FUNI WEB-DL -KS-).mkv")
        self.assertEqual(convert_filename("One Piece S16e20 Shocking! The True Identity Of The Mystery Man Vergo!.mkv"),
                         "One Piece S16e20 Shocking! The True Identity Of The Mystery Man Vergo!.mkv")

        # Real-word special cases that need renaming
        self.assertEqual(convert_filename("One Piece - 717 - Trueno Bastardo! Kyros' Furious Strike! (1080p FUNI WEB-DL -KS-).mkv"),
                         "One Piece S17E90 - Trueno Bastardo! Kyros' Furious Strike! (1080p FUNI WEB-DL -KS-).mkv")
        self.assertEqual(convert_filename("One Piece - 711 - The Man's Pride! Bellamy's Last Charge! (1080p FUNI WEB-DL -KS-).mkv"),
                         "One Piece S17E84 - The Man's Pride! Bellamy's Last Charge! (1080p FUNI WEB-DL -KS-).mkv")
        self.assertEqual(convert_filename("One Piece - 729 - Flame Dragon King! Protect Luffy's Life! (1080p FUNI WEB-DL -KS-).mkv"),
                         "One Piece S17E102 - Flame Dragon King! Protect Luffy's Life! (1080p FUNI WEB-DL -KS-).mkv")
        self.assertEqual(convert_filename("One Piece - 655 (1080p FUNI WEB-DL AAC2.0 -KS-).mkv"),
                         "One Piece S17E28 (1080p FUNI WEB-DL AAC2.0 -KS-).mkv")

        # Real-word special cases that don't need renaming
        self.assertEqual(convert_filename("One Piece S04E13 Through the Sky They Soar! The 1000 Year Legend Lives Again!.mkv"),
                         "One Piece S04E13 Through the Sky They Soar! The 1000 Year Legend Lives Again!.mkv")
        self.assertEqual(convert_filename("One Piece S07E12 Spiders Café at 8 o'Clock! The Enemy Leaders Gather!.mkv"),
                         "One Piece S07E12 Spiders Café at 8 o'Clock! The Enemy Leaders Gather!.mkv")
        self.assertEqual(convert_filename("One Piece S09E32 Chance of Survival 0%!! Pirate Chopper vs. Shinto Priest Ohm.mkv"),
                         "One Piece S09E32 Chance of Survival 0%!! Pirate Chopper vs. Shinto Priest Ohm.mkv")
        self.assertEqual(convert_filename("One Piece S10E08 The Pirate Ship Disappears! Stronghold Battle, Round 2.mkv"),
                         "One Piece S10E08 The Pirate Ship Disappears! Stronghold Battle, Round 2.mkv")
        self.assertEqual(convert_filename("One Piece S13E50 The Trap of Chief Guard Saldeath - Level 3 Starvation Hell.mkv"),
                         "One Piece S13E50 The Trap of Chief Guard Saldeath - Level 3 Starvation Hell.mkv")
        self.assertEqual(convert_filename("One Piece S13E11 New Rivals Gather! The 11 Supernovas.mkv"),
                         "One Piece S13E11 New Rivals Gather! The 11 Supernovas.mkv")


if __name__ == "__main__":
    unittest.main()
