# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_items_positive_day(self):
        items = [Item("Elixir of the Mongoose", 23, 33)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Elixir of the Mongoose", items[0].name)
        self.assertEqual(22, items[0].sell_in)
        self.assertEqual(32, items[0].quality)

    def test_normal_items_negative_day(self):
        items = [Item("Potion", -4, 46)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Potion", items[0].name)
        self.assertEqual(-5, items[0].sell_in)
        self.assertEqual(44, items[0].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 0, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(47, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -123, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(-124, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes_at_zero_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_passes_at_more_than_ten_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_at_ten_or_less_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstage_passes_at_five_or_less_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(33, items[0].quality)

    def test_conjured_positive_day(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_conjured_negative_day(self):
        items = [Item("Conjured Mana Cake", 0, 23)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

if __name__ == '__main__':
    unittest.main()

