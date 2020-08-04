# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def increase_quality(self, item, value = 1):
        new_quality = item.quality + value
        if new_quality > 50:
            item.quality = 50
        else:
            item.quality = new_quality

    def decrease_quality(self, item, value = 1):
        new_quality = item.quality - value
        if new_quality < 0:
            item.quality = 0        # quality is never negative
        else:
            item.quality = new_quality

    def update_quality(self):
        for item in self.items:
            
            # Update sell_in for all items
            item.sell_in -= 1

            # Sulfuras, Hand of Ragnaros
            if item.name == "Sulfuras, Hand of Ragnaros":
                break

            # Aged Brie
            if item.name == "Aged Brie":
                if item.sell_in < 0:
                    self.increase_quality(item, 2)
                    break
                else:
                    self.increase_quality(item)
                    break

            # Backstage passes
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    item.quality = 0
                    break
                elif 6 <= item.sell_in <= 10:
                    self.increase_quality(item, 2)
                    break
                elif 0 < item.sell_in <= 5:
                    self.increase_quality(item, 3)
                    break
                else:
                    self.increase_quality(item)
                    break

            # Conjured
            if item.name.split(' ', 1)[0] == "Conjured":
                if item.sell_in > 0:
                    self.decrease_quality(item, 2)  # decrease twice as fast as normal items
                    break
                else:
                    self.decrease_quality(item, 4)  # double twice as fast!
                    break

            # Normal items
            if item.sell_in < 0:
                self.decrease_quality(item, 2)
            else:
                self.decrease_quality(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

