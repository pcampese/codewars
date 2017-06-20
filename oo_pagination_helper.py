# https://www.codewars.com/kata/paginationhelper/train/python

import math

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
  
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)    # Length == number of items
  
    # returns the number of pages
    def page_count(self):
        return math.ceil(self.item_count() / float(self.items_per_page))    # Roundup (ceiling) items / items-per-page
	
    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        if (0 <= page_index < self.page_count() and self.collection):      # If the page of interest is within the valid range and collection isn't empty.
                                                                           # We must do '<' instead of '<=' since page_index is zero-based, and page_count isn't
            full_pages = (self.item_count() // self.items_per_page) - 1    # Determine which pages are full
            if (page_index <= full_pages):                                 # If it's on a fully populated page
                count = self.items_per_page                                # then, return the number of items on each page
            else:                                                     # If it's a page that's not fully populated (last page)
                count = len(self.collection) % self.items_per_page    # Return remainder of: (collection size) / (items per page)
        else:             # If the page of interested isn't in a valid range
            count = -1    # Return -1
        
        return count
  
    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        if (0 <= item_index < self.item_count() and self.collection):    # If item in a valid range and collection isn't empty
            index = math.ceil(item_index / self.items_per_page)          # then round up the item index / page result
        else:                                                            # If item is not in a valid range
            index = -1                                                   # then return -1
        return index